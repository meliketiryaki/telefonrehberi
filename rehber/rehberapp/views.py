from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from rehberapp.models import Kisi,Sirket,GelenArama
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.forms.models import model_to_dict
from .forms import SirketForm



def index(request):
    if request.method == 'POST' and 'telefon_rehberi' in request.POST:
        return redirect('kisiler')  # Kişiler listesi URL'sine yönlendirme yapılır
    return render(request, 'rehberapp/index.html')

def kisiler(request):
    context = {  
            "kisiler": Kisi.objects.all(),
            "sirketler": Sirket.objects.all()
    }
    return render(request,"rehberapp/kisilerlistesi.html",context)

def kisiler_detay(request,id):
    
    k=Kisi.objects.get(id=id)
  
    return JsonResponse(model_to_dict(k), safe=False, status=200)

def sirketler(request):
    
    
    serialized_data = serialize("json", Sirket.objects.all())
    serialized_data = json.loads(serialized_data)

    return JsonResponse(serialized_data, safe=False, status=200)
            

    

def sirketler_detay(request,id):
    s=Sirket.objects.get(id=id)

    return JsonResponse(model_to_dict(s), safe=False, status=200)

def gelen_aramalar(request):
    aramalar = GelenArama.objects.all()
    context = {
        'aramalar': aramalar
    }
    return render(request, 'rehberapp/gelenaramalar.html', context)


def kisiduzenle(request, slug):
    kisi = get_object_or_404(Kisi, slug=slug)  # Kişi nesnesini slug değerine göre getirir veya 404 hatası döndürür
    from .forms import KisiForm
    if request.method == 'POST':
        # Eğer form gönderildiyse, formdan gelen verileri al ve kişi nesnesini güncelle
        form = KisiForm(request.POST, instance=kisi)
        if form.is_valid():
            form.save()
            return redirect('kisiler')  # Kişilerin listelendiği sayfaya yönlendir
    else:
        # GET isteği olduğunda, kişi düzenleme formunu oluştur ve şu anki kişinin verileriyle doldur
        form = KisiForm(instance=kisi)

    return render(request, 'rehberapp/kisiduzenle.html', {'form': form, 'kisi': kisi})


def kisisil(request, slug):
    kisi = get_object_or_404(Kisi, slug=slug)  # Kişi nesnesini slug değerine göre getirir veya 404 hatası döndürür

    if request.method == 'POST':
        # Eğer POST isteği ise, kişiyi sil ve kişiler sayfasına yönlendir
        kisi.delete()
        return redirect('kisiler')

    return render(request, 'kisisil.html', {'kisi': kisi})




def sirket_ekle(request):
    if request.method == 'POST':
        form = SirketForm(request.POST)
        if form.is_valid():
            sirket = form.save()  # Yeni bir Sirket nesnesi oluşturulur ve veritabanına kaydedilir
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        return JsonResponse({'success': False, 'errors': 'Geçersiz istek metodu'})


def sirketduzenle(request, id):
    sirket = get_object_or_404(Sirket, id=id)  # Kişi nesnesini slug değerine göre getirir veya 404 hatası döndürür
    from .forms import SirketForm
    if request.method == 'POST':
        # Eğe(r form gönderildiyse, formdan gelen verileri al ve kişi nesnesini güncelle
        print("hello")
        form = SirketForm(request.POST, instance=sirket)
        if form.is_valid():
            form.save()

            return redirect('sirketler')  # Kişilerin listelendiği sayfaya yönlendir
    else:
        # GET isteği olduğunda, kişi düzenleme formunu oluştur ve şu anki kişinin verileriyle doldur
        form = SirketForm(instance=sirket)

    return render(request, 'rehberapp/sirketduzenle.html', {'form': form, 'sirket': sirket})

def sirketsil(request, id):
    sirket = get_object_or_404(Sirket, id=id)  # Kişi nesnesini slug değerine göre getirir veya 404 hatası döndürür

    if request.method == 'POST':
        # Eğer POST isteği ise, kişiyi sil ve kişiler sayfasına yönlendir
        sirket.delete()
        return redirect('sirketler')

    return render(request, 'sirketsil.html', {'sirket': sirket})