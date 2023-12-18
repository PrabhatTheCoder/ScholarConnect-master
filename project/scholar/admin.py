from django.contrib import admin
from scholar.models import Docs


class DocsAdmin(admin.ModelAdmin):
    list_display = ['student', 'applicant_photo', 'domicile_certificate', 'income_certficate', 'caste_certificate', 'aadhar_card', 'bonafide', 'fee_receipt', 'passbook']
    search_fields = ['student__user__username']  # Allows searching by student's username

admin.site.register(Docs, DocsAdmin)


