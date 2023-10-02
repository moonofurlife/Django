from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    """Функция обработки запроса по маршруту "catalog/" \

        c отображением всего списка телефонов на странице.

    """
    template = 'catalog.html'

    phones = Phone.objects.all()
    # записываем в переменную отображение \
    # всех параметров объектов из базы данных

    sort_param = request.GET.get('sort', '')
    # создаем переменную, с получением и сортировкой объектов

    if sort_param == 'name':
        """Здесь указано условие о сортировке объектов, \

            при выборе пользователем "сортировть по названию", \
                объекты на странице выстраиваются по алфавиту, \

                данным условием в ином случае, устанавлено отображение \
                     объектов на странице по цене, от меньшей к большему.

        """
        phones = phones.order_by('name')
    elif sort_param == 'min_price':
        phones = phones.order_by('price')

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    """Функция обработки запроса по маршруту \

        "catalog/<slug:slug>/", \
            которая отображает на отдельной странице \
                выбранный из "catalog/" телефон, c выводом его характеристик.

    """
    template = 'product.html'

    phone = get_object_or_404(Phone, slug=slug)
    # переменная, в которой происходит вызов функции \
    # отображения ошибки сервера, "страница не найдена"

    context = {
        'phone': phone
    }
    return render(request, template, context)
