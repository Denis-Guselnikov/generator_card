from django import forms

from .models import Cards


class DateInput(forms.DateInput):
    input_type = 'date'


class CardForm(forms.ModelForm):

    class Meta:
        model = Cards
        fields = '__all__'
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'card_series': 'Серия карты',
            'number_card': 'Номер карты',
            'amount': 'Сумма',
            'data_end': 'Дата окончания',
            'status': 'Статус карты'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'card_series': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_card': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'data_end': DateInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
