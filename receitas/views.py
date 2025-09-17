from django.shortcuts import render, get_object_or_404
from .models import Receita

def home(request):
    return render(request, 'receitas/home.html')

def sobre(request):
    return render(request, 'receitas/sobre.html')

def contato(request):
    return render(request, 'receitas/contato.html')

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receitas/receita_detail.html', {'receita': receita})

def pesquisar_receitas(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Receita.objects.filter(title__icontains=query)
    return render(request, 'receitas/pesquisa.html', {
        'query': query,
        'resultados': resultados
    })

def categoria_receitas(request, categoria):
    receitas = Receita.objects.filter(categoria__iexact=categoria)
    return render(request, 'receitas/categoria.html', {
        'categoria': categoria,
        'receitas': receitas
    })