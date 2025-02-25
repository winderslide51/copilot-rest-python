from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import datetime
import json
from pathlib import Path
from django.conf import settings
from django.shortcuts import render

@api_view(['GET'])
def get_current_time(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return JsonResponse({'time': current_time}, status=status.HTTP_200_OK)

# Create a new function GET hello?key=World
# that returns a JSON {"message": "Hello World"} when the query parameter key is present
# and return HTTP 500 code with message "key query parameter is required"
# when the query parameter key is not present
@api_view(['GET'])
def get_hello(request):
    key = request.query_params.get('key', None)
    if key:
        return JsonResponse({'message': f'Hello {key}'}, status=status.HTTP_200_OK)
    return JsonResponse({'message': 'key query parameter is required'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_pierre(request):
    try:
        json_path = Path(settings.BASE_DIR) / 'data' / 'vms.json'
        with open(json_path, 'r') as file:
            vms_data = json.load(file)
        return JsonResponse(vms_data, safe=False, status=status.HTTP_200_OK)
    except FileNotFoundError:
        return JsonResponse(
            {'error': 'VM data file not found' + str(json_path)}, 
            status=status.HTTP_404_NOT_FOUND
        )
    except json.JSONDecodeError:
        return JsonResponse(
            {'error': 'Invalid JSON data'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

def home(request):
    return render(request, 'api/home.html')