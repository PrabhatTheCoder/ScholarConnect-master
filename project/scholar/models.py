
from django.db import models
from users.models import Student,Institute, StateAuthority

class Docs(models.Model):
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='attached_docs')
    applicant_photo = models.ImageField(upload_to="user_detail/")
    domicile_certificate = models.ImageField(upload_to="user_detail/")
    income_certficate = models.ImageField(upload_to="user_detail/")
    caste_certificate = models.ImageField(upload_to="user_detail/")
    aadhar_card = models.ImageField(upload_to="user_detail/")
    bonafide = models.ImageField(upload_to="user_detail/")
    fee_receipt = models.ImageField(upload_to="user_detail/")
    passbook = models.ImageField(upload_to="user_detail/")


class ApplicationStatus(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True, blank=True)
    state_authority = models.ForeignKey(StateAuthority, on_delete=models.CASCADE, null=True, blank=True)
    
    # Add fields to track the status at each level
    institute_approval = models.BooleanField(default=False)
    state_approval = models.BooleanField(default=False)
    final_approval = models.BooleanField(default=False)
    
    # Additional fields for comments, timestamps, etc., can be added based on requirements
    
    def __str__(self):
        return f"Application Status for {self.student}"
