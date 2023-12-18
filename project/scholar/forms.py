from django import forms

from scholar.models import Docs
from django import forms


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
