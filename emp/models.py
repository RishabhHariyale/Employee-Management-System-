from django.db import models

# Create your models here.


class Employee1(models.Model):
    emp_first_name = models.CharField(max_length = 200 , null = False )
    emp_last_name = models.CharField(max_length = 200 ,null = False )
    emp_age = models.IntegerField(max_length = 3)
    emp_department = models.CharField(max_length = 100 , null = False)
    emp_salary = models.IntegerField(max_length = 10 , default = 0)
    emp_bonus = models.IntegerField(max_length = 10 ,default = 0)
    emp_role = models.CharField(max_length = 100 , null = False)
    emp_phone = models.IntegerField(max_length = 10 , default = 0)
    emp_address = models.CharField(max_length = 200 ,null = False)
    emp_working = models.BooleanField(default= True)

    def __str__(self) :
        return " %s %s " %(self.emp_first_name  , self.emp_last_name)


    
