from rest_framework.decorators import api_view
from rest_framework.response import Response

from .docs import ProfileDocType
from .models import Activation
from .serializers import ActivationSerializer, ProfileSerializer

@api_view(['GET'])
def activation_list(request):
    activations = Activation.objects.all()
    serializer = ActivationSerializer(activations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def submissions_list(request):
    submissionsData = ProfileDocType.search().execute()
    submissionsDataSerializer = ProfileSerializer(submissionsData, many=True)
    return Response(
        {"Total sumbmissions completed": len(submissionsDataSerializer.data)}
    )

@api_view(['GET'])
def brand_list(request):
    brandData = ProfileDocType.search().filter("exists", field="brand_ids").execute()
    brandDataSerializer = ProfileSerializer(brandData, many=True)
    return Response(
        {"Total submissions with brand data": len(brandDataSerializer.data)}
    )

@api_view(['GET'])
def profile_list(request):
    profiles = ProfileDocType.search().execute()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)
