from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    GENRE_A = 'comedy'
    GENRE_B = 'thriller'
    GENRE_C = 'romance'
    GENRE_CHOICES = [
        (GENRE_A, '코미디'),
        (GENRE_B, '공포'),
        (GENRE_C, '로맨스'),
    ]

    genre = forms.ChoiceField(choices=GENRE_CHOICES)

    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'score': forms.NumberInput(attrs={
                'step':0.5,
                'min':0,
                'max':5
            }),
            'release_date':forms.DateInput(attrs={'type':'date'}),
        }
