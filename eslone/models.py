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
    goods_id = models.IntegerField(default=0)
    item = models.CharField(max_length=50)
    before = models.CharField(max_length=200)
    after = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    operator = models.CharField(max_length=200)


class Esls(models.Model):
    label_num = models.CharField(max_length=20)
    goods_id = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    label_type = models.CharField(max_length=20)
    update_time = models.CharField(max_length=50)


class ChangeList(models.Model):
    label_id = models.IntegerField(default=0)
    indate = models.CharField(max_length=50)


class TaskLogs(models.Model):
    change_list_id = models.IntegerField(default=0)
    result = models.CharField(max_length=20)
    notes = models.CharField(max_length=1000)

