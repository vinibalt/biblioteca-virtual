from django.shortcuts import render
from .models import Livro
from django.shortcuts import render, redirect
from django.contrib.auth.models import User




def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listar_livros.html', {'livros': livros})


from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Livro

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


