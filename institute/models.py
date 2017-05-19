from django.db import models

from district.models import District

# Create your models here.


class Institute(models.Model):
    inst_id = models.IntegerField(primary_key = True)
    inst_name = models.CharField(max_length = 100, unique = True)
    dist_id = models.ForeignKey(District)

    def __str__(self):
        return  self.inst_id + ". " + self.inst_name