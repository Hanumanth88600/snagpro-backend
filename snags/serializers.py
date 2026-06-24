from rest_framework import serializers

from .models import (
    Inspection,
    Snag,
    SnagImage
)


class InspectionSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Inspection

        fields = "__all__"


class SnagImageSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = SnagImage

        fields = "__all__"


class SnagSerializer(
    serializers.ModelSerializer
):

    contractor_name = serializers.SerializerMethodField()

    images = SnagImageSerializer(
            many=True,
            read_only=True
        )

    class Meta:

        model = Snag

        fields = "__all__"

    def get_contractor_name(
        self,
        obj
    ):
        return (
            obj.contractor.username
            if obj.contractor
            else None
        )