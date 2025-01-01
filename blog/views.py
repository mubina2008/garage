from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Banner,Catagary,Camputers,Mansclothers,Woman
from .forms import ContactForm
from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here

class ComputersUpdateView(UpdateView):
    model = Camputers
    fields = ('name','bio','img','price','price2')
    template_name = 'ComputersEdit.html'


class ComputersDeleteView(DeleteView):
    model = Camputers
    template_name = 'ComputersDelete.html'
    success_url = reverse_lazy('index')


class ComputersCreateView(CreateView):
    model = Camputers
    template_name = 'ComputersCreateView.html'
    success_url = reverse_lazy('index')
    fields = ('name','bio','img','price2')


def computers(request):
    camputers = Camputers.objects.all()
    context = {
        'camputers': camputers
    }

    return render(request,'computers.html', context=context)


def index(request):
    banner = Banner.objects.all()
    catagary = Catagary.objects.all()
    camputers = Camputers.objects.all()
    mansclothers = Mansclothers.objects.all()
    woman = Woman.objects.all()
    contact = ContactForm(request.POST or None)
    if request.method == " POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>Sorovingiz muvaffaqiyatli amalga oshirildi. Rahmat")
    context = {
        'banner':banner,
        'catagary':catagary,
        'camputers':camputers,
        'mansclothers':mansclothers,
        'woman':woman
    }
    return render(request,'index.html', context=context)


def contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>Sorovingiz muaffaqiyatli amalga oshirildi. Rahmat")
    context = {
        'contact': contact
    }
    return render(request,'contact.html',context=context)


def mans_clothers(request):
    mansclothers = Mansclothers.objects.all()
    context = {
        'mansclothers': mansclothers
    }
    return render(request,'mans_clothers.html', context=context)


def womans_clothers(request):
    woman = Woman.objects.all()
    context = {
        'woman': woman
    }
    return render(request,'womans_clothers.html', context=context)


def detail(request,id):
    banner = Banner.objects.get(id=id)
    context = {
        'x':banner
    }
    return render(request,'detail.html', context=context)


def cdetail(request,id):
    catagary = Catagary.objects.get(id=id)
    context = {
        'x': catagary
    }
    return render(request,'cdetail.html', context=context)


def comdetail(request,computers):
    camputers = get_object_or_404(Camputers, slug=computers)
    context = {
        'x': camputers
    }
    return render(request,'comdetail.html', context=context)


def mdetail(request,id):
    mansclothers = Mansclothers.objects.get(id=id)
    context = {
        'x':mansclothers
    }
    return render(request,'mdetail.html', context=context)



def wdetail(request,id):
    woman = Woman.objects.get(id=id)
    context = {
        'x':woman
    }
    return render(request,'wdetail.html', context=context)
