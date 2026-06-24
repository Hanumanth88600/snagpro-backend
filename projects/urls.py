from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    CreateProjectView,
    AssignProjectView,
    ProjectListView,
    ProjectDetailView,
    ProjectAssignmentDetailView,
    ClientProjectListView,
    ClientProjectDetailsView
)
from .views import (
    ProjectAssignmentListView
)

urlpatterns = [

    path(
        "create/",
        CreateProjectView.as_view()
    ),

    path(
        "",
        ProjectListView.as_view()
    ),

    path(
        "<int:pk>/",
        ProjectDetailView.as_view()
    ),

    path(
        "assign/",
        AssignProjectView.as_view()
    ),
    path(
    "assignments/",
    ProjectAssignmentListView.as_view()
),
    path(
    "assignments/<int:pk>/",
    ProjectAssignmentDetailView.as_view()
),
    path(
    "client/projects/",
    ClientProjectListView.as_view()
),
    path(
    "client/details/",
    ClientProjectDetailsView.as_view()
),
    
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)