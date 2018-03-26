from rest_framework import serializers

class ActivationSerializer(serializers.Serializer):
    name = serializers.CharField()

class ProfileSerializer(serializers.Serializer):
    id = serializers.CharField(source='_id',)
    brand_ids = serializers.SerializerMethodField()

    def get_brand_ids(self, obj):
        return list(obj.brand_ids or [])






