"""
Catálogo de produtos da MOAB.

Por enquanto os produtos vivem aqui como dados em Python (sem banco de dados
e sem painel de admin pra edição). Quando o projeto evoluir pra ter carrinho
e conta de usuário, esse catálogo vira um Model de verdade.
"""

PRODUCTS = [
    {
        "slug": "macaco-atirador",
        "name": "Macaco Atirador",
        "tagline": "Lança dardos de espuma a até 6 metros de distância.",
        "eyebrow": "Linha de ação",
        "price": "R$ 129,90",
        "badge": "Tiro certeiro",
        "badge_class": "badge-hot",
        "image": "core/images/atirador.jpg",
        "alt": "Macaco Atirador MOAB lançando dardo de espuma",
        "description": (
            "Aperte o botão da base e veja os dardos de espuma voarem a até 6 metros "
            "de distância. Ideal pra guerra de dardos em família, pra desafiar os amigos "
            "ou simplesmente pra afastar visita chata sem machucar ninguém."
        ),
        "specs": [
            ("Alcance", "até 6 metros"),
            ("Material dos dardos", "espuma macia e atóxica"),
            ("Idade recomendada", "+3 anos"),
            ("Ativação", "botão na base"),
        ],
        "includes": ["1 Macaco Atirador", "3 dardos de espuma"],
        "has_skins": False,
    },
    {
        "slug": "macaco-domador",
        "name": "Pat Fusty",
        "tagline": "Esmaga balões de verdade com as próprias mãos.",
        "eyebrow": "Linha domador",
        "price": "R$ 249,90",
        "badge": "Mais vendido",
        "badge_class": "badge-hot",
        "image": "core/images/domador-classico.jpg",
        "alt": "Pat Fusty MOAB esmagando balão",
        "description": (
            "+60cm de altura e cara fechada. Insira a moeda, leve um balão de verdade "
            "até ele e assista à esmagada com as próprias mãos. Feito pra aguentar "
            "muita ação e desafiar todo mundo na festa."
        ),
        "specs": [
            ("Altura", "+60 cm"),
            ("Ativação", "por moeda"),
            ("Idade recomendada", "+6 anos"),
            ("Material", "resistente a impacto"),
        ],
        "includes": ["1 Pat Fusty", "Base de moedas"],
        "has_skins": False,
    },
    {
        "slug": "pat-fusty-domador",
        "name": "Pat Fusty Domador",
        "tagline": "Edição especial: a mesma esmagada, com muito mais drama.",
        "eyebrow": "Edição especial",
        "price": "R$ 279,90",
        "badge": "Edição especial",
        "badge_class": "badge-new",
        "image": "core/images/domador-fusty.jpg",
        "alt": "Pat Fusty Domador MOAB esmagando balão",
        "description": (
            "A versão pedra do Domador: olhos de brasa, garras afiadas e o mesmo talento "
            "pra estourar balão de verdade. Pra quem acha que o clássico é fraquinho demais."
        ),
        "specs": [
            ("Altura", "+60 cm"),
            ("Ativação", "por moeda"),
            ("Idade recomendada", "+6 anos"),
            ("Edição", "tiragem especial"),
        ],
        "includes": ["1 Pat Fusty Domador", "Base de moedas"],
        "has_skins": True,
        "skins": [
            {
                "key": "classico",
                "name": "Pat Fusty Pedra",
                "desc": (
                    "A versão pedra original: olhos de brasa, garras afiadas e o mesmo "
                    "talento pra estourar balão de verdade."
                ),
                "image": "core/images/domador-fusty.jpg",
                "alt": "Pat Fusty Domador MOAB, versão pedra clássica",
            },
            {
                "key": "donkey-kong",
                "name": "Edição Donkey Kong",
                "desc": (
                    "Lançamento próprio da MOAB em parceria com a Nintendo"
                    "sem vínculo com nenhuma outra marca."
                ),
                "image": "core/images/donkey-kong-fusty.jpg",
                "alt": "Pat Fusty Domador MOAB, Edição Donkey Kong — imagem a ser adicionada",
            },
        ],
    },
    {
        "slug": "macaco-fogueteiro",
        "name": "Macaco Fogueteiro",
        "tagline": "Lança fogos de baixa intensidade, show de luzes garantido.",
        "eyebrow": "Linha festa",
        "price": "R$ 179,90",
        "badge": "Novo",
        "badge_class": "badge-new",
        "image": "core/images/fogueteiro.jpg",
        "alt": "Macaco Fogueteiro MOAB lançando fogos de artifício",
        "description": (
            "Insira a moeda, prepare o lançamento e aperte o botão: fogos de baixa "
            "intensidade que iluminam a festa sem machucar ninguém. Perfeito pra "
            "comemorações, aniversários ou uma terça-feira que precisava de brilho."
        ),
        "specs": [
            ("Altura", "+60 cm"),
            ("Idade recomendada", "+4 anos"),
            ("Emissão de fumaça", "baixa"),
            ("Ativação", "por moeda"),
        ],
        "includes": [
            "1 Macaco Fogueteiro",
            "6 foguetes coloridos",
            "1 base eletrônica",
            "1 manual de instruções",
        ],
        "has_skins": False,
    },
    {
        "slug": "macaco-enche-baloes",
        "name": "Macaco Enche-Balões",
        "tagline": "Enche balões de verdade só de mexer o braço.",
        "eyebrow": "Linha festa",
        "price": "R$ 159,90",
        "badge": "Armazena 12 balões",
        "badge_class": "badge-new",
        "image": "core/images/enche-baloes.jpg",
        "alt": "Macaco Enche-Balões MOAB inflando um balão azul",
        "description": (
            "Encaixe o balão no bico do inflador, movimente o braço do macaco pra baixo "
            "e pronto: o mecanismo enche o balão automaticamente. Guarda até 12 balões "
            "dentro da própria base, de vários tamanhos e cores, prontos pra festa."
        ),
        "specs": [
            ("Altura", "30 cm"),
            ("Armazenamento interno", "até 12 balões"),
            ("Idade recomendada", "+3 anos"),
            ("Ativação", "braço manual"),
        ],
        "includes": [
            "1 Macaco Enche-Balões",
            "12 balões",
            "1 base",
            "1 manual de instruções",
        ],
        "has_skins": False,
    },
    {
        "slug": "tack-zone-x5",
        "name": "Tack Zone X-5",
        "tagline": "Robô aspirador inteligente com 3 skins pra escolher.",
        "eyebrow": "Linha casa",
        "price": "R$ 399,90",
        "badge": "3 skins",
        "badge_class": "badge-skins",
        "image": "core/images/tackzone-zen.jpg",
        "alt": "Tack Zone X-5 robô aspirador MOAB",
        "description": (
            "Sucção 360°, navegação inteligente e retorno automático pra base — e ainda "
            "vem com um macaco sentado meditando em cima. Escolha entre monge, sultão "
            "ou gênio: a mesma faxina, três personalidades diferentes."
        ),
        "specs": [
            ("Sucção", "360°"),
            ("Bateria", "até 120 minutos"),
            ("Altura", "7,5 cm (ultra fino)"),
            ("Retorno à base", "automático"),
        ],
        "includes": ["1 Tack Zone X-5", "1 base de recarga", "1 manual de instruções"],
        "has_skins": True,
        "skins": [
            {
                "key": "zen",
                "name": "Monge Zen",
                "desc": (
                    "Aspira em silêncio, medita em movimento. Roxo e rosa, pra quem "
                    "gosta de limpar com paz interior."
                ),
                "image": "core/images/tackzone-zen.jpg",
                "alt": "Tack Zone X-5 skin Monge Zen",
            },
            {
                "key": "sultao",
                "name": "Sultão Real",
                "desc": (
                    "Realeza que limpa embaixo do sofá. Branco e dourado, pra quem não "
                    "abre mão do luxo nem na faxina."
                ),
                "image": "core/images/tackzone-sultao.jpg",
                "alt": "Tack Zone X-5 skin Sultão Real",
            },
            {
                "key": "genio",
                "name": "Gênio Azul",
                "desc": (
                    "Três desejos: menos pó, menos migalha, menos pelo de gato. Todos "
                    "concedidos, sem lâmpada nenhuma."
                ),
                "image": "core/images/tackzone-genio.jpg",
                "alt": "Tack Zone X-5 skin Gênio Azul",
            },
        ],
    },
]


def get_product(slug):
    """Retorna o produto pelo slug, ou None se não existir."""
    for product in PRODUCTS:
        if product["slug"] == slug:
            return product
    return None
