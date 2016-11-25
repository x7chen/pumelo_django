from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    package = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    origin = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50)
    level = models.CharField(max_length=20)


class GoodLogs(models.Model):
    good_id = models.IntegerField(default=0)
    item = models.CharField(max_length=50)
    before = models.CharField(max_length=200)
    after = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    operator = models.CharField(max_length=200)
