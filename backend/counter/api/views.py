import logging

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from counter.models import MarketingCounter
from counter.api.serializers import MarketingCounterSerializer

logger = logging.getLogger('msb')


@api_view(['GET'])
@permission_classes([IsAdminUser])
def marketing_counter_list(request):
    try:
        marketing_counters = MarketingCounter.objects.all()
        serializer = MarketingCounterSerializer(marketing_counters, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.error(e)
        return Response({"message": "No marketing counters found"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def marketing_counter_create(request):
    try:
        owner = request.user
        request.data['owner'] = owner.id
        serializer = MarketingCounterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Exception as e:
        logger.error(e)
        return Response({"message": "Error creating marketing counter"})
