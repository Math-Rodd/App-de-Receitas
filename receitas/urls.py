from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('receita/<int:id>/', views.receita_detail, name='receita_detail'),
    path('pesquisar/', views.pesquisar_receitas, name='pesquisar_receitas'),
    path('categoria/<str:categoria>/', views.categoria_receitas, name='categoria_receitas'),
    # Adicione aqui as rotas de categorias quando for implementar
]