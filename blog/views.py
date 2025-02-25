from django.shortcuts import render, redirect
from unicodedata import category

from .models import About, Portfolio,Category,Services,Resume,HeppiClents
from .forms import Contect

def index (request):
    about = About.objects.all()
    portfolio = Portfolio.objects.all()[::-1]
    categorya = Category.objects.all()
    servise = Services.objects.all()
    resume = Resume.objects.all()
    heppi = HeppiClents.objects.all()
    contect = Contect(request.POST or None)
    if contect.is_valid():
        contect.save()
        return redirect(".")
    ctx = {
        "about" : about,
        "portfolio" : portfolio,
        "categoriya" : categorya,
        "servis" : servise,
        "resume" : resume,
        "heppi" : heppi,
        "form" : contect
    }
    return render(request, "index.html", ctx)