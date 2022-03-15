from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

#convert to json type 
import json

#see listed events
from django.db.models import F

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from datetime import datetime



from .models import Student 
# Create your views here.
@csrf_exempt
def get_all_or_post(request):
  if request.method == 'GET':
    stud_list = list(Student.objects.all().values('id','first_name','last_name','date_of_birth','grade','phone','email').order_by('id'))
    print(stud_list)
    #SomeModel_json = serializers.serialize("json", Student.objects.all())
    return HttpResponse(stud_list,status=200)
  elif request.method == 'POST':

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    date_of_birth = request.POST.get('date_of_birth')
    grade = request.POST.get('grade')
    phone = request.POST.get('phone')
    email = request.POST.get('email')

    stud_ob = Student(first_name = first_name,last_name=last_name, date_of_birth = datetime.now() , grade = grade ,phone = phone,email=email)
    stud_ob.save()
    stud_ob = Student.objects.filter(first_name = first_name,last_name=last_name,grade = grade ,phone = phone,email=email).values('id','first_name','last_name','date_of_birth','grade','phone','email')

    print(stud_ob)
    return HttpResponse(stud_ob,status=201)

@csrf_exempt
def get_or_update(request,id):
  if request.method == 'GET':
    try:
      stud_ob = Student.objects.filter(id = id).values('id','first_name','last_name','date_of_birth','grade','phone','email')
      #print(stud_ob)
      return HttpResponse(stud_ob,status=200)
    except:
      return HttpResponse('',status=404)  

    
  elif request.method == 'POST':
   
    try:

      stud_ob = Student.objects.get(id = id) #.values('id','first_name','last_name','date_of_birth','grade','phone','email')
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      date_of_birth = request.POST.get('date_of_birth')
      grade = request.POST.get('grade')
      phone = request.POST.get('phone')
      email = request.POST.get('email')
      stud_ob.first_name = first_name
      stud_ob.last_name = last_name
      #stud_ob.date_of_birth = date_of_birth
      stud_ob.grade = grade
      stud_ob.phone = phone
      stud_ob.email = email
      stud_ob.save()
      stud_ob = Student.objects.filter(id = id).values('id','first_name','last_name','date_of_birth','grade','phone','email')
      print(stud_ob)
      return HttpResponse(stud_ob,status=200)
    except:
      return HttpResponse('some error',status=404)  
    
