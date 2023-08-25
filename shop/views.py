from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from FlowerShop import settings
from shop.models import Consulting, Order, Bouquet, Holiday, Aviso, TimeInterval
from django.views.decorators.csrf import csrf_protect

import uuid
from yookassa import Configuration, Payment
from environs import Env

env = Env()
env.read_env()
ACCOUNT_ID = env('ACCOUNT_ID')
U_KEY = env('U_KEY')


def get_key(value):
    for period in settings.PERIOD:
        if period[1] == value:
            return period[0]
    return None


@csrf_protect
def consult(request):
    fname = request.GET.get('fname', None)
    if fname:
        name = fname
        phone = request.GET['tel']
        Consulting.objects.create(name=name, phone=phone)


@csrf_protect
def create_order(request):
    if request.method == 'POST':
        bouquet = Bouquet.objects.get(id=request.POST['bouquet'][0])
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        period = TimeInterval.objects.get(id=request.POST['orderTime'][0])
        Order.objects.create(
            bouquet=bouquet,
            name=name,
            phone=phone,
            address=address,
            period=period
        )
        Configuration.account_id = ACCOUNT_ID
        Configuration.secret_key = U_KEY

        payment = Payment.create({
            "amount": {
                "value": f"{bouquet.price}",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "http://127.0.0.1:8000/"
            },
            "capture": True,
            "description": f"{bouquet}"
        }, uuid.uuid4())
        confirmation_url = payment.confirmation.confirmation_url
    return redirect(confirmation_url)


def index(request):
    bouquets = Bouquet.objects.all()[:3]
    template = loader.get_template('index.html')
    consult(request)
    context = {
        'bouquets': bouquets
    }
    return render(request, 'index.html', context)


def card(request):
    template = loader.get_template('card.html')
    consult(request)
    return render(request, 'card.html')


@csrf_protect
def catalog(request):
    bouquets = Bouquet.objects.all()
    if request.method == 'POST':
        print(request.POST)

    consult(request)
    context = {
        'bouquets': bouquets
    }
    return render(request, 'catalog.html', context)
    #return HttpResponse(template.render(context))


def catalog_choice(request):
    print(request.GET)
    template = loader.get_template('catalog_choice.html')
    consult(request)
    sender_request_ip = request.META.get('REMOTE_ADDR')
    holiday_name = settings.BOUQUET_CHOICE[f'{sender_request_ip}_event']
    price = settings.BOUQUET_CHOICE[f'{sender_request_ip}_price']
    holiday = Holiday.objects.get(name=holiday_name)
    if price == '<1':
        bouquets = holiday.bouquets.filter(price__lte=1000)
    elif price == '1<5':
        bouquets = holiday.bouquets.filter(price__gt=1000).filter(price__lte=5000)
    elif price == '>5':
        bouquets = holiday.bouquets.filter(price__gt=5000)
    else:
        bouquets = holiday.bouquets.all()
    context = {
        'bouquets': bouquets
    }
    #return HttpResponse(template.render(context))
    return render(request, 'catalog_choice.html', context)


def consultation(request):
    template = loader.get_template('consultation.html')
    consult(request)
    return render(request, 'consultation.html')

@csrf_protect
def order(request, bouquet_id=0):
    time_intervals = TimeInterval.objects.all()
    bouquet = Bouquet.objects.get(id=bouquet_id)
    context ={
        'time_intervals': time_intervals,
        'bouquet': bouquet,
    }
    return render(request, 'order.html', context)


def quiz(request):
    holidays = Holiday.objects.all()
    context = {
        'holidays': holidays
    }
    return render(request, 'quiz.html', context)


@csrf_protect
def quiz_step(request):
    holiday_id = list(request.GET.keys())[0]
    return render(request, 'quiz-step.html', {'holiday_id': holiday_id})



def result(request):
    template = loader.get_template('result.html')
    consult(request)
    return render(request, 'result.html')

