from django.urls import path
from . import views

app_name = 'scholar'

urlpatterns = [

    path('', views.home, name='home'),
    
    path('institute/dashboard/', views.institute_dashboard, name='institute_dashboard'),
    path('institute/login', views.institute_login, name='home'),
    
    path('state/login', views.state_login, name='state_login'),
    path('state_dashboard', views.state_dashboard, name='state_dashboard'),
    
    
]

