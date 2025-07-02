from django.http import JsonResponse
from app1.models import Student
import base64
def check_password(request):
    password = request.GET.get('password')
    confirm_password = request.GET.get('cpassword')
    if password != confirm_password:
        return JsonResponse({"status": "failed", "message": "Confirm Password is not same "})
    return JsonResponse({"status": "success",})

# def user_details(request,id):
#     obj = Student.objects.get(id=id)
#     binary_data = obj.profile_pic.read() if obj.profile_pic else None
#     base64_string = base64.b64encode(binary_data).decode('utf-8') if binary_data else None
#     return JsonResponse({
#         "id": obj.id,
#         "firstname": obj.user.first_name,
#         "lastname" : obj.user.last_name,
#         "email": obj.user.email,
#         "phone": obj.phone,
#         "address": obj.address,
#         "image": base64_string,
#     })
    # return JsonResponse({"status": "success", "data": data})

def student_delete(request, id):
    try:
        obj = Student.objects.get(id=id)
        obj.delete()
        return JsonResponse({"status": "success", "message": "User deleted successfully"})
    except Student.DoesNotExist:
        return JsonResponse({"status": "failed", "message": "User not found"})
    
def filter_student_api(request):
    search = request.GET.get('search') ## [ai 'search' holo ajax ar url ar ? mark ar pora ja 'search' keyword asa sai ta.]
    if search:
        students = Student.objects.filter(user__username__icontains=search)  
    else:
        students = Student.objects.all()
    
    student_list = []
    for student in students:
        student_list.append({
            "id": student.id,
            "username": student.user.username,
            "firstname": student.user.first_name,
            "lastname": student.user.last_name,
            "email": student.user.email,
            "phone": student.phone,
            "address": student.address,
            "dept": student.dept,
            "image": student.profile_pic.url
        })
    return JsonResponse({"status": "success", "student": student_list})
        