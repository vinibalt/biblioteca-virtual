from django.shortcuts import render
from .models import Livro, Troca
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Livro

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Livro, Troca

def logout_view(request):
    logout(request)
    return redirect('livros:login')



def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listar_livros.html', {'livros': livros})


@login_required
def atualizar_troca(request, troca_id, acao):
    troca = Troca.objects.get(id=troca_id)


    if troca.dono != request.user:
        return HttpResponseForbidden("Você não tem permissão para alterar essa troca.")

    if acao == 'aceitar':
        troca.status = 'aceita'
    elif acao == 'recusar':
        troca.status = 'recusada'
    troca.save()

    return redirect('livros:lista_trocas')

@login_required
def listar_trocas(request):
    minhas_solicitacoes = Troca.objects.filter(solicitante=request.user)
    minhas_respostas = Troca.objects.filter(dono=request.user)

    return render(request, 'livros/lista_trocas.html', {
        'minhas_solicitacoes': minhas_solicitacoes,
        'minhas_respostas': minhas_respostas
    })


@login_required
def criar_troca(request, livro_id):
    livro = Livro.objects.get(id=livro_id)

    # Verifica se o usuário está tentando trocar um livro dele mesmo
    if livro.dono == request.user:
        return HttpResponseForbidden("Você não pode solicitar trocas para seus próprios livros.")

    troca = Troca.objects.create(
        livro=livro,
        solicitante=request.user,
        dono=livro.dono
    )

    return redirect('livros:lista_trocas')

@login_required
def solicitar_troca(request, livro_id):
    livro_desejado = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        livro_oferecido_id = request.POST['livro_oferecido']
        livro_oferecido = get_object_or_404(Livro, id=livro_oferecido_id, usuario=request.user)

        Troca.objects.create(
            livro_oferecido=livro_oferecido,
            livro_desejado=livro_desejado,
            solicitante=request.user,
        )
        return redirect('livros:listar_livros')

    return render(request, 'livros/solicitar_troca.html', {'livro_desejado': livro_desejado})


def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})

def listar_livros(request):
    query = request.GET.get('q')  # Termo de busca
    livros = Livro.objects.all()

    if query:
        livros = livros.filter(
            Q(titulo__icontains=query) |
            Q(categoria__icontains=query) |
            Q(idioma__icontains=query) |
            Q(status__icontains=query)
        )

    return render(request, 'livros/livro_list.html', {'livros': livros})

def detalhes_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livros/livro_detail.html', {'livro': livro})

def adicionar_livro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        categoria = request.POST['categoria']
        idioma = request.POST['idioma']
        status = request.POST['status']
        publicado_em = request.POST['publicado_em']

        Livro.objects.create(
            titulo=titulo,
            autor=autor,
            categoria=categoria,
            idioma=idioma,
            status=status,
            publicado_em=publicado_em,
            dono=request.user
        )
        return redirect('livros:listar_livros')

    return render(request, 'livros/livro_form.html')

def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        livro.titulo = request.POST['titulo']
        livro.autor = request.POST['autor']
        livro.categoria = request.POST['categoria']
        livro.idioma = request.POST['idioma']
        livro.status = request.POST['status']
        livro.publicado_em = request.POST['publicado_em']
        livro.save()
        return redirect('livros:listar_livros')

    return render(request, 'livros/livro_form.html', {'livro': livro})

def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        livro.delete()
        return redirect('livros:listar_livros')

    return render(request, 'livros/livro_confirm_delete.html', {'livro': livro})


