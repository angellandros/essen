from django.contrib import admin

from .models import Essen, Esser, Abendessen


class EssenAdmin(admin.ModelAdmin):
    fields = ['name', 'category_name', 'price']
    list_display = ['name', 'category_name', 'price']


class EsserAdmin(admin.ModelAdmin):
    fields = ['name', 'alias', 'email', 'bill']
    list_display = ['name', 'alias', 'email', 'bill']


class AbendessenAdmin(admin.ModelAdmin):
    fields = ['person', 'type', 'price', 'date']
    list_display = ['name', 'person', 'type', 'price', 'date']
    list_filter = ['person', 'type', 'date']

    def name(self, obj):
        return str(obj)


admin.site.register(Essen, EssenAdmin)
admin.site.register(Esser, EsserAdmin)
admin.site.register(Abendessen, AbendessenAdmin)
