from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
from . import api
from . import api_view
from rest_framework import routers
from .auth_app import CoustomLoginView
router = routers.DefaultRouter()
router.register('studentlist', api_view.StudentViewSet, basename='student')
router.register('student-registration', api_view.StudentRegView, basename='student_registration')
urlpatterns = [           
    path('', include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('login-student/', CoustomLoginView.as_view()),
    path('accounts/login/', views.login_page, name='login_page'),
    path('accounts/logout/', views.logout_page, name='logout_page'),
    path('', views.index, name='home'),
    # ai jaiga ta faka rakla kaj kor home dela kaj kora na ba url name dela kaj kora na.
    path('about/', views.about, name='about'),
    path('student/', views.student, name='student'),
    path('student-data/<int:id>/', views.single_student, name='single_student'),
    # path('filter-student/', views.filter_student, name='filter_student'),
    # api
    path('check-password/', api.check_password, name='check_password'),
    path('filter-student-api/', api.filter_student_api, name='filter_student_api'),
    path('student-delete/<int:id>/', api.student_delete, name='student_delete'),
    
    #Forget Password
    path('password-reset/', PasswordResetView.as_view(template_name='forget.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    #Custom
    # path('password-reset/', views.PasswordReset.as_view(), name='password_reset'),
    
    #api view
    path('student-api/', api_view.student_list, name='student_api'),
    # path('student-api-viewset/', api_view.StudentViewSet.as_view({'get': 'list'}), name='student_api_viewset'),
 
]
