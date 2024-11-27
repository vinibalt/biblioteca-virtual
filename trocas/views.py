from django.shortcuts import render, redirect, get_object_or_404
from livros.models import Livro
from .models import Troca
from django.contrib.auth.models import User
from .models import Notificacao

def gerenciar_trocas(request):
    # Solicitações recebidas e enviadas
    solicitacoes_recebidas = Troca.objects.filter(destinatario=request.user, status='pendente')
    solicitacoes_enviadas = Troca.objects.filter(solicitante=request.user)

    if request.method == 'POST':
        troca_id = request.POST['troca_id']
        acao = request.POST['acao']
        troca = get_object_or_404(Troca, id=troca_id)

        if acao == 'aceitar':
            troca.status = 'aceito'
        elif acao == 'rejeitar':
            troca.status = 'rejeitado'

        troca.save()
        if acao == 'aceitar':
            mensagem = f"Sua solicitação de troca pelo livro '{troca.livro_desejado.titulo}' foi aceita!"
        elif acao == 'rejeitar':
            mensagem = f"Sua solicitação de troca pelo livro '{troca.livro_desejado.titulo}' foi rejeitada."

        Notificacao.objects.create(
            usuario=troca.solicitante,
            mensagem=mensagem,
            livro_relacionado=troca.livro_desejado
        )

        return redirect('gerenciar_trocas')

    return render(request, 'trocas/gerenciar_trocas.html', {
        'solicitacoes_recebidas': solicitacoes_recebidas,
        'solicitacoes_enviadas': solicitacoes_enviadas,
    })


def solicitar_troca(request, livro_id):
    # Livro desejado
    livro_desejado = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        # Livro oferecido e usuário solicitante
        livro_oferecido_id = request.POST['livro_oferecido']
        livro_oferecido = get_object_or_404(Livro, id=livro_oferecido_id)
        solicitante = request.user
        destinatario = livro_desejado.dono

        Notificacao.objects.create(
            usuario=destinatario,
            mensagem=f"{solicitante.username} solicitou trocar o livro '{livro_oferecido.titulo}' pelo seu livro '{livro_desejado.titulo}'.",
            livro_relacionado=livro_desejado
        )

        # Cria a troca
        Troca.objects.create(
            livro_oferecido=livro_oferecido,
            livro_desejado=livro_desejado,
            solicitante=solicitante,
            destinatario=destinatario,
        )
        return redirect('listar_livros')

    # Lista apenas livros do usuário solicitante
    livros_usuario = Livro.objects.filter(dono=request.user)

    return render(request, 'trocas/solicitar_troca.html', {
        'livro_desejado': livro_desejado,
        'livros_usuario': livros_usuario,
    })


def listar_notificacoes(request):
    notificacoes = Notificacao.objects.filter(usuario=request.user).order_by('-data_criacao')
    if request.method == 'POST':
        notificacao_id = request.POST.get('notificacao_id')
        notificacao = Notificacao.objects.get(id=notificacao_id, usuario=request.user)
        notificacao.lida = True
        notificacao.save()
        return redirect('listar_notificacoes')

    return render(request, 'trocas/listar_notificacoes.html', {
        'notificacoes': notificacoes,
    })
