from django.db import models
from django.utils.text import slugify

#.../kisiler/melike-tiryaki
class Kisi(models.Model):
    adsoyad = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    email = models.EmailField()
    sirket = models.ForeignKey('Sirket', null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return f"{self.adsoyad}"
    
    def save(self,*args, **kwargs):
        
        super().save(*args, **kwargs)

#.../sirketler/a-sirketi
class Sirket(models.Model):
    isim = models.CharField(max_length=50)
    adres = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)
    email = models.EmailField()
    web = models.URLField()


    def __str__(self):
        return f"{self.isim}"
    
    def save(self,*args, **kwargs):
        
        super().save(*args, **kwargs)
    
class GelenArama(models.Model):
    adsoyad = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    aciklama = models.TextField()
    arama_nedeni = models.CharField(max_length=100)

