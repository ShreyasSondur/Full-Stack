from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class faculty(models.Model):
    Name = models.CharField(max_length = 150)
    Designation = models.CharField(max_length = 150)
    About = models.TextField(null=False,blank=False)
    Qualification = models.CharField(max_length = 150)
    Email = models.CharField(max_length = 150)
    Phone = models.IntegerField()
    
    def __str__(self):
        return self.Name
    

class departhment(models.Model):
    Name = models.CharField(max_length = 150)
    HOD = models.CharField(max_length = 150)
    About = models.TextField(null=False,blank=False)
    staff = models.CharField(max_length = 150)

    def __str__(self):
        return self.Name