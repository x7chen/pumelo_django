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
            for field in Goods.get_fields():
                if (field == "name") and (obj_original.name != obj.name):
                    goods_log.item = "name"
                    goods_log.before = obj_original.name
                    goods_log.after = obj.name
                if (field == "price") and (obj_original.price != obj.price):
                    goods_log.item = "price"
                    goods_log.before = obj_original.price
                    goods_log.after = obj.price
                if (field == "package") and (obj_original.package != obj.package):
                    goods_log.item = "package"
                    goods_log.before = obj_original.package
                    goods_log.after = obj.package
                if (field == "unit") and (obj_original.unit != obj.unit):
                    goods_log.item = "unit"
                    goods_log.before = obj_original.unit
                    goods_log.after = obj.unit
                if (field == "origin") and (obj_original.origin != obj.origin):
                    goods_log.item = "origin"
                    goods_log.before = obj_original.origin
                    goods_log.after = obj.origin
                if (field == "barcode") and (obj_original.barcode != obj.barcode):
                    goods_log.item = "barcode"
                    goods_log.before = obj_original.barcode
                    goods_log.after = obj.barcode
                if (field == "level") and (obj_original.level != obj.level):
                    goods_log.item = "level"
                    goods_log.before = obj_original.level
                    goods_log.after = obj.level
                goods_log.goods = obj
                goods_log.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                goods_log.operator = request.user
                goods_log.save()
            super(GoodsAdmin, self).save_model(request, obj, form, change)
        else:
            super(GoodsAdmin, self).save_model(request, obj, form, change)
            goods_log.goods = obj
            goods_log.item = "add"
            goods_log.before = "-"
            goods_log.after = obj.name
            goods_log.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            goods_log.operator = request.user
            goods_log.save()


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Esls)
