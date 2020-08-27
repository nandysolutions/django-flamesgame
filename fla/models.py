from django.db import models


# Create your models here.
class Flames(models.Model):
    n1 = models.CharField(max_length=100, default='', blank=False)
    n2 = models.CharField(max_length=100, default='', blank=False)
    res = models.CharField(max_length=40, default='flames', blank=True)

    def __str__(self):
        return str(self.n1) + str(self.n2)
