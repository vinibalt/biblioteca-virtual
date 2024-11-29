from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'livros'

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('<int:pk>/', views.detalhes_livro, name='detalhes_livro'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('<int:pk>/editar/', views.editar_livro, name='editar_livro'),
    path('<int:pk>/excluir/', views.excluir_livro, name='excluir_livro'),
    path('troca/<int:livro_id>/', views.criar_troca, name='troca_livro'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registrar/', views.registrar, name='registrar'),
    path('troca/<int:livro_id>/', views.criar_troca, name='troca_livro'),
    path('trocas/', views.listar_trocas, name='lista_trocas'),
    path('troca/<int:troca_id>/<str:acao>/', views.atualizar_troca, name='atualizar_troca'),

]