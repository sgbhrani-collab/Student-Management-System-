from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json

@csrf_exempt
def students(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Student.objects.create(**data)
        return JsonResponse({"message": "Saved"})

    if request.method == "GET":
        students = list(Student.objects.values())
        return JsonResponse(students, safe=False)