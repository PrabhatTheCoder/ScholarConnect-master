from multiprocessing import AuthenticationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
# from scholar.forms import InstituteForm
from scholar.models import *

from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


from users.models import Student,Institute,StateAuthority
from django.contrib import messages


def home(request):
    return render(request, 'scholar/homepage.html')


def institute_login(request):
    data = request.POST
    if request.method == "POST":
        username = data.get('username')
        password = data.get('password')
        
        if not InstituteUser.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username!!")
            return redirect('/Institute/login')
        
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('/institute/dashboard/')
            
        else:
            messages.error(request, 'Invalid Password!!')
            return redirect('institute/login')
    return render(request, 'scholar/institute_login.html')
        
# def institute_register(request):
#     args = {}
#     if request.method == 'POST':
#         form = InstituteForm(request.POST)     # create form object
#         if form.is_valid():
#             clearPassNoHash = form.cleaned_data['password']
#             form.password = make_password(clearPassNoHash, None, 'md5')
#             form.save()
#             form = InstituteForm()
#             print ('se salvo')
#         else:
#             print ('Error en el form')
#     else:
#         form = InstituteForm()
#     args['form'] = form #MyRegistrationForm()
#     return render(request, 'register/register.html', args)
    
def institute_logout(request):
    ...
    
def institute_dashboard(request):

    current_user = request.user
    institute = Institute.objects.get(user=current_user)

    # Get all student applications associated with the current institute
    student_applications = Student.objects.filter(institute=institute)

    context = {'student_applications': student_applications}
    return render(request, 'scholar/institute_dashboard.html')
  
def state_login(request):
    ...
    
def state_dashboard(request):
    ...  
    
def state_logout(request):
    ...

def view_details(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    docs = Docs.objects.get(student=student)
    
    context = {'student': student, 'docs': docs}
    return render(request, 'view_details.html', context)


def Scholar_application(request):
    if request.method == "POST":
        
        data = request.POST
        
        applicant_photo = request.FILES.get('applicant_photo')
        domicile_certificate = request.FILES.get('applicant_photo')
        income_certficate = request.FILES.get('income_certficate')
        caste_certificate = request.FILES.get('caste_certificate')
        aadhar_card = request.FILES.get('aadhar_card')
        bonafide = request.FILES.get('bonafide')
        fee_receipt = request.FILES.get('fee_receipt')
        passbook = request.FILES.get('passbook')
        
        institute_state = data.get('institute_state')
        institute_name = data.get('institute_name')
        
        applicant_name = data.get('applicant_name')
        father_name = data.get('father_name')
        mother_name = data.get('mother_name')
        gender = data.get('gender')
        annual_income = data.get('annual_income')
        category = data.get('category')
        religion = data.get('religion')
        course = data.get('course')
        enrollment = data.get('enrollment')
        adm_year = data.get('adm_year')
        pr_year = data.get('pr_year')
        mode = data.get('mode')
        pre_board = data.get('pre_board')
        prev_class = data.get('prev_class')
        pass_year = data.get('pass_year')
        disabled = data.get('disabled')
        parents_profession = data.get('parents_profession')
        acc_no = data.get('acc_no')
        ifsc = data.get('ifsc')
        
        student = Student.objects.create(
            
            applicant_name = applicant_name,
            father_name = father_name,
            mother_name = mother_name,
            gender = gender,
            annual_income = annual_income,
            category = category,
            religion = religion,
            course = course,
            enrollment = enrollment,
            adm_year = adm_year,
            pr_year = pr_year,
            mode = mode,
            pre_board = pre_board,
            prev_class = prev_class,
            pass_year = pass_year,
            disabled = disabled,
            parents_profession = parents_profession,
            acc_no = acc_no,
            ifsc = ifsc,
            
            institute_name = institute_name,
            
            applicant_photo = applicant_photo,
            domicile_certificate = domicile_certificate,
            income_certficate = income_certficate,
            caste_certificate = caste_certificate,
            aadhar_card = aadhar_card,
            bonafide = bonafide,
            fee_receipt = fee_receipt,
            passbook = passbook,
        )
