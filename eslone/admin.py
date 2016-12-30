from django.contrib import admin
from models import *
import datetime


# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    list_filter = ['barcode']
    search_fields = ['barcode']
    #   fields = ['name', 'price', 'package', 'origin', 'barcode']
    list_display = ('name', 'price', 'package', 'origin', 'barcode')

    def save_model(self, request, obj, form, change):
        goods_log = GoodLogs()
        if change:
            obj_original = self.model.objects.get(pk=obj.pk)
            goods_log.goods = obj
            goods_log.item = "price"
            goods_log.before = obj_original.price
            goods_log.after = obj.price
            goods_log.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            goods_log.operator = request.user
            goods_log.save()
            super(GoodsAdmin, self).save_model(request, obj, form, change)
        else:
            super(GoodsAdmin, self).save_model(request, obj, form, change)
            goods_log.goods = obj
            goods_log.item = "price"
            goods_log.before = "-"
            goods_log.after = obj.price
            goods_log.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            goods_log.operator = request.user
            goods_log.save()



admin.site.register(Goods, GoodsAdmin)
admin.site.register(Esls)
