"""FlowerShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from FlowerShop import settings
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='indexpage'),
    path('card/', views.card, name='card'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog_choice/', views.catalog_choice, name='catalog_choice'),
    path('consultation/', views.consultation, name='consultation'),
    path('order/<int:bouquet_id>/', views.order, name='order'),
    path('create_order/', views.create_order, name='create_order'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz-step/', views.quiz_step, name='quiz-step'),
    path('result/', views.result, name='result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
