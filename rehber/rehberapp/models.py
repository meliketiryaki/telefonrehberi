from django.db import models

class Kisi(models.Model):
    adsoyad = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    sirket = models.ForeignKey('Sirket', on_delete=models.CASCADE)

class Sirket(models.Model):
    isim = models.CharField(max_length=50)
    adres = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    web = models.URLField()

class GelenArama(models.Model):
    adsoyad = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    aciklama = models.TextField()
    arama_nedeni = models.CharField(max_length=100)
