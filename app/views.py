from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

#convert to json type 
import json

#see listed events
from django.db.models import F

from django.views.decorators.csrf import csrf_exempt


'''


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    grade = models.IntegerField()
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
'''


from .models import Student 
# Create your views here.
@csrf_exempt
def student(request):
  if request.method == 'GET':
    stud_list = list(Student.objects.all().order_by('-id'))
    print(stud_list)
    return HttpResponse(stud_list)

    '''
    from django.http import JsonResponse

    return JsonResponse(['a', 'b'], safe=False)
    '''