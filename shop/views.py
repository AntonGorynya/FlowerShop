from django.shortcuts import render, loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}))


def card(request):
    template = loader.get_template('card.html')
    return HttpResponse(template.render({}))


def catalog(request):
    template = loader.get_template('catalog.html')
    return HttpResponse(template.render({}))

