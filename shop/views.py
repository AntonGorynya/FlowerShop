import telegram

from .telegram_norification import send_notification
from django.shortcuts import render, loader, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from shop.models import Consulting, Order, Bouquet, Holiday, TimeInterval
from yookassa import Configuration, Payment
from environs import Env
import uuid


env = Env()
env.read_env()
ACCOUNT_ID = env('ACCOUNT_ID')
U_KEY = env('U_KEY')
TELEGRAM_KEY = env('TELEGRAM_KEY')
CHAT_ID = env('CHAT_ID')
BOT = telegram.Bot(token=TELEGRAM_KEY)


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
        bouquet = Bouquet.objects.get(id=request.POST['bouquet'])
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        period = TimeInterval.objects.get(id=request.POST['orderTime'])
        order = Order.objects.create(
            bouquet=bouquet,
            name=name,
            phone=phone,
            address=address,
            period=period
        )
        message = f"""
            Заказ номер {order.id} создан. 
            Клиент: {name} {phone}
            Доставка на {address}
            Время доставки: {period}
            Букет {bouquet}
        """
        send_notification(BOT, CHAT_ID, message)
        Configuration.account_id = ACCOUNT_ID
        Configuration.secret_key = U_KEY

        payment = Payment.create({
            "amount": {
                "value": f"{bouquet.price}",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": f"http://kaser137.pythonanywhere.com/?id={bouquet.id}"
            },
            "capture": True,
            "description": f"{bouquet}",
            "metadata": {"order": order.id}
        }, uuid.uuid4())
        confirmation_url = payment.confirmation.confirmation_url
    return redirect(confirmation_url)


def index(request):
    bouquets = Bouquet.objects.all()[:3]
    consult(request)
    context = {
        'bouquets': bouquets
    }
    return render(request, 'index.html', context)


def card(request):
    consult(request)
    return render(request, 'card.html')


@csrf_protect
def catalog(request):
    if 'holiday' not in request.GET:
        bouquets = Bouquet.objects.all()
    else:
        min_price, max_price = list(request.GET)[0].split('_')
        bouquets = Bouquet.objects.filter(
            holidays__id=request.GET.get('holiday'),
            price__gte=min_price,
            price__lte=max_price
        )
    paginator = Paginator(bouquets, 3)
    page = request.GET.get('page')
    try:
        bouquets_page = paginator.page(page)
    except PageNotAnInteger:
        bouquets_page = paginator.page(1)
    except EmptyPage:
        bouquets_page = paginator.page(paginator.num_pages)
    consult(request)
    context = {
        'bouquets': bouquets,
        'page': page,
        'bouquets_page': bouquets_page
    }
    return render(request, 'catalog.html', context)


def consultation(request):
    template = loader.get_template('consultation.html')
    consult(request)
    return render(request, 'consultation.html')


@csrf_protect
def order(request, bouquet_id=0):
    time_intervals = TimeInterval.objects.all()
    bouquet = Bouquet.objects.get(id=bouquet_id)
    context = {
        'time_intervals': time_intervals,
        'bouquet': bouquet,
    }
    return render(request, 'order.html', context)


@csrf_protect
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
