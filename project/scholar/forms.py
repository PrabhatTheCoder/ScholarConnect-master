from django import forms

from scholar.models import Docs
from django import forms
from users.models import Institute, Student
       
# class InstituteForm(forms.ModelForm):
#     class Meta:
#         model = Institute
#         fields = ['username', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }
#         labels = {
#             'username': 'Username',
#             'password': 'Password',
#         }
#         required = {
#             'username': True,
#             'password': True,
#         }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     password2 = cleaned_data.get("password2")
    #     if password != password2:
    #         raise forms.ValidationError(
    #             "Passwords do not match"
    #         )
        
class UserDocsForm(forms.ModelForm):
    class Meta:
        model = Docs
        fields = [
            'applicant_photo',
            'domicile_certificate',
            'income_certficate',
            'caste_certificate',
            'aadhar_card',
            'bonafide',
            'fee_receipt',
            'passbook',
        ]
        labels = {
            'applicant_photo': 'Applicant Photo',
            'domicile_certificate': 'Domicile Certificate',
            'income_certficate': 'Income Certificate',
            'caste_certificate': 'Caste Certificate',
            'aadhar_card': 'Aadhar Card',
            'bonafide': 'Bonafide',
            'fee_receipt': 'Fee Receipt',
            'passbook': 'Passbook',
        }
        
        required = {
            'applicant_photo': True,
            'domicile_certificate': True,
            'income_certificate': True,
            'caste_certificate' : True,
            'aadhar_card': True,
            'bonafide': True,
            'fee_receipt': True,
            'passbook': True,
            
        }
        
        