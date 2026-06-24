from django.db import models
from companies.models import Company

from accounts.models import User
class Project(models.Model):

    STATUS_CHOICES = (
        ("PLANNING", "PLANNING"),
        ("ACTIVE", "ACTIVE"),
        ("COMPLETED", "COMPLETED"),
        ("ON_HOLD", "ON_HOLD"),
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="projects"
    )
    
    client = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="client_projects"
)

    project_name = models.CharField(
        max_length=255
    )

    project_code = models.CharField(
        max_length=50,
        unique=True
    )

    location = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    start_date = models.DateField()

    end_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PLANNING"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.project_name





class ProjectAssignment(models.Model):

    ASSIGNMENT_CHOICES = (
        ("ENGINEER", "ENGINEER"),
        ("CONTRACTOR", "CONTRACTOR"),
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="assignments"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    assignment_type = models.CharField(
        max_length=20,
        choices=ASSIGNMENT_CHOICES
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.user.username}"
            f" -> "
            f"{self.project.project_name}"
        )