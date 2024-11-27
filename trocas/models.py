from django.db import models
from livros.models import Livro
from django.contrib.auth.models import User

class Troca(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aceito', 'Aceito'),
        ('rejeitado', 'Rejeitado'),
    ]

    livro_oferecido = models.ForeignKey(Livro, related_name='oferecido', on_delete=models.CASCADE)
    livro_desejado = models.ForeignKey(Livro, related_name='desejado', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    solicitante = models.ForeignKey(User, related_name='solicitante', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='destinatario', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.solicitante} -> {self.destinatario} ({self.status})"

class Notificacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.TextField()
    livro_relacionado = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, blank=True)
    lida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificação para {self.usuario.username}: {self.mensagem}"