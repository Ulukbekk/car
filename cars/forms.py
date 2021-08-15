from django import forms

from cars.models import Car


class CarAddForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('image', 'category', 'title', 'color', 'transmission',
                   'volume', 'rul', 'release_date', 'price', 'description', )

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('image', 'category', 'title', 'color', 'transmission',
                'volume', 'rul', 'release_date', 'price', 'description',)
