from __future__ import unicode_literals

from django.db import models
import json


# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    package = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    origin = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50)
    level = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    def get_fields(self):
        return ("name", "price", "package", "unit", "origin", "barcode", "level")


class GoodLogs(models.Model):
    goods = models.ForeignKey(Goods)
    # goods_id = models.IntegerField(default=0)
    item = models.CharField(max_length=50)
    before = models.CharField(max_length=200)
    after = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    operator = models.CharField(max_length=200)

    def __unicode__(self):
        return self.item

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class Esls(models.Model):
    goods = models.ForeignKey(Goods)
    label_num = models.CharField(max_length=20)
    # goods_id = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    label_type = models.CharField(max_length=20)
    update_time = models.CharField(max_length=50)

    def __unicode__(self):
        return self.label_num

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class ChangeList(models.Model):
    esl = models.ForeignKey(Esls)
    # label_id = models.IntegerField(default=0)
    indate = models.CharField(max_length=50)

    def __unicode__(self):
        return self.label_id

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class TaskLogs(models.Model):
    change_item = models.ForeignKey(ChangeList)
    # change_list_id = models.IntegerField(default=0)
    result = models.CharField(max_length=20)
    notes = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.change_list_id

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
