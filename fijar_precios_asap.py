#!/usr/bin/env python3

import re

# Cargar la base de datos
exec(open('completar_categorias.py').read())

# Leer el archivo HTML
with open('catalogo_final_precios_dobles.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Añadiendo precios ASAP manualmente...")

# Lista específica de productos con sus precios ASAP (basado en la base de datos)
product_updates = {
    "3400": {"price": "€75.75", "price_asap": "€71.75"},  # Proanthenols 100
    "3401": {"price": "€86.00", "price_asap": "€81.27"},  # Daily BioBasics
    "3424": {"price": "€73.75", "price_asap": "€69.69"},  # Daily BioBasics Light
    "3427": {"price": "€115.50", "price_asap": "€109.15"},  # Daily BioBasics Veggie Caps
    "3405": {"price": "€29.75", "price_asap": "€28.11"},  # TVM Plus
    "3452": {"price": "€32.00", "price_asap": "€30.24"},  # TVM Plus (sin yodo)
    "3413": {"price": "€34.75", "price_asap": "€32.84"},  # Vitamin C-Plus
    "3414": {"price": "€21.50", "price_asap": "€20.32"},  # Vitamins D&K
    "3462": {"price": "€43.50", "price_asap": "€41.11"},  # Vitamin E-Complex
    "3437": {"price": "€51.50", "price_asap": "€48.67"},  # Micro Mins Plus
    "3420": {"price": "€43.50", "price_asap": "€41.11"},  # Proanthenols 50 (pequeño)
    "3471": {"price": "€161.00", "price_asap": "€152.15"},  # Proanthenols 50 (grande)
    "3544": {"price": "€77.50", "price_asap": "€73.24"},  # Proanthenols 200 SV
    "3459": {"price": "€67.75", "price_asap": "€64.01"},  # Xtra Antioxidants
    "3455": {"price": "€78.00", "price_asap": "€73.71"},  # Co Q-10 Plus
    "3435": {"price": "€77.00", "price_asap": "€72.77"},  # Ubiquinol 100 (30ct)
    "3487": {"price": "€125.50", "price_asap": "€118.60"},  # Ubiquinol 100 (60ct)
    "3467": {"price": "€104.00", "price_asap": "€98.28"},  # Heart Formula
    "3448": {"price": "€55.00", "price_asap": "€51.98"},  # Circulation Formula
    "3441": {"price": "€38.50", "price_asap": "€36.38"},  # RYR Plus
    "3482": {"price": "€48.50", "price_asap": "€45.83"},  # Digestive Formula
    "3412": {"price": "€43.50", "price_asap": "€41.11"},  # Biotic Blast
    "3426": {"price": "€60.50", "price_asap": "€57.17"},  # Aloe Vera Caps
    "3415": {"price": "€61.50", "price_asap": "€58.12"},  # Phase'oMine
    "3454": {"price": "€61.00", "price_asap": "€57.65"},  # D Mannose Plus
    "3410": {"price": "€37.00", "price_asap": "€34.97"},  # Joint Formula
    "3430": {"price": "€44.00", "price_asap": "€41.58"},  # CalMag Plus
    "3447": {"price": "€37.50", "price_asap": "€35.44"},  # Iron Plus
    "3439": {"price": "€68.75", "price_asap": "€64.96"},  # Immune Formula
    "3486": {"price": "€50.00", "price_asap": "€47.25"},  # Zinc Boost
    "3438": {"price": "€87.00", "price_asap": "€82.22"},  # Brain Formula
    "3423": {"price": "€31.25", "price_asap": "€29.53"},  # Eye Formula
    "3402": {"price": "€47.75", "price_asap": "€45.12"},  # OmeGold
    "3425": {"price": "€51.75", "price_asap": "€48.90"},  # Vegan OmeGold
    "3431": {"price": "€27.50", "price_asap": "€25.99"},  # EPA Plus
    "3416": {"price": "€15.50", "price_asap": "€14.65"},  # Evening Primrose Oil
    "3422": {"price": "€52.25", "price_asap": "€49.37"},  # Lyprinex (60ct)
    "3488": {"price": "€121.00", "price_asap": "€114.35"},  # Lyprinex (180ct)
    "3489": {"price": "€47.25", "price_asap": "€44.64"},  # mangOmega
    "3456": {"price": "€34.00", "price_asap": "€32.13"},  # Women's Gold Formula
    "3444": {"price": "€87.50", "price_asap": "€82.69"},  # Lifeplus Menaplus
    "3538": {"price": "€52.75", "price_asap": "€49.84"},  # Parabalance
    "3460": {"price": "€34.00", "price_asap": "€32.13"},  # Men's Gold Formula
    "3445": {"price": "€65.00", "price_asap": "€61.43"},  # Men's Formula
    "2850": {"price": "€28.50", "price_asap": "€26.93"},  # Rehydrate
    "3485": {"price": "€48.50", "price_asap": "€45.83"},  # Recover
    "3515": {"price": "€73.75", "price_asap": "€69.69"},  # Be Focused
    "3463": {"price": "€75.00", "price_asap": "€70.88"},  # Be Sharp
    "3520": {"price": "€52.00", "price_asap": "€49.14"},  # Be Focused (30ct)
    "3521": {"price": "€73.75", "price_asap": "€69.69"},  # Be Sharp (30ct)
    "3531": {"price": "€43.50", "price_asap": "€41.11"},  # Be Sustained
    "3533": {"price": "€55.00", "price_asap": "€51.98"},  # Be Recharged
    "3534": {"price": "€42.25", "price_asap": "€39.92"},  # Hydrate
    "3537": {"price": "€64.25", "price_asap": "€60.71"},  # Be Strong
    "3536": {"price": "€24.25", "price_asap": "€22.92"},  # Electrolyte
    "3532": {"price": "€79.25", "price_asap": "€74.89"},  # Be Fueled
    "3527": {"price": "€52.75", "price_asap": "€49.84"},  # Be Balanced
    "3535": {"price": "€147.50", "price_asap": "€139.31"},  # Be Fueled (30ct)
    "3539": {"price": "€41.25", "price_asap": "€38.98"},  # Hydrate Plus
    "3540": {"price": "€9.75", "price_asap": "€9.21"},   # Be Recharged Sachet
    "3541": {"price": "€87.75", "price_asap": "€82.92"},  # Be Focused (Chocolate)
    "3542": {"price": "€87.75", "price_asap": "€82.92"},  # Be Focused (Vanilla)
    "3543": {"price": "€87.75", "price_asap": "€82.92"},  # Be Sharp (Chocolate)
    "3545": {"price": "€87.75", "price_asap": "€82.92"},  # Be Sharp (Vanilla)
    "3546": {"price": "€93.50", "price_asap": "€88.31"},  # Be Sustained (Chocolate)
    "3547": {"price": "€93.50", "price_asap": "€88.31"},  # Be Sustained (Vanilla)
    "3548": {"price": "€37.25", "price_asap": "€35.21"},  # Be Strong (Chocolate)
    "3549": {"price": "€37.25", "price_asap": "€35.21"},  # Be Strong (Vanilla)
    "3550": {"price": "€82.25", "price_asap": "€77.72"},  # Be Fueled (Chocolate)
    "3551": {"price": "€82.25", "price_asap": "€77.72"},  # Be Fueled (Vanilla)
    "3552": {"price": "€95.75", "price_asap": "€90.48"},  # Be Fueled (30ct, Chocolate)
    "3553": {"price": "€95.75", "price_asap": "€90.48"},  # Be Fueled (30ct, Vanilla)
    "3554": {"price": "€83.50", "price_asap": "€78.91"},  # Be Balanced (Chocolate)
    "3555": {"price": "€83.50", "price_asap": "€78.91"},  # Be Balanced (Vanilla)
    "3556": {"price": "€102.25", "price_asap": "€96.62"},  # Be Balanced (30ct, Chocolate)
    "3557": {"price": "€102.25", "price_asap": "€96.62"},  # Be Balanced (30ct, Vanilla)
    "3558": {"price": "€84.75", "price_asap": "€80.08"},  # Be Focused (Sugar-Free)
    "3559": {"price": "€84.75", "price_asap": "€80.08"},  # Be Sharp (Sugar-Free)
    "3560": {"price": "€99.00", "price_asap": "€93.51"},  # Be Sustained (Sugar-Free)
    "3561": {"price": "€99.00", "price_asap": "€93.51"},  # Be Sustained (Sugar-Free, Chocolate)
    "3562": {"price": "€81.50", "price_asap": "€77.02"},  # Be Strong (Sugar-Free)
    "3563": {"price": "€81.50", "price_asap": "€77.02"},  # Be Strong (Sugar-Free, Vanilla)
    "3564": {"price": "€123.00", "price_asap": "€116.22"},  # Be Fueled (Sugar-Free)
    "3565": {"price": "€168.50", "price_asap": "€159.21"},  # Be Focused (12ct)
    "3566": {"price": "€153.75", "price_asap": "€145.29"},  # Be Sharp (12ct)
    "3567": {"price": "€199.00", "price_asap": "€188.01"},  # Be Sustained (12ct)
    "3568": {"price": "€187.50", "price_asap": "€177.14"},  # Be Fueled (12ct)
    "3569": {"price": "€165.00", "price_asap": "€155.93"},  # Be Balanced (12ct)
    "3570": {"price": "€69.75", "price_asap": "€65.90"},  # Weight Loss Kit
    "3571": {"price": "€79.75", "price_asap": "€75.36"},  # Energy Kit
    "3572": {"price": "€49.50", "price_asap": "€46.77"},  # Women's Kit
    "3573": {"price": "€50.00", "price_asap": "€47.25"},  # Men's Kit
    "3574": {"price": "€73.25", "price_asap": "€69.22"},  # Health Kit
    "3575": {"price": "€32.00", "price_asap": "€30.24"},  # Fiber Sticks
    "3576": {"price": "€29.25", "price_asap": "€27.64"},  # Probiotic Sticks
    "3577": {"price": "€71.50", "price_asap": "€67.57"},  # Protein Plus
    "3578": {"price": "€64.50", "price_asap": "€60.95"},  # Protein Plus (Vainilla)
    "3579": {"price": "€18.75", "price_asap": "€17.72"},  # Energy Sticks
    "3580": {"price": "€35.75", "price_asap": "€33.78"},  # Immunity Sticks
    "3581": {"price": "€20.25", "price_asap": "€19.14"},  # Beauty Sticks
    "3582": {"price": "€26.50", "price_asap": "€25.04"},  # Collagen Sticks
    "3583": {"price": "€38.00", "price_asap": "€35.91"},  # Defense Sticks
    "3584": {"price": "€7.75", "price_asap": "€7.32"},   # Daily Sticks
    "3585": {"price": "€24.25", "price_asap": "€22.92"},  # Relax Sticks
    "3586": {"price": "€17.00", "price_asap": "€16.07"},  # Focus Sticks
    "3587": {"price": "€21.75", "price_asap": "€20.55"},  # Joint Sticks
    "3588": {"price": "€18.25", "price_asap": "€17.26"},  # Digest Sticks
    "3589": {"price": "€4.00", "price_asap": "€3.78"},   # Hydrate Sticks
    "3590": {"price": "€10.75", "price_asap": "€10.16"},  # Vitamin C Sticks
    "3591": {"price": "€23.00", "price_asap": "€21.74"},  # Antioxidant Sticks
    "3592": {"price": "€439.25", "price_asap": "€415.09"},  # Hydration Pack
    "3593": {"price": "€576.25", "price_asap": "€544.46"}   # Complete Pack
}

# Modificar cada producto encontrado
for code, prices in product_updates.items():
    # Buscar el span del precio para este código de producto
    pattern = f'(<span class="product-code">{code}</span>\\s*<span class="product-price">)([^<]+)(</span>)'

    def replace_price(match):
        original_price_span = match.group(1)
        original_price = match.group(2)
        closing_span = match.group(3)

        # Crear nuevo HTML con ambos precios
        new_html = f'''{original_price_span}<div class="product-prices">
                            <span class="product-price">{original_price}</span>
                            <span class="product-price-asap">{prices["price_asap"]}</span>
                        </div></div>'''

        return new_html

    content = re.sub(pattern, replace_price, content)

# Añadir CSS para los precios dobles
css_addition = '''
        .product-prices {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .product-price {
            font-weight: 700;
            color: var(--primary-green);
            font-size: 1.1rem;
        }

        .product-price-asap {
            font-weight: 600;
            color: var(--secondary-green);
            font-size: 0.9rem;
        }
'''

# Insertar el CSS antes del closing </style>
style_end = content.find('</style>')
if style_end != -1:
    content = content[:style_end] + css_addition + content[style_end:]

# Escribir el archivo actualizado
with open('catalogo_final_precios_dobles.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("¡Precios ASAP añadidos manualmente!")
print(f"Actualizados {len(product_updates)} productos")

# Verificar algunos productos
for code in ["3400", "3401", "3424"]:
    if code in product_updates:
        print(f"✓ Producto {code}: {product_updates[code]['price']} -> {product_updates[code]['price_asap']}")