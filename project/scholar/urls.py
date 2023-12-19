from django.urls import path
from scholar import views
from django.contrib import admin

app_name = 'scholar'

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    # Home_Page
    path('', views.home, name='home'),
    
    # Student Scholarship Application
    path('scholar_application/', views.Scholar_application, name='Scholar_application'),
    path('scholar_application2/', views.Scholar_application2, name='Scholar_application2'),
    path('student_dashboard/',views.student_dashboard, name='student_dashboard'),
    
    # Institute
    path('institute/dashboard/', views.institute_dashboard, name='institute_dashboard'),
    path('institute/login/', views.institute_login, name='institute_login'),
    path('institute/logout/',views.institute_logout, name='institute_logout'),
    
    # State 
    path('state/login/', views.state_login, name='state_login'),
    path('state_dashboard/', views.state_dashboard, name='state_dashboard'),
    path('state/logout/', views.state_logout, name='state_logout'),
]

