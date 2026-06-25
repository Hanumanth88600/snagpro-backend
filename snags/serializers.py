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


class SnagImageSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = SnagImage
        fields = ["id", "image", "uploaded_at"]

    def get_image(self, obj):

        request = self.context.get("request")

        if request:
            return request.build_absolute_uri(
                obj.image.url
            )

        return obj.image.url


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