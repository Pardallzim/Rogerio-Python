from django import forms
from django.forms import ModelForm
from .models import Usuarios, Cards

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = "__all__"
        labels = {
            "nome":"identificação",
            "email":"endereço",
        }
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Ex: João",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Ex: joão@gmail.com",
                }
            )
        }

class CardsForm(forms.ModelForm):
    class Meta:
        model = Cards
        fields = "__all__"
        lables ={
            "title" : "Nome",
            "descripition" : "Descrição",
            "value" : "Valor",
            "path" : "imagem",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Python",
                }
            ),
            "descripition": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Curso fullstack python",
                }
            ),
            "value": forms.NumberInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Ex: 500.00",
                }
            ),
            "path": forms.ClearableFileInput(
                attrs={
                    "class":"form-control",
                }
            )
        }