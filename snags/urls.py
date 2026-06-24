from django.urls import path


from .views import (
    CreateInspectionView,
    CreateSnagView,
    AssignContractorView,
    ContractorSnagListView,
    InspectionListView,
    InspectionDetailView,
    SnagListView,
    SnagDetailView,
    UpdateSnagStatusView,
    ClientInspectionListView,
    ClientSnagListView
)

urlpatterns = [

    path(
        "inspection/create/",
        CreateInspectionView.as_view()
    ),
    
    path(
    "create/",
    CreateSnagView.as_view()
),
    
    path(
    "assign/<int:snag_id>/",
    AssignContractorView.as_view()
),
    
    path(
    "contractor/snags/",
    ContractorSnagListView.as_view()
),
    
    path(
    "inspections/",
    InspectionListView.as_view()
),

path(
    "inspections/<int:pk>/",
    InspectionDetailView.as_view()
),

path(
    "list/",
    SnagListView.as_view()
),
path(
    "<int:pk>/",
    SnagDetailView.as_view()
),
path(
    "contractor/update/<int:snag_id>/",
    UpdateSnagStatusView.as_view()
),

path(
    "client/inspections/",
    ClientInspectionListView.as_view()
),

path(
    "client/snags/",
    ClientSnagListView.as_view()
),
]