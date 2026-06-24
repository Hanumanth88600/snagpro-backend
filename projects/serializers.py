from rest_framework import serializers

from .models import (
    Project,
    ProjectAssignment
)

from accounts.models import User


class ProjectSerializer(
    serializers.ModelSerializer
):

    client_name = serializers.CharField(
            source="client.username",
            read_only=True
        )

    class Meta:

        model = Project

        fields = "__all__"


class ProjectAssignmentSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = ProjectAssignment

        fields = "__all__"