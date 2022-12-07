import json

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import CardForm
from .models import Cards


def search_card(request):
    """Поисковик на главной странице"""
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        cards = Cards.objects.filter(
            first_name__icontains=search_str) | Cards.objects.filter(
            last_name__icontains=search_str) | Cards.objects.filter(
            card_series__istartswith=search_str) | Cards.objects.filter(
            number_card__istartswith=search_str) | Cards.objects.filter(
            amount__istartswith=search_str) | Cards.objects.filter(
            data_created__istartswith=search_str) | Cards.objects.filter(
            data_end__istartswith=search_str) | Cards.objects.filter(
            status__icontains=search_str)

        data = cards.values()
        return JsonResponse(list(data), safe=False)


def index(request):
    """Главная страница"""
    cards = Cards.objects.all()
    paginator = Paginator(cards, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'cards': cards, 'page_obj': page_obj}
    return render(request, 'cards/index.html', context)


def view_info(request, id):
    """Информация об объекте"""
    return HttpResponseRedirect(reverse('cards:index'))


def edit_card(request, id):
    """Редактирование объекта"""
    if request.method == 'POST':
        card = Cards.objects.get(pk=id)
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return render(request, 'cards/edit_card.html', {
                'form': form,
                'success': True})
    else:
        card = Cards.objects.get(pk=id)
        form = CardForm(instance=card)
    return render(request, 'cards/edit_card.html', {
                'form': form})


def delete_card(request, id):
    """Удаление объекта"""
    if request.method == 'POST':
        card = Cards.objects.get(pk=id)
        card.delete()
        return HttpResponseRedirect(reverse('cards:index'))


def add_card(request):
    """Добавление нового объекта"""
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_card_series = form.cleaned_data['card_series']
            new_number_card = form.cleaned_data['number_card']
            new_amount = form.cleaned_data['amount']
            new_data_end = form.cleaned_data['data_end']
            new_status = form.cleaned_data['status']

            new_card = Cards(
                first_name=new_first_name,
                last_name=new_last_name,
                card_series=new_card_series,
                number_card=new_number_card,
                amount=new_amount,
                data_end=new_data_end,
                status=new_status
            )
            new_card.save()
            return render(request, 'cards/add_card.html', {
                'form': CardForm(), 'success': True})
    else:
        form = CardForm()
    return render(request, 'cards/add_card.html', {
        'form': CardForm()})
