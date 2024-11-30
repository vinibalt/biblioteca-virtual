
# Biblioteca Virtual

## Descrição

A **Biblioteca Virtual** é um sistema web desenvolvido utilizando o framework **Django**. O objetivo principal do sistema é permitir que os usuários registrem, organizem e gerenciem seus livros de maneira prática e eficiente. Além disso, o sistema oferece funcionalidades de busca, categorização de livros e simulação de trocas entre os usuários.

### Funcionalidades Principais:
- **Cadastro de Livros:** Os usuários podem adicionar livros ao sistema, fornecendo informações como título, autor, categoria, idioma, status e data de publicação.
- **Edição e Exclusão de Livros:** Os usuários podem editar ou excluir livros cadastrados no sistema.
- **Busca de Livros:** Permite a busca por livros através de diferentes critérios (título, autor, categoria, idioma e status).
- **Classificação de Livros:** Os livros são classificados por status (ex: "lido", "lendo", "wishlist") e por categoria e idioma.
- **Troca de Livros:** Funcionalidade opcional para simular o processo de troca de livros entre os usuários.
- **Notificações:** Sistema simples de notificações para lembrar sobre livros a serem lidos ou atualizações no sistema de trocas.

## Tecnologias Usadas

- **Django:** Framework web para desenvolvimento rápido.
- **Python:** Linguagem de programação usada no backend.
- **SQLite:** Banco de dados embutido (não exige configuração de banco externo).
- **Bootstrap:** Framework CSS para estilização rápida e responsiva.
- **HTML/CSS:** Para criação de páginas web interativas e visualmente agradáveis.

## Como Rodar o Projeto

### Pré-requisitos

1. **Python 3.13** ou superior.
2. **Django** instalado (ou o virtual environment configurado).

### Passos para Configuração:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/vinibalt/biblioteca_virtual.git
   cd biblioteca_virtual
   ```

2. **Instale as dependências:**

   Crie um ambiente virtual e instale o Django:

   ```bash
   python -m venv env
   source env/bin/activate  # No Linux/Mac
   env\Scripts\activate  # No Windows
   pip install -r requirements.txt
   ```

   Se você não tem o arquivo `requirements.txt`, instale o Django manualmente:

   ```bash
   pip install django
   ```

3. **Configuração do Banco de Dados:**

   O banco de dados padrão é o **SQLite**, que vem configurado por padrão no Django. Se você precisar de outro banco de dados, será necessário ajustar a configuração no arquivo `settings.py`.

4. **Realize as migrações:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário para acessar o admin (opcional):**

   ```bash
   python manage.py createsuperuser
   ```

   Siga as instruções para criar o superusuário.

6. **Execute o servidor:**

   ```bash
   python manage.py runserver
   ```

   O servidor será iniciado em `http://127.0.0.1:8000/`.

### Acessando o Sistema

- **Página Inicial:** Visualize e busque os livros cadastrados no sistema.
- **Página de Cadastro de Livros:** Adicione novos livros com título, autor, categoria, status e data de publicação.
- **Página de Edição de Livros:** Editar os livros já cadastrados.
- **Sistema de Busca:** Procure livros por título, autor, categoria ou status.

### Estrutura do Projeto

A estrutura básica do projeto está organizada da seguinte forma:

```
biblioteca_virtual/
│
├── biblioteca_virtual/               # Diretório do projeto principal
│   ├── settings.py                   # Configurações do Django
│   ├── urls.py                       # URL routes do projeto
│   ├── wsgi.py                       # Configuração para deploy
│   └── asgi.py                       # Configuração para deploy assíncrono
│
├── livros/                           # App onde os livros são gerenciados
│   ├── migrations/                   # Armazena migrações de banco de dados
│   ├── models.py                     # Definição do modelo Livro
│   ├── views.py                      # Funções de visualização
│   ├── urls.py                       # URLs específicas do app livros
│   └── templates/                    # Templates HTML para as páginas
│       ├── livros/
│           ├── livro_list.html       # Listagem de livros
│           ├── livro_form.html       # Formulário de cadastro/edição
│           ├── livro_detail.html     # Detalhes do livro
│           ├── livro_confirm_delete.html # Página de confirmação de exclusão
```

### Diagrama de Classe

O Diagrama de Classe do sistema pode ser descrito da seguinte forma:

- **`Livro`** (Classe):
  - **Propriedades:** `titulo`, `autor`, `categoria`, `idioma`, `status`, `publicado_em`
  - **Métodos:** `__str__` (para representação do livro)

- **`Usuario`** (Classe embutida do Django):
  - Já é fornecida automaticamente pelo Django.

### Diagrama de Caso de Uso

Os **principais casos de uso** incluem:
1. **Usuário comum:**
   - Adicionar livro à biblioteca.
   - Editar ou excluir livros da biblioteca.
   - Buscar livros.
   - Visualizar detalhes do livro.
### Notificações

O sistema pode incluir notificações simples (via e-mail ou interface) para lembrar os usuários de livros que estão em sua **"wishlist"** ou para notificar trocas pendentes de livros.

## Conclusão

Este é um sistema simples, porém funcional, de gerenciamento de livros com funcionalidades extras como busca e troca de livros. O sistema pode ser estendido com novas funcionalidades, como um sistema de login de usuários, integração com APIs de recomendação de livros, entre outras.
