from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
# Create your views here.


USER_FULL_NAME = "Mudasir_Mushtaq"
DOB = "06022003"
EMAIL = "mudasirmmattoo@gmail.com"
ROLL_NUMBER = "21BCI0128"


def home(request):
    return render(request, 'api/index.html')
# GET method view
def get_operation_code(request):
    return JsonResponse({"operation_code": 1}, status=200)

# POST method view
@csrf_exempt
def process_data(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            data = body.get('data', [])

            # Separate numbers and alphabets
            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]

            # Find the highest lowercase alphabet
            lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
            highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

            response = {
                "is_success": True,
                "user_id": "john_doe_17091999",
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
            }

        except Exception as e:
            response = {
                "is_success": False,
                "message": str(e)
            }

        return JsonResponse(response, status=200)

    elif request.method == 'GET':
        return JsonResponse({"operation_code": 1}, status=200)

    else:
        return JsonResponse({"is_success": False, "message": "Invalid request method"}, status=400)
