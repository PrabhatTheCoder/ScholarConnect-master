
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from .forms import CustomUserForm, StudentForm
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from users.models import *
# Create your views here.


from django.contrib.auth.hashers import make_password

def register_student(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        student_form = StudentForm(request.POST)

        # Check if both forms are valid
        if user_form.is_valid() and student_form.is_valid():
            # Save the user form with user_type set to 1 for students
            user = user_form.save(commit=False)
            user.user_type = 1  # Assuming 1 represents the "Student" user type
            user.password = make_password(user_form.cleaned_data['password'])  # Manually hash the password
            user.save()

            student_group = Group.objects.get(name='Student')
            user.groups.add(student_group)

            # Save the student form with the user instance
            student = student_form.save(commit=False)
            student.user = user
            student.save()

            return HttpResponseRedirect(reverse("users:student_login"))

    else:
        user_form = CustomUserForm()
        student_form = StudentForm()

    return render(request, 'users/student_registeration.html', {'user_form': user_form, 'student_form': student_form})



def registration_success(request):
    print('it worked')
    print(request.user)
    return render(request, 'users/registration_success.html')


        
def student_login(request):
    data = request.POST
    if request.method == 'POST':
        username = data.get('abc_id')
        password = data.get('password')

        print(username,"sfjaisfh", password)
        user = authenticate(request, username = username, password=password)
        print('working')
        if user is not None:
            login(request, user)
            print('login working')
            print(user.user_type)
            if user.user_type == 1:
                print(' a student logged in')
                return HttpResponseRedirect(reverse('scholar:student_dashboard'))
        else:
            logout(request)
            messages.error(request, 'Invalid ABC ID or password.')
 
    

    return render(request, 'users/user_login.html')


def student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:student_login'))