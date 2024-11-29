from django.contrib.auth.models import User
from django.db import models

class Livro(models.Model):
    STATUS_CHOICES = [
        ('wishlist', 'Wishlist'),
        ('lendo', 'Lendo'),
        ('lido', 'Lido'),
    ]

    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    idioma = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='wishlist')
    publicado_em = models.DateField(blank=True, null=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="meus_livros")  # Novo campo para associar ao usuário

    def __str__(self):
        return self.titulo


class Troca(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes_feitas')
    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes_recebidas')
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('aceita', 'Aceita'),
        ('recusada', 'Recusada')
    ], default='pendente')

    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.solicitante} solicitou {self.livro} de {self.dono}"