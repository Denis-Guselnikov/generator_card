from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CardForm
from .models import Cards


def index(request):
    cards = Cards.objects.all()
    context = {'cards': cards}
    return render(request, 'cards/index.html', context)


def view_info(request, id):
    return HttpResponseRedirect(reverse('cards:index'))


def edit_card(request, id):
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
    if request.method == 'POST':
        card = Cards.objects.get(pk=id)
        card.delete()
        return HttpResponseRedirect(reverse('cards:index'))


def add_card(request):
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
