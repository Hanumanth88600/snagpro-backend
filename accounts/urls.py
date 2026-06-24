from django.urls import path

from .views import (
    LoginView,
    CreateStaffView,
    StaffListView,
    StaffDetailView,
    ClientListView,
)

from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from .views import ProfileView, UpdateProfileView, ChangePasswordView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("create-staff/", CreateStaffView.as_view()),
    path("staff/", StaffListView.as_view()),
    path("staff/<int:pk>/", StaffDetailView.as_view()),
    path("clients/", ClientListView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("profile/update/", UpdateProfileView.as_view()),
    path("change-password/", ChangePasswordView.as_view()),
    path(
        "token/refresh/",
        TokenRefreshView.as_view()
    ),

]
