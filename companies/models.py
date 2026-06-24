from django.db import models


class CompanyRequest(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    )

    company_name = models.CharField(max_length=255)

    owner_name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    address = models.TextField()

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
    
    
class Company(models.Model):

    name = models.CharField(max_length=255)

    company_code = models.CharField(
    max_length=50,
    unique=True,
    null=True,
    blank=True
)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    address = models.TextField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name