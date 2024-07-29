from rest_framework import serializers

from counter.models import MarketingCounter


class MarketingCounterSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = MarketingCounter
        fields = '__all__'

