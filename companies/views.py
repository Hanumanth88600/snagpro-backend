from rest_framework import generics
from .models import CompanyRequest
from .serializers import CompanyRequestSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

from .models import CompanyRequest, Company

User = get_user_model()


class CompanyRequestCreateView(generics.CreateAPIView):

    queryset = CompanyRequest.objects.all()

    serializer_class = CompanyRequestSerializer
    
    
    
class ApproveCompanyView(APIView):

    def post(self, request, pk):

        company_request = CompanyRequest.objects.get(pk=pk)

        if company_request.status != "PENDING":

            return Response({
                "message": "Already processed"
            })

        company = Company.objects.create(
            name=company_request.company_name,
            email=company_request.email,
            phone=company_request.phone,
            address=company_request.address
        )

        temp_password = get_random_string(10)

        username = company_request.email.split("@")[0]

        user = User.objects.create_user(
            username=username,
            email=company_request.email,
            password=temp_password,
            role="COMPANY_ADMIN",
            company=company
        )

        company_request.status = "APPROVED"
        company_request.save()

        return Response({
            "message": "Company Approved",
            "username": username,
            "password": temp_password
        })