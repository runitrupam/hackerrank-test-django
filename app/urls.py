from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',views.get_all_or_post,name='get_all_or_post'), # get or add a student
    path('students/<int:id>',views.get_or_update,name='get_or_update'), # UPDATE a student or get
]