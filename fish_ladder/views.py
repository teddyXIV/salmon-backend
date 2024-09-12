from django.shortcuts import render
from rest_framework.views import APIView
from . models import * 
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from datetime import datetime
from . serializer import *
from django.db import models

class SalmonSimView(APIView):

    serializer_class = CountSerializer

    def get(self, request):
        start_date_str = request.GET.get('startDate')
        end_date_str = request.GET.get('endDate')

        if not start_date_str or not end_date_str:
            raise NotFound("A start and end date are required.")
        
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        
        salmon_counts = FishCount.objects.filter(date__range=(start_date, end_date))

        if not salmon_counts:
            raise NotFound(f"There are no salmon counts from {start_date_str} to {end_date_str}.")

        serializer = CountSerializer(salmon_counts, many=True)
        serialized_data = serializer.data

        return Response(serialized_data)

# Create your views here.
