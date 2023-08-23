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


def consultation(request):
    template = loader.get_template('consultation.html')
    return HttpResponse(template.render({}))


def order(request):
    template = loader.get_template('order.html')
    return HttpResponse(template.render({}))


def quiz(request):
    template = loader.get_template('quiz.html')
    return HttpResponse(template.render({}))


def quiz_step(request):
    template = loader.get_template('quiz-step.html')
    return HttpResponse(template.render({}))


def result(request):
    template = loader.get_template('result.html')
    return HttpResponse(template.render({}))
