from django.shortcuts import render, loader
from django.http import HttpResponse
from shop.models import Consulting, Order, Bouquet, Holiday


def consult(request):
    if request.GET:
        name = request.GET['fname']
        phone = request.GET['tel']
        Consulting.objects.create(name=name, phone=phone)


def index(request):
    template = loader.get_template('index.html')
    consult(request)
    return HttpResponse(template.render({}))


def card(request):
    template = loader.get_template('card.html')
    consult(request)
    return HttpResponse(template.render({}))


def catalog(request):
    template = loader.get_template('catalog.html')
    bouquets = Bouquet.objects.all()
    consult(request)
    context = {
        'bouquets': bouquets
    }
    return HttpResponse(template.render(context))


def consultation(request):
    template = loader.get_template('consultation.html')
    consult(request)
    return HttpResponse(template.render({}))


def order(request, bouquet_id=0):
    template = loader.get_template('order.html')
    return HttpResponse(template.render({}))


def order_step(request):
    template = loader.get_template('order-step.html')
    return HttpResponse(template.render({}))


def quiz(request):
    template = loader.get_template('quiz.html')
    return HttpResponse(template.render({}))


def quiz_step(request):
    template = loader.get_template('quiz-step.html')
    return HttpResponse(template.render({}))


def result(request):
    template = loader.get_template('result.html')
    consult(request)
    return HttpResponse(template.render({}))
