from django.urls import path
from .views import CompanyRequestCreateView
from .views import ApproveCompanyView

urlpatterns = [
    path(
        "request-company/",
        CompanyRequestCreateView.as_view()
    ),
    
    path(
    "approve/<int:pk>/",
    ApproveCompanyView.as_view()
),
]