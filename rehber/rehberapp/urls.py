from django.urls import path
from . import views
#url tanımlamalari

#http://127.0.0.1:8000/                     -> index
#http://127.0.0.1:8000/index                -> index
#http://127.0.0.1:8000/kisiler              -> kisiler
#http://127.0.0.1:8000/kisiler/abc-def      -> kisiler
#http://127.0.0.1:8000/gelenaramalar        -> gelenaramalar
#http://127.0.0.1:8000/gidenaramalar        -> gidenaramalar
#http://127.0.0.1:8000/cevapsizaramalar     -> cevapsizaramalar
#http://127.0.0.1:8000/sirketler            -> sirketler
#http://127.0.0.1:8000/sirketler/aaa-bbb    -> sirketler
urlpatterns=[
    path("", views.index,name="home"),
    path("index", views.index),
    path("kisiler", views.kisiler,name="kisiler"),
    path("kisiler/<slug:id>", views.kisiler_detay,name="kisilerdetay"),
    path("kisiler/<slug:id>/duzenle", views.kisiduzenle, name="kisiduzenle"),
    path('kisiler/<slug:id>/sil/', views.kisisil, name='kisisil'),
    path("sirketler", views.sirketler,name="sirketler"),
    path("sirketler/<slug:id>", views.sirketler_detay,name="sirketlerdetay"),
    path("sirketler/<slug:id>/duzenle", views.sirketduzenle,name="sirketduzenle"),
    path("sirketler/<slug:id>/sil", views.sirketsil,name="sirketsil"),
    path('gelen-aramalar/', views.gelen_aramalar, name='gelenaramalar'),
    path('sirket-ekle/', views.sirket_ekle, name='sirketekle'),

]