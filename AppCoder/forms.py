from django import forms

class CursoFormulario(forms.Form):
    dashboard = forms.CharField(max_length=20)
    camada = forms.IntegerField()

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)
    