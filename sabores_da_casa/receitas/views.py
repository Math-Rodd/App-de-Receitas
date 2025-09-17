from django.shortcuts import render, redirect, get_object_or_404
from .models import Receita
from .forms import ReceitaForm, ContatoForm
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    receitas = Receita.objects.all()
    return render(request, "index.html", {"receitas": receitas})


def detalhes_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    return render(request, "detalhes_receita.html", {"receita": receita})


def pesquisar_receitas(request):
    query = request.GET.get("q", "")
    receitas = Receita.objects.filter(Q(titulo__icontains=query))
    return render(request, "pesquisa.html", {"receitas": receitas, "query": query})


def adicionar_receita(request):
    if request.method == "POST":
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ReceitaForm()
    return render(request, "adicionar.html", {"form": form})


def editar_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    if request.method == "POST":
        form = ReceitaForm(request.POST, request.FILES, instance=receita)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ReceitaForm(instance=receita)
    return render(request, "adicionar.html", {"form": form, "editar": True})


def excluir_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    if request.method == "POST":
        receita.delete()
        return redirect("index")
    return render(request, "excluir.html", {"receita": receita})


def contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            mensagem = form.cleaned_data["mensagem"]
            # Enviar e-mail (configure o e-mail no settings.py)
            send_mail(
                f"Contato de {nome}",
                mensagem,
                email,
                [settings.DEFAULT_FROM_EMAIL],  # ou seu e-mail
                fail_silently=False,
            )
            return render(request, "contato.html", {"form": ContatoForm(), "sucesso": True})
    else:
        form = ContatoForm()
    return render(request, "contato.html", {"form": form})


def sobre(request):
    return render(request, "sobre.html")
