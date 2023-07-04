from django.shortcuts import render
from django.http.response import HttpResponse

data={
    
}


# Create your views here.


def index(request):
    return render(request,"rehberapp/index.html")

def kisiler(request):
    return render(request,"rehberapp/kisilerlistesi.html")

def kisiler_detay(request,id):
    return render(request,"rehberapp/kisilerdetay.html",{
        "id":id
    })