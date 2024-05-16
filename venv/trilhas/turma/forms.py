from django import forms
from django.forms import ModelForm
from .models import Pedido , Usuarios, Itens

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["numero"]
        labels = {
            "numero":"numero1"
        }
        widgets = {
            "numero": forms.NumberInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Ex: 22",
                }
            )
        }


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

class ItensForm(forms.ModelForm):
    class Meta:
        model = Itens
        fields = "__all__"
        labels = {
            "nome": "nome",
            "preco": "valor",
            "path": "img",
        }
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Ex: João",
                }
            ),
            "preco": forms.NumberInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Ex: joão@gmail.com",
                }
            ),
            "path": forms.ClearableFileInput(
                attrs={
                    "class":"form-control",
                }
            )
        }