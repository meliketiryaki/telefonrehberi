from django.contrib import admin
from .models import Kisi,Sirket,GelenArama


class RehberAdmin(admin.ModelAdmin):
    search_fields=("adsoyad","isim",)
    



admin.site.register(Kisi,RehberAdmin)
admin.site.register(Sirket,RehberAdmin)
