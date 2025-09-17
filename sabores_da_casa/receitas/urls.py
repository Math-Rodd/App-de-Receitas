from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("receita/<int:receita_id>/", views.detalhes_receita, name="detalhes_receita"),
    path("pesquisar/", views.pesquisar_receitas, name="pesquisar_receitas"),
    path("adicionar/", views.adicionar_receita, name="adicionar_receita"),
    path("editar/<int:receita_id>/", views.editar_receita, name="editar_receita"),
    path("excluir/<int:receita_id>/", views.excluir_receita, name="excluir_receita"),
    path("contato/", views.contato, name="contato"),
    path("sobre/", views.sobre, name="sobre"),
]

from django.contrib.auth import views as auth_views

urlpatterns += [
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="index"), name="logout"),
]
