from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from FlowerShop import settings
from shop.models import Consulting, Order, Bouquet, Holiday, Aviso, TimeInterval
from django.views.decorators.csrf import csrf_protect


def get_key(value):
    for period in settings.PERIOD:
        if period[1] == value:
            return period[0]
    return None


def consult(request):
    fname = request.GET.get('fname', None)
    if fname:
        name = fname
        phone = request.GET['tel']
        Consulting.objects.create(name=name, phone=phone)


def create_order(requst):
    print(requst)
    return redirect('https://yookassa.ru/integration/simplepay/payment')


def index(request):
    bouquets = Bouquet.objects.all()[:3]
    template = loader.get_template('index.html')
    consult(request)
    context = {
        'bouquets': bouquets
    }
    return HttpResponse(template.render(context))


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


def catalog_choice(request):
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
    return HttpResponse(template.render(context))


def consultation(request):
    template = loader.get_template('consultation.html')
    consult(request)
    return HttpResponse(template.render({}))

@csrf_protect
def order(request, bouquet_id=0):
    time_intervals = TimeInterval.objects.all()
    bouquet = Bouquet.objects.get(id=bouquet_id)
    template = loader.get_template('order.html')

    name = request.GET.get('fname', None)
    phone = request.GET.get('tel', None)
    address = request.GET.get('adres', None)
    if name and phone and address:
        sender_request_ip = request.META.get('REMOTE_ADDR')
        settings.BOUQUET_CHOICE[f'{sender_request_ip}_bouquet_id'] = bouquet_id
        order_time = request.GET.get('orderTime', None)
        period = get_key(order_time)
        bouquet = Bouquet.objects.get(id=bouquet_id)
        if period:
            order = Order.objects.create(bouquet=bouquet, name=name, phone=phone, address=address, period=period)
        else:
            order = Order.objects.create(bouquet=bouquet, name=name, phone=phone, address=address)
        settings.BOUQUET_CHOICE[f'{sender_request_ip}_order_id'] = order.id
        return redirect('order-step')
    consult(request)
    context ={
        'time_intervals': time_intervals,
        'bouquet': bouquet,
    }
    return HttpResponse(template.render(context))


def quiz(request):
    template = loader.get_template('quiz.html')
    event = request.GET.get('event', None)
    sender_request_ip = request.META.get('REMOTE_ADDR')
    if event:
        settings.BOUQUET_CHOICE[f'{sender_request_ip}_event'] = event
        return redirect('quiz-step')
    return HttpResponse(template.render({}))


def quiz_step(request):
    template = loader.get_template('quiz-step.html')
    price = request.GET.get('price', None)
    sender_request_ip = request.META.get('REMOTE_ADDR')
    if price:
        settings.BOUQUET_CHOICE[f'{sender_request_ip}_price'] = request.GET['price']
        return redirect('catalog_choice')
    return HttpResponse(template.render({}))


def result(request):
    template = loader.get_template('result.html')
    consult(request)
    return HttpResponse(template.render({}))
