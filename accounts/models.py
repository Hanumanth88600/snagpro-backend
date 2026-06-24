from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company


class User(AbstractUser):

    ROLE_CHOICES = (
        ("SUPER_ADMIN", "SUPER_ADMIN"),
        ("COMPANY_ADMIN", "COMPANY_ADMIN"),
        ("SITE_ENGINEER", "SITE_ENGINEER"),
        ("CONTRACTOR", "CONTRACTOR"),
        ("CLIENT", "CLIENT"),
    )

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default="CLIENT"
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    must_change_password = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True 
    )
    
    plain_password = models.CharField(
    max_length=255,
    blank=True,
    null=True
)

    def __str__(self):
        return self.username