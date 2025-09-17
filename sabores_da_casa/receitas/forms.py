from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'ingredientes', 'preparo', 'imagem']

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Seu nome")
    email = forms.EmailField(label="Seu e-mail")
    mensagem = forms.CharField(widget=forms.Textarea, label="Mensagem")