from django.db import models

from projects.models import Project

from accounts.models import User


class Inspection(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    engineer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    inspection_number = models.CharField(
        max_length=100,
        unique=True
    )

    location = models.CharField(
        max_length=255
    )

    notes = models.TextField(
        blank=True
    )

    inspection_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.inspection_number


class Snag(models.Model):

    PRIORITY_CHOICES = (
        ("LOW", "LOW"),
        ("MEDIUM", "MEDIUM"),
        ("HIGH", "HIGH"),
        ("CRITICAL", "CRITICAL"),
    )

    STATUS_CHOICES = (
        ("OPEN", "OPEN"),
        ("IN_PROGRESS", "IN_PROGRESS"),
        ("COMPLETED", "COMPLETED"),
        ("VERIFIED", "VERIFIED"),
        ("APPROVED", "APPROVED"),
    )

    inspection = models.ForeignKey(
        Inspection,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN"
    )

    contractor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_snags"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
class SnagImage(models.Model):

    snag = models.ForeignKey(
        Snag,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="snags/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Image {self.id}"