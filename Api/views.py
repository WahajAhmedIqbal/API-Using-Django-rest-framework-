from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import employe
from .serializers import employeSerializer

class emplyeList(APIView):
    
    def get(self , request):
        employ1 = employe.objects.all()
        seri = employeSerializer(employ1, many=True)
        return Response(seri.data)
    
    