from django.contrib import admin
from .models import Project

from .models import (
    Project,
    ProjectAssignment
)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "project_name",
        "project_code",
        "company",
        "status"
    )

@admin.register(ProjectAssignment)
class ProjectAssignmentAdmin(
    admin.ModelAdmin
):

    list_display = (
        "project",
        "user",
        "assignment_type"
    )