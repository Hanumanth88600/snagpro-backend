from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.permissions import (
    IsCompanyAdmin
)

from .models import Project
from .serializers import (
    ProjectSerializer
)


from .models import (
    Project,
    ProjectAssignment
)
from snags.models import Inspection, Snag
from .serializers import (
    ProjectSerializer,
    ProjectAssignmentSerializer
)
from rest_framework.permissions import IsAuthenticated


class CreateProjectView(APIView):

    permission_classes = [
        IsCompanyAdmin
    ]

    def post(self, request):

        print("REQUEST DATA =", request.data)

        data = request.data.copy()

        data["company"] = (
            request.user.company.id
        )

        serializer = ProjectSerializer(
            data=data
        )

        serializer.is_valid(
            raise_exception=True
        )

        project = serializer.save()

        print(
            "CLIENT SAVED =",
            project.client
        )

        return Response(
            ProjectSerializer(
                project
            ).data
        )
        
class ProjectListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        projects = Project.objects.filter(
            company=request.user.company
        )

        serializer = ProjectSerializer(
            projects,
            many=True
        )

        return Response(
            serializer.data
        )        
        

class AssignProjectView(APIView):

    permission_classes = [
        IsCompanyAdmin
    ]

    def post(self, request):

        project_id = request.data.get(
            "project"
        )

        user_id = request.data.get(
            "user"
        )

        assignment_type = request.data.get(
            "assignment_type"
        )

        assignment, created = (
            ProjectAssignment.objects.get_or_create(
                project_id=project_id,
                user_id=user_id,
                assignment_type=assignment_type
            )
        )

        return Response({
            "created": created,
            "id": assignment.id
        })
        
class ProjectDetailView(APIView):

    permission_classes = [
        IsCompanyAdmin
    ]

    def put(
    self,
    request,
    pk
):

        project = Project.objects.get(
            id=pk,
            company=request.user.company
        )

        project.project_name = request.data.get(
            "project_name",
            project.project_name
        )

        project.project_code = request.data.get(
            "project_code",
            project.project_code
        )

        project.location = request.data.get(
            "location",
            project.location
        )

        project.description = request.data.get(
            "description",
            project.description
        )

        project.start_date = request.data.get(
            "start_date",
            project.start_date
        )

        project.end_date = request.data.get(
            "end_date",
            project.end_date
        )

        project.status = request.data.get(
            "status",
            project.status
        )

        project.save()

        return Response({
            "message":
            "Project Updated"
        })

    def delete(
        self,
        request,
        pk
    ):

        project = Project.objects.get(
            id=pk,
            company=request.user.company
        )

        project.delete()

        return Response({
            "message":
            "Project Deleted"
        })
        
class ProjectAssignmentListView(APIView):

    permission_classes = [
        IsCompanyAdmin
    ]

    def get(self, request):

        assignments = (
            ProjectAssignment.objects
            .select_related(
                "user",
                "project"
            )
        )

        data = []

        for item in assignments:

            data.append({

                "id": item.id,

                "project_id":
                    item.project.id,

                "project_name":
                    item.project.project_name,

                "user_id":
                    item.user.id,

                "user_name":
                    item.user.first_name,

                "role":
                    item.assignment_type

            })

        return Response(data)  
    

class ProjectAssignmentDetailView(APIView):

    permission_classes = [
        IsCompanyAdmin
    ]

    def delete(
        self,
        request,
        pk
    ):

        assignment = (
            ProjectAssignment.objects.get(
                id=pk
            )
        )

        assignment.delete()

        return Response({
            "message":
            "Assignment Removed"
        })
        
class ClientProjectListView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        projects = Project.objects.filter(
            client=request.user
        )

        serializer = ProjectSerializer(
            projects,
            many=True
        )

        return Response(
            serializer.data
        )
        
class ClientProjectDetailsView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        projects = Project.objects.filter(
            client=request.user
        )

        data = []

        for project in projects:

            assignments = (
                ProjectAssignment.objects.filter(
                    project=project
                )
            )

            engineers = []
            contractors = []

            for item in assignments:

                if item.assignment_type == "ENGINEER":

                    engineers.append(
                        item.user.username
                    )

                elif item.assignment_type == "CONTRACTOR":

                    contractors.append(
                        item.user.username
                    )

            inspection_count = (
                Inspection.objects.filter(
                    project=project
                ).count()
            )

            snag_queryset = (
                Snag.objects.filter(
                    inspection__project=project
                )
            )

            snag_count = snag_queryset.count()

            snag_list = []

            for snag in snag_queryset:

                snag_list.append({

                    "title": snag.title,

                    "status": snag.status,

                    "priority": snag.priority

                })

            data.append({

                "id": project.id,

                "project_name": project.project_name,

                "project_code": project.project_code,

                "location": project.location,

                "status": project.status,

                "engineers": engineers,

                "contractors": contractors,

                "inspection_count": inspection_count,

                "snag_count": snag_count,

                "snags": snag_list

            })

        return Response(data)