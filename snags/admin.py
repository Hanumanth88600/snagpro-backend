from django.contrib import admin
from .models import Inspection, Snag


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):

    list_display = (
        "inspection_number",
        "project",
        "engineer",
        "inspection_date"
    )


@admin.register(Snag)
class SnagAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "priority",
        "status",
        "contractor"
    )