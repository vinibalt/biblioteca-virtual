from django.urls import path
from . import views

urlpatterns = [
    path('solicitar/<int:livro_id>/', views.solicitar_troca, name='solicitar_troca'),
    path('gerenciar/', views.gerenciar_trocas, name='gerenciar_trocas'),
    path('notificacoes/', views.listar_notificacoes, name='listar_notificacoes')

]
