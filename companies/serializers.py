from rest_framework import serializers
from .models import CompanyRequest


class CompanyRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyRequest
        fields = "__all__"