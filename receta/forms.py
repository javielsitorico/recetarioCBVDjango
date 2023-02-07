from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
     class Meta:
          model = Receta
          fields = ['nombre', 'subnombre', 'imagen', 'ingredientes', 'receta', 'author', 'categorias']
          # Esto se usaría para modificar el elemento que queramos de estilo o propiedades
          # widgets = {
          #      'nombre': forms.TextInput(attrs={'style': 'background-color: red'}),
          #      'subnombre': forms.TextInput(attrs={'placeholder': 'Inserta un subnombre'})
          # }