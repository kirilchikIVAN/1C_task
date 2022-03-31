from .models import Filter, SelectedRoom
from django.forms import ModelForm, TextInput, DateTimeInput, IntegerField
from django import forms


class FilterFrom(ModelForm):
    class Meta:
        model = Filter
        fields = ['capacity',
                  'activity',
                  'date_start',
                  'date_finish']

        widgets = {
            'capacity': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кол-во человек',
            }),
            'activity': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цель',
            }),
            'date_start': DateTimeInput(attrs={
                # 'type': 'time',
                'class': 'form-control',
                'placeholder': '2000-01-15 10:10 - начало',
            }),
            'date_finish': DateTimeInput(attrs={
                # 'type': 'time',
                'class': 'form-control',
                'placeholder': '2002-01-15 23:59 - конец',
            }),
        }


class SelectedRoomForm(ModelForm):
    class Meta:
        model = SelectedRoom
        fields = ['numb']
        widgets = {
            # 'id': TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Номер комнаты',
            # }),
            'numb': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер комнаты',
            })

        }
