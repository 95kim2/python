from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.Charfield(max_length=100)
    s_major = models.Charfield(max_length=100)
    s_age = models.IntegerField(default = 0)
    s_gender = models.CharField(max_length=30)
    s_attendence = models.IntergerField(default=0)

    def __str__(self):
        return self.s_name