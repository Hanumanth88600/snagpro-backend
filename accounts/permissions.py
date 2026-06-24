from rest_framework.permissions import BasePermission


class IsCompanyAdmin(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role
            == "COMPANY_ADMIN"
        )


class IsSiteEngineer(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role
            == "SITE_ENGINEER"
        )


class IsCompanyAdminOrEngineer(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role in [
                "COMPANY_ADMIN",
                "SITE_ENGINEER"
            ]
        )