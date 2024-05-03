
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class course(models.Model):
    course_name = models.CharField(max_length=200)

class teacher(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    course_fk =  models.ForeignKey(course, on_delete=models.CASCADE, null=True)
    number = models.IntegerField()
    image = models.ImageField(upload_to='image/', null=True) 
    join_date = models.DateField(auto_now_add=True)

