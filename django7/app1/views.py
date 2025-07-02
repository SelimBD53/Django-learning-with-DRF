from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from app1.models import Profile, Student
from django.contrib import messages
from watson import search
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
from django7.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
# Create your views here.
def index(request):
    CONTEXT = {}
    CONTEXT['page_title'] = 'home_page'
    CONTEXT['name'] = 'Django'
    return render(request, 'home.html', CONTEXT)
def about(request):
    CONTEXT = {
        'page_title' : 'about_page',
        'name' : 'Django'
    }
    return render(request, 'about.html', CONTEXT)

from django.db.models import Q
def filter_student(request):
    if request.method == 'GET':
        data = request.GET.get('search_data')
        queryset = Student.objects.filter(
            Q(user__username__icontains=data) | Q(user__first_name__icontains=data) | Q(user__last_name__icontains=data) | Q(user__email__icontains=data) | Q(roll_no__icontains=data) | Q(dept__icontains=data) | Q(phone__icontains=data)
        )
        
        # queryset = search.filter(Student, data)
        # | = or , & = and
    else:
        queryset = Student.objects.all()
    CONTEXT = {
        "page_title": "filter_student",
        "students": queryset,
    }
    return render(request,'student_page.html',CONTEXT)




# def check_password(request):
#     len(password) > 8:
#     is_digit()
#     is_upper()
#     is_lower()
#     is_special()
    
#     if not any(char.isdigit() for char in password):
#         return HttpResponse("Password must contain at least on digit")




def student(request):
    if request.method == 'POST':
        data = request.POST
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        password = data.get('password')
        cpassword = data.get('cpassword')
        roll = data.get('roll')
        dept = data.get('dept')
        address = data.get('address')
        phone = data.get('phone')

        if password != cpassword:
            return HttpResponse("Password and Confirm Password do not match")
        try:
            username = f"{firstname}_{lastname}_{phone[-2:]}"
            user = User.objects.create(username=username,first_name=firstname,last_name=lastname,email=email)
            user.set_password(password)  # Hash the password
            user.save()
            student = Student.objects.create(user=user,roll_no=roll,address=address,dept=dept,phone=phone)
            student.save()
            subject = "Welcome to our platform"
            message = f"""
Hello {firstname},

Welcome to our platform! Your account has been created successfully.

This is your Username:{username}
This is your Password:{password}

Best regards,
Django 7"""
            checking = send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            print(checking)
            messages.success(request, "Student Created Successfully")
        except Exception as e:
            user.delete()
            messages.error(request, str(e))
        print(user)
        if "image" in request.FILES:
            image = request.FILES['image']
            student.profile_pic = image
            student.save()

    queryset = Student.objects.all()
    CONTEXT = {
        "page_title": "student_page",
        "students": queryset,
    }
    return render(request,'student_page.html',CONTEXT)


def single_student(request, id):        ## srudent info update
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('firstname')
        student.user.first_name = first_name
        student.user.save()
        last_name = data.get('lastname')
        student.user.last_name = last_name
        student.user.save()
        messages.success(request, "Student Updated Successfully")
    CONTEXT = {
        "page_title" : "single_student",
        "single": student,
    }
    return render(request,'single_student.html',CONTEXT)
def login_page(request):
    CONTEXT = {
        "page_title" : "login_page",
    }
    if request.method =='POST':
        data = request.POST
        mail = data.get('mail')
        password = data.get('password')
        try:
            user = User.objects.get(email=mail)
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfully")
                return HttpResponse("Login Successfully")
            else:
                messages.error(request, "Invalid Credentials")
        except Exception as e:
            messages.error(request, f"{e}User does not Exist")
    return render(request,'login.html',CONTEXT)

def logout_page(request): 
    logout(request)
    return redirect('login_page')

class PasswordReset(PasswordResetView):
    template_name = 'forget.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        print(data)
        return data














