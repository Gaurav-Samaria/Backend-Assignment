from rest_framework.response import Response
from rest_framework.decorators import api_view
from Shrink_App.models import Record
from .serializers import RecordSerializer
from django_q.tasks import async_task


@api_view(['GET'])
def getData(request):
    records = Record.objects.all()
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def addData(request):
    serializer = RecordSerializer(data=request.data)
    if serializer.is_valid():
        # initially saving the record
        serializer.save()

        # adding the resizing task to queue
        async_task("api.services.image_size_reducer", serializer.data['id'], hook="api.services.hook_size_reducer")
    return Response(serializer.data)