from rest_framework.response import Response
from rest_framework.decorators import api_view
from Shrink_App.models import Record
from .serializers import RecordSerializer


@api_view(['GET'])
def getData(request):
    records = Record.objects.all()
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)
    