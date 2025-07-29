from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django_resized import ResizedImageField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=50, choices=[('student','Student'), ('teacher','Teacher')], default='student')
    profile_pic = ResizedImageField(size=[300, 300], upload_to='profile_pics', null=True, blank=True, force_format='webp', quality=100)
    
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    def __str__(self):
        return self.user.username
    

# class Profile(AbstractUser):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     address = models.TextField()
#     profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
DEPT=[
    ("CSE", "Computer Science Engineering"),
    ("ECE", "Electronics and Communication Engineering"),
    ("ME", "Mechanical Engineering"),
    ("CE", "Civil Engineering"),
    ("EE", "Electrical Engineering"),
]
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    credits = models.IntegerField()
    semester = models.IntegerField()
    dept = models.CharField(max_length=50, choices=DEPT)
    
    def __str__(self):
        return self.name 
    
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    roll_no = models.CharField(max_length=15, unique=True, blank=True, null=True)
    dept = models.CharField(max_length=50, choices=DEPT, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_pic = ResizedImageField(size=[300, 300], upload_to="profile_pics", null=True, blank=True, force_format="webp", quality=100)
    courses = models.ManyToManyField(Course, blank=True)
    @property
    def full_name(self):
        return f"{self.user.first_name}{self.user.last_name}"
    
    def __str__(self):
        return self.user.username
