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

    def __str__(self):
        return self.titulo