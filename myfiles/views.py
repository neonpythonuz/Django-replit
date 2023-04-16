import datetime

from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def index(malumot):
    if malumot.method == "POST":
        ismi = malumot.POST.get('name')
        mail = malumot.POST.get('mail')
        mavzu = malumot.POST.get('subject ')
        xabar = malumot.POST.get('message')
        vaqt = datetime.datetime.now()

        Murojaat(name=ismi,mail=mail,title=mavzu,text=xabar,date=vaqt).save()

    works = Portfolio.objects.all()
    turlar = Type.objects.all()
    return render(malumot,'index.html',{'works': works}, {"types": turlar})

def filter_index(malumot):
    works = Portfolio.objects.filter(tur_id=id)
    turlar = Type.objects.all()
    return render(malumot, 'index.html',{'works': works},{"types": turlar})

def portfolio(malumot):
    return render(malumot,'portfolio-details.html')


def inner_page(malumot):
    return render(malumot, 'inner-page.html')

def single_portfolio(malumot,id):
    work = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{'work':work})


def team(malumot):
    teams = Team.objects.all()
    return render(malumot,'index.html',{'teams': teams})

def service(malumot):
    services = Service.objects.all()
    return render(malumot,'index.html',{'services': services})