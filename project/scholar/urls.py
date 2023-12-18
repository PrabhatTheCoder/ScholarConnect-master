from django.urls import path
from . import views

app_name = 'scholar'

urlpatterns = [
    
    # Home_Page
    path('', views.home, name='home'),
    
    # Institute
    path('institute/dashboard/', views.institute_dashboard, name='institute_dashboard'),
    path('institute/login', views.institute_login, name='home'),
    path('institute/logout_page',views.institute_logout, name='institute_logout'),
    
    # State 
    path('state/login', views.state_login, name='state_login'),
    path('state_dashboard', views.state_dashboard, name='state_dashboard'),
    path('state_dashboard', views.state_logout, name='state_logout'),
    
    
]

