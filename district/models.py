from django.db import models

# Create your models here.


class District(models.Model):
    dist_id = models.IntegerField(primary_key = True)
    dist_name = models.CharField(max_length = 100, unique = True)
    dist_div = models.CharField(max_length = 100)


    def __str__(self):
        return self.dist_id + ". " + self.dist_name

