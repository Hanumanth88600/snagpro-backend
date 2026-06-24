from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    ProfileSerializer
)
from .serializers import LoginSerializer
from .models import User
from .utils import (
    generate_username,
    generate_password
)

from .serializers import (
    StaffCreateSerializer
)
from rest_framework.permissions import (
    IsAuthenticated
)

from accounts.permissions import (
    IsCompanyAdminOrEngineer
)
from .permissions import IsCompanyAdmin

class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        return Response({

            "access": str(refresh.access_token),

            "refresh": str(refresh),

            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "company_id": (
                    user.company.id
                    if user.company
                    else None
                ),
                "must_change_password":
                    user.must_change_password
            }

        }, status=status.HTTP_200_OK)
        
class CreateStaffView(APIView):

    permission_classes = [IsCompanyAdmin]

    def post(self, request):

        print("====== CREATE STAFF ======")
        print("USER:", request.user)
        print("ROLE:", request.user.role)
        print("DATA:", request.data)

        serializer = (
            StaffCreateSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        username = generate_username(
            request.data["first_name"]
        )

        password = generate_password()

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=request.data["first_name"],
            email=request.data["email"],
            phone=request.data["phone"],
            role=request.data["role"],
            company=request.user.company
        )

        user.plain_password = password
        user.save()

        return Response({

            "message":
                "User Created",

            "username":
                username,

            "password":
                password,

            "role":
                user.role

        })
        

class StaffListView(APIView):

    permission_classes = [
         IsCompanyAdminOrEngineer
    ]

    def get(self, request):

        users = User.objects.filter(
            company=request.user.company
        ).exclude(
            role="COMPANY_ADMIN"
        )

        data = []

        for user in users:

            data.append({
                "id": user.id,
                "name": user.first_name,
                "email": user.email,
                "role": user.role,
                "phone": user.phone,
                "username": user.username,
                "password": user.plain_password
            })

        return Response(data)
    
class StaffDetailView(APIView):

    permission_classes = [
        IsCompanyAdmin
    ]

    def delete(
        self,
        request,
        pk
    ):

        user = User.objects.get(
            id=pk,
            company=request.user.company
        )

        user.delete()

        return Response({
            "message":
            "Deleted"
        })
    
    
    def put(
    self,
    request,
    pk
):

        try:

            user = User.objects.get(
                id=pk,
                company=request.user.company
            )

            user.first_name = request.data.get(
                "first_name",
                user.first_name
            )

            user.email = request.data.get(
                "email",
                user.email
            )

            user.phone = request.data.get(
                "phone",
                user.phone
            )

            user.role = request.data.get(
                "role",
                user.role
            )

            user.save()

            return Response({
                "message":
                "Staff Updated"
            })

        except User.DoesNotExist:

            return Response(
                {
                    "message":
                    "User Not Found"
                },
                status=404
            )
            
class ClientListView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        clients = User.objects.filter(
            role="CLIENT",
            company=request.user.company
        )

        data = []

        for client in clients:

            data.append({

                "id":
                client.id,

                "username":
                client.username

            })

        return Response(
            data
        )  
        
class ProfileView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        serializer = (
            ProfileSerializer(
                request.user
            )
        )

        return Response(
            serializer.data
        )


class UpdateProfileView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def put(
        self,
        request
    ):

        serializer = (
            ProfileSerializer(

                request.user,

                data=request.data,

                partial=True

            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
        )


class ChangePasswordView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def put(
        self,
        request
    ):

        old_password =request.data.get(
            "old_password"
        )

        new_password =request.data.get(
            "new_password"
        )

        if not (
            request.user.check_password(
                old_password
            )
        ):

            return Response({

                "error":
                "Current password is incorrect"

            }, status=400)

        request.user.set_password(
            new_password
        )

        request.user.save()

        return Response({

            "message":
            "Password Updated"

        })          