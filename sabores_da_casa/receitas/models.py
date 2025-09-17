from django.db import models


class Receita(models.Model):
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField()
    preparo = models.TextField()
    imagem = models.ImageField(upload_to="receitas/", blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
