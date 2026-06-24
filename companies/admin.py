from django.contrib import admin
from .models import CompanyRequest
from .models import Company


@admin.register(CompanyRequest)
class CompanyRequestAdmin(admin.ModelAdmin):

    list_display = (
        "company_name",
        "owner_name",
        "email",
        "status",
        "created_at"
    )

    list_filter = ("status",)
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "is_active"
    )