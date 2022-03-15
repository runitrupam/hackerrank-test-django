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
    


    if request.method == 'POST':

        #print(request.POST.get('name'))
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        ''' phone = request.POST['phone']
        if len(phone)<10 or len(phone)>10:
            raise ValidationError("Phone number length is not right")
        query = request.POST['query']
        '''
        #print(name ,  email ,  password  )
        
        u = User.objects.filter(username = name ).first() 
        if u is None :
            user = User.objects.create_user(username=name,
                                 email=email,
                                 password=password , is_staff=True)
        else:
            return HttpResponse(' user already there ')

    return HttpResponse('created a user')
