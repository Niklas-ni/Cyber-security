from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blacklist(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    people = models.TextField(max_length=100)
    dept = models.IntegerField(default=0)

    def __str__(self):
        dept = str(self.dept)
        return self.people + ' To Pay ' + dept
    
    

    

