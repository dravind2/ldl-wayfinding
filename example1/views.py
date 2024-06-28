from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
import logging
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class HelloWorld(APIView):
    @csrf_exempt
    def post(self, _):
        return JsonResponse({'message' : 'Hello, success!'}, status=200)