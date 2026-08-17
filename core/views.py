from django.http import Http404
from django.shortcuts import render

from .data import PRODUCTS, get_product


def index(request):
    """Pagina inicial da MOAB - Macaco de Auxilio a Baloes."""
    context = {"products": PRODUCTS, "footer_products": PRODUCTS}
    return render(request, "core/index.html", context)


def product_detail(request, slug):
    """Pagina de compra de um produto isolado."""
    product = get_product(slug)
    if product is None:
        raise Http404("Produto não encontrado")

    outros = [p for p in PRODUCTS if p["slug"] != slug][:3]
    context = {
        "product": product,
        "outros_produtos": outros,
        "footer_products": PRODUCTS,
    }
    return render(request, "core/product_detail.html", context)
