from django.contrib import admin
from .models import Profile, Student, Course
#  superuser UserName: selim
# password: 1234
# email: selim@gmail.com
# Register your models here.
class AdminProfile(admin.ModelAdmin):
    list_display = ('user','phone','address','profile_pic')
    search_fields = ('user__username','phone')
    list_filter = ('user__is_active','user__is_superuser')
    list_per_page = 10
    ordering = ('user',)
    # list_editable = ('phone', 'address', 'profile_pic')
    list_display_links = ('user', 'phone')
admin.site.register(Profile,AdminProfile)
admin.site.register(Student)
admin.site.register(Course)