from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)

from .models import Inspection

from .serializers import (
    InspectionSerializer,
    SnagSerializer,
    SnagImageSerializer
)

from accounts.permissions import (
    IsSiteEngineer,
    IsCompanyAdmin,
    IsCompanyAdminOrEngineer
)

from .models import (
    Inspection,
    Snag,
    SnagImage
)

from .serializers import (
    InspectionSerializer,
    SnagSerializer
)

from accounts.models import User

from accounts.permissions import IsCompanyAdmin
from rest_framework.permissions import IsAuthenticated

class CreateInspectionView(
    APIView
):

    permission_classes = [
    IsCompanyAdminOrEngineer
]

    def post(self, request):

        data = request.data.copy()

        data["engineer"] = (
            request.user.id
        )

        serializer = (
            InspectionSerializer(
                data=data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
        )
        
        
class InspectionListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        inspections = Inspection.objects.all()

        serializer = InspectionSerializer(
            inspections,
            many=True
        )

        return Response(
            serializer.data
        )      
        
class InspectionDetailView(APIView):

    permission_classes = [
    IsCompanyAdminOrEngineer
]

    def put(
        self,
        request,
        pk
    ):

        inspection = Inspection.objects.get(
            id=pk
        )

        serializer = InspectionSerializer(
            inspection,
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
        )

    def delete(
        self,
        request,
        pk
    ):

        inspection = Inspection.objects.get(
            id=pk
        )

        inspection.delete()

        return Response({
            "message":
            "Inspection Deleted"
        })          
        
class CreateSnagView(APIView):

    permission_classes = [
    IsCompanyAdminOrEngineer
]

    def post(self, request):

        serializer = SnagSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        snag = serializer.save()

        print(
            "FILES:",
            request.FILES
        )

        images = request.FILES.getlist(
            "images"
        )

        print(
            "IMAGE COUNT:",
            len(images)
        )

        for image in images:

            SnagImage.objects.create(
                snag=snag,
                image=image
            )

        serializer = SnagSerializer(
            snag
        )

        return Response(
            serializer.data
        )
        
class SnagListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        snags = Snag.objects.all()

        serializer = SnagSerializer(
            snags,
            many=True
        )

        return Response(
            serializer.data
        )        
        
class AssignContractorView(APIView):

    permission_classes = [
        IsCompanyAdmin
    ]

    def post(self, request, snag_id):

        snag = Snag.objects.get(
            id=snag_id
        )

        contractor_id = request.data.get(
            "contractor_id"
        )

        contractor = User.objects.get(
            id=contractor_id
        )

        if contractor.role != "CONTRACTOR":

            return Response({
                "error":
                "User is not a contractor"
            })

        snag.contractor = contractor

        snag.save()

        return Response({
            "message":
            "Contractor Assigned"
        })
        
class ContractorSnagListView(
    APIView
):
    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        snags = Snag.objects.filter(
            contractor=request.user
        )

        data = []

        for snag in snags:

            data.append({

                "id": snag.id,

                "title":
                    snag.title,

                "priority":
                    snag.priority,

                "status":
                    snag.status

            })

        return Response(data)
    
    
class SnagDetailView(APIView):

    permission_classes = [
    IsCompanyAdminOrEngineer
]
    def put(
        self,
        request,
        pk
    ):

        snag = Snag.objects.get(
            id=pk
        )

        serializer = SnagSerializer(
            snag,
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
        )

    def delete(
        self,
        request,
        pk
    ):

        snag = Snag.objects.get(
            id=pk
        )

        snag.delete()

        return Response({
            "message":
            "Snag Deleted"
        })
        
class UpdateSnagStatusView(APIView):

    def put(
        self,
        request,
        snag_id
    ):

        snag = Snag.objects.get(
            id=snag_id,
            contractor=request.user
        )

        snag.status = request.data.get(
            "status"
        )

        snag.save()

        return Response({
            "message":
            "Status Updated"
        })
        
class ClientInspectionListView(
    APIView
):

    permission_classes = [
        IsAuthenticated
        
    ]

    def get(
        self,
        request
    ):

        inspections = Inspection.objects.filter(
            project__client=request.user
        )

        serializer = InspectionSerializer(
            inspections,
            many=True
        )

        return Response(
            serializer.data
        )
        
class ClientSnagListView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        snags = Snag.objects.filter(
            inspection__project__client=
            request.user
        )

        serializer = SnagSerializer(
            snags,
            many=True
        )

        return Response(
            serializer.data
        )