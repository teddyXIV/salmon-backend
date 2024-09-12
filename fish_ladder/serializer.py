from rest_framework import serializers
from . models import *

class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishCount
        fields = ['date', 'count', 'dam']