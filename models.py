from django.db import models

class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    year = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name     
