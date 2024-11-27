from django.urls import path
from . import views


app_name = 'livros'

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('<int:pk>/', views.detalhes_livro, name='detalhes_livro'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('<int:pk>/editar/', views.editar_livro, name='editar_livro'),
    path('<int:pk>/excluir/', views.excluir_livro, name='excluir_livro'),
]