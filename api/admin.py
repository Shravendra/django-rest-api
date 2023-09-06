from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'email_id', 'strength', 'website')
    search_fields = ('company_name', 'company_code')

