from django.db import models
from district.models import District
from institute.models import Institute
# Create your models here.


class Student(models.Model):
    stu_id = models.IntegerField(primary_key = True)
    stu_name = models.CharField(max_length = 100, unique = True)
    dist_id = models.ForeignKey(District)
    inst_id = models.ForeignKey(Institute)
    stu_phone = models.CharField(max_length = 15, unique = True)
    stu_admission = models.DateField()

    def __str__(self):
        return self.stu_id + ". " + self.stu_name
