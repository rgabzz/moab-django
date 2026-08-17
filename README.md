# MOAB — Macaco de Auxílio a Balões (Django)

Site institucional da MOAB, agora como projeto Django. Mesmo conteúdo e visual da versão em
HTML puro, só que servido por uma view Django com template e static files.

## Estrutura da pasta

```
moab-django/
├── manage.py
├── requirements.txt
├── moab_project/            → configuração do projeto
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── core/                     → app com a página inicial e as páginas de produto
    ├── data.py                 → catálogo de produtos (lista em Python, ainda sem banco de dados)
    ├── views.py                → views "index" e "product_detail"
    ├── urls.py                 → rotas do app
    ├── templates/core/
    │   ├── base.html             → cabeçalho, rodapé e blocos compartilhados
    │   ├── index.html             → template da home
    │   └── product_detail.html    → template da página de cada produto
    └── static/core/
        ├── css/style.css
        ├── js/main.js           → lógica do seletor de skins (reutilizada na home e no produto)
        └── images/               → fotos dos produtos
```

## Catálogo de produtos

Os 6 produtos (Macaco Atirador, Macaco Domador, Pat Fusty Domador, Macaco Fogueteiro, Macaco
Enche-Balões e Tack Zone X-5) vivem como uma lista de dicionários em `core/data.py` — ainda não
tem banco de dados nem painel de admin pra edição, só código Python mesmo. Cada produto tem uma
página própria em `/produto/<slug>/`, acessível clicando em qualquer card da home.

O botão "Comprar agora" nessas páginas está desabilitado de propósito: ainda não existe carrinho
nem conta de usuário no projeto, então ele só serve pra visualizar os detalhes do produto por
enquanto.

## Como rodar

Requer **Python 3.10+**.

```bash
cd moab-django

# 1. criar e ativar um ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. instalar as dependências (requirements)
pip install -r requirements.txt

# 3. rodar as migrações (cria o banco sqlite local)
python manage.py migrate

# 4. subir o servidor de desenvolvimento
python manage.py runserver
```

O site abre em **http://127.0.0.1:8000/**.

## Rotas

| URL      | View            | Descrição            |
|----------|-----------------|-----------------------|
| `/`      | `core.views.index` | Página inicial da MOAB |
| `/produto/<slug>/` | `core.views.product_detail` | Página de compra de um produto isolado |
| `/admin/`| Django admin      | Painel administrativo padrão |

## Observação importante

As fotos de produto em `core/static/core/images/` foram geradas com a marca "Bloons TD6"
visível, que pertence a outro jogo (Ninja Kiwi). Antes de apresentar o projeto, vale trocar
essas imagens ou cobrir o logo, pra não usar marca de terceiros no material da MOAB.

## Próximos passos sugeridos

- Criar uma página/rota separada (ex: `/okr/`) com o **Objetivo**, os **Resultados-Chave** e as
  **estratégias** do OKR, pra fechar a atividade completa.
- Trocar preços e textos de exemplo pelos valores definidos pelo grupo.
- Quando fizer sentido, migrar `core/data.py` pra um Model de verdade (banco de dados) e
  implementar carrinho de compras e conta de usuário.
- Se quiser deploy (Render, Railway, PythonAnywhere etc.), lembrar de configurar
  `ALLOWED_HOSTS`, `DEBUG = False` e rodar `python manage.py collectstatic`.
