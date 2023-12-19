from multiprocessing import AuthenticationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
# from scholar.forms import InstituteForm
from scholar.models import *

from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


from users.models import Student,Institute,StateAuthority
from scholar.models import Docs
from django.contrib import messages
from users.decorators import group_required


def home(request):
    return render(request, 'scholar/homepage.html')


def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    print(student)

    return render(request,'scholar/student_dashboard.html')

# def institute_login(request):
#     data = request.POST
#     if request.method == "POST":
#         username = data.get('username')
#         password = data.get('password')
        
#         try:
#             institute = Institute.objects.get(user__username=username)
#         except Institute.DoesNotExist:
#             messages.info(request, "Invalid Username!!")
#             return HttpResponseRedirect(reverse('scholar:institute_login'))
        
#         # Check if the user type is Institute
#         if institute.user.user_type != 2:  # Assuming 2 is the user_type for Institute
#             messages.error(request, 'Invalid user type. Please log in as an Institute.')
#             return HttpResponseRedirect(reverse('scholar:institute_login'))
        
#         user = authenticate(username = username, password = password)
        
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse('scholar:institute_dashboard'))
            
#         else:
#             messages.error(request, 'The user is not registered.')
#             return HttpResponseRedirect(reverse('scholar:institute_login'))

#     return render(request, 'scholar/institute_login.html')
        

def institute_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        try:
            institute = Institute.objects.get(user__username=username)
            print(institute,"institute")
        except Institute.DoesNotExist:
            messages.info(request, "Invalid Username!!")
            return HttpResponseRedirect(reverse('scholar:institute_login'))
        
        # Check if the user type is Institute
        if institute.user.user_type != 2: # Assuming 2 is the user_type for Institute
            messages.error(request, 'Invalid user type. Please log in as an Institute.')
            return HttpResponseRedirect(reverse('scholar:institute_login'))
        
        user = authenticate(username=username, password=password)
        print("authenticated")
        if user is not None and user == institute.user:
            login(request, user)
            print("logged in")
            return HttpResponseRedirect(reverse('scholar:institute_dashboard'))
        else:
            messages.error(request, 'Invalid credentials.')
            return HttpResponseRedirect(reverse('scholar:institute_login'))

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
    logout(request)
    return HttpResponseRedirect(reverse('scholar:institute_login'))
    
    
def institute_dashboard(request):

    current_user = request.user
    institute = Institute.objects.get(user=current_user)

    # Get all student applications associated with the current institute
    student_applications = Student.objects.filter(institute=institute)

    context = {'student_applications': student_applications}
    return render(request, 'scholar/institute_dashboard.html')
  
def state_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        try:
            state = StateAuthority.objects.get(user__username=username)
            print(state,"State")
        except Institute.DoesNotExist:
            messages.info(request, "Invalid Username!!")
            return HttpResponseRedirect(reverse('scholar:state_login'))
        
        # Check if the user type is State
        if state.user.user_type != 3: # Assuming 2 is the user_type for StateAuthority
            messages.error(request, 'Invalid user type. Please log in as an State.')
            return HttpResponseRedirect(reverse('scholar:state_login'))
        
        user = authenticate(username=username, password=password)
        print("authenticated")
        if user is not None and user == state.user:
            login(request, user)
            print("logged in")
            return HttpResponseRedirect(reverse('scholar:state_dashboard'))
        else:
            messages.error(request, 'Invalid credentials.')
            return HttpResponseRedirect(reverse('scholar:state_login'))

    return render(request, 'scholar/state_login.html')
    
def state_dashboard(request):
    return render(request,'scholar/state_dashboard.html')
    
    
def state_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('scholar:state_login'))

def view_details(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    docs = Docs.objects.get(student=student)
    
    context = {'student': student, 'docs': docs}
    return render(request, 'view_details.html', context)

@group_required('Student')
def Scholar_application(request):
    if request.method == "POST":
        
        data = request.POST
        print(data)
        # applicant_photo = request.FILES.get('applicant_photo')
        # domicile_certificate = request.FILES.get('applicant_photo')
        # income_certficate = request.FILES.get('income_certficate')
        # caste_certificate = request.FILES.get('caste_certificate')
        # aadhar_card = request.FILES.get('aadhar_card')
        # bonafide = request.FILES.get('bonafide')
        # fee_receipt = request.FILES.get('fee_receipt')
        # passbook = request.FILES.get('passbook')
        
        institute_state = data.get('institute_state')
        
        
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
        
        current_student = Student.objects.filter(user=request.user)
        
        # student = Student.objects.create(
        print('checked')
        current_student.applicant_name = applicant_name,
        current_student.father_name = father_name,
        current_student.mother_name = mother_name,
        current_student.gender = gender,
        current_student.annual_income = annual_income,
        current_student.category = category,
        current_student.religion = religion,
        current_student.course = course,
        current_student.enrollment = enrollment,
        current_student.adm_year = adm_year,
        current_student.pr_year = pr_year,
        current_student.mode = mode,
        current_student.pre_board = pre_board,
        current_student.prev_class = prev_class,
        current_student.pass_year = pass_year,
        current_student.disabled = disabled,
        current_student.parents_profession = parents_profession,
        current_student.acc_no = acc_no,
        current_student.ifsc = ifsc,
        
        
        # current_student.applicant_photo = applicant_photo,
        # current_student.domicile_certificate = domicile_certificate,
        # current_student.income_certficate = income_certficate,
        # current_student.caste_certificate = caste_certificate,
        # current_student.aadhar_card = aadhar_card,
        # current_student.bonafide = bonafide,
        # current_student.fee_receipt = fee_receipt,
        # current_student.passbook = passbook,
        
        current_student.save()
        print('saved')
        return HttpResponseRedirect(reverse('scholar:Scholar_application2'))

    return render(request,'scholar/scholar_application.html')



def Scholar_application2(request):
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

        student_files = Docs.objects.create(
            student = request.user.student,
            applicant_photo = applicant_photo,
            domicile_certificate = domicile_certificate,
            income_certficate = income_certficate,
            caste_certificate = caste_certificate,
            aadhar_card = aadhar_card,
            bonafide = bonafide,
            fee_receipt = fee_receipt,
            passbook = passbook,
        )
        student_files.save()
        return HttpResponseRedirect(reverse('scholar:student_dashboard'))
        
    return render(request,'scholar/scholar_application2.html')

#aise hoga ye wrna create se to nya student ka bn jaega The view scholar.views.Scholar_application didn't return an HttpResponse object. It returned None instead.The view scholar.views.Scholar_application didn't return an HttpResponse object. It returned None instead.
# ok  student login and scholar_application ko integrate kar diya hu css k saath base.html use kiya hu
#ok great
#ok
#wse session chat khol lo  baad meh comment ko hataa denge
#