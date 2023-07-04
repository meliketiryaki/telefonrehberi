from django.urls import path
from . import views
#url tanımlamalari

#http://127.0.0.1:8000/                 -> index
#http://127.0.0.1:8000/index            -> index
#http://127.0.0.1:8000/kisiler          -> kisiler
#http://127.0.0.1:8000/kisiler/1        -> kisiler
#http://127.0.0.1:8000/gelenaramalar    -> gelenaramalar
#http://127.0.0.1:8000/gidenaramalar    -> gidenaramalar
#http://127.0.0.1:8000/cevapsizaramalar -> cevapsizaramalar


urlpatterns=[
    path("", views.index,name="home"),
    path("index", views.index),
    path("kisiler", views.kisiler,name="kisiler"),
    path("kisiler/<int:id>", views.kisiler_detay,name="kisilerdetay"),
]