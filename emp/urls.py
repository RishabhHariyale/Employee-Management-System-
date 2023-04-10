from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.index, name='index'),
    path('all_emp' , views.all_emp, name='all_emp'),
    path('add_emp' , views.add_emp, name='add_emp'),
    path("del_emp" , views.del_emp, name='del_emp'),
    path("del_emp/<int:emp_id>" , views.del_emp, name='del_emp'),
    path("update_emp/<int:emp_id>" , views.update_emp, name='update_emp'),
    path("doUpdate_emp/<int:emp_id>" , views.doUpdate_emp, name='doUpdate_emp'),
    path('filter_emp' , views.filter_emp, name='filter_emp'),
    path('accounts/' , include('accounts.urls')),

    
]