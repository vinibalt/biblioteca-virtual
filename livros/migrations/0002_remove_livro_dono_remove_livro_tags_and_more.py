# Generated by Django 5.1.3 on 2024-11-27 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='dono',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='tags',
        ),
        migrations.AddField(
            model_name='livro',
            name='publicado_em',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='livro',
            name='categoria',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='idioma',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='status',
            field=models.CharField(choices=[('wishlist', 'Wishlist'), ('lendo', 'Lendo'), ('lido', 'Lido')], default='wishlist', max_length=20),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]
