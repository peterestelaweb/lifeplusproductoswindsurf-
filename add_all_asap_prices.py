#!/usr/bin/env python3

# Importar la base de datos actual
exec(open('completar_categorias.py').read())

# Lista de productos que necesitan precios ASAP (basado en el análisis)
products_missing_asap = [
    # PACKS (6 productos)
    {"category": "packs", "code": "3592", "name": "Hydration Pack", "price": "€439.25"},
    {"category": "packs", "code": "3593", "name": "Complete Pack", "price": "€576.25"},
    {"category": "packs", "code": "3570", "name": "Weight Loss Kit", "price": "€69.75"},
    {"category": "packs", "code": "3571", "name": "Energy Kit", "price": "€79.75"},
    {"category": "packs", "code": "3572", "name": "Women's Kit", "price": "€49.50"},
    {"category": "packs", "code": "3573", "name": "Men's Kit", "price": "€50.00"},

    # PROTEÍNAS (4 productos)
    {"category": "proteinas", "code": "3530", "name": "Lifeplus Triple Protein Shake: Chocolate", "price": "€87.75"},
    {"category": "proteinas", "code": "3547", "name": "Lifeplus Triple Protein Shake: Chocolate (sin edulcorante)", "price": "€87.75"},
    {"category": "proteinas", "code": "3531", "name": "Lifeplus Triple Protein Shake: Vanilla", "price": "€87.75"},
    {"category": "proteinas", "code": "3548", "name": "Lifeplus Triple Protein Shake: Vanilla (sin edulcorante)", "price": "€87.75"},

    # DEPORTE (15 productos)
    {"category": "deporte", "code": "2850", "name": "Rehydrate", "price": "€28.50"},
    {"category": "deporte", "code": "3485", "name": "Recover", "price": "€48.50"},
    {"category": "deporte", "code": "3515", "name": "Be Focused", "price": "€73.75"},
    {"category": "deporte", "code": "3463", "name": "Be Sharp", "price": "€75.00"},
    {"category": "deporte", "code": "3520", "name": "Be Focused (30ct)", "price": "€52.00"},
    {"category": "deporte", "code": "3521", "name": "Be Sharp (30ct)", "price": "€73.75"},
    {"category": "deporte", "code": "3533", "name": "Be Recharged", "price": "€55.00"},
    {"category": "deporte", "code": "3534", "name": "Hydrate", "price": "€42.25"},
    {"category": "deporte", "code": "3537", "name": "Be Strong", "price": "€64.25"},
    {"category": "deporte", "code": "3536", "name": "Electrolyte", "price": "€24.25"},
    {"category": "deporte", "code": "3532", "name": "Be Fueled", "price": "€79.25"},
    {"category": "deporte", "code": "3527", "name": "Be Balanced", "price": "€52.75"},
    {"category": "deporte", "code": "3535", "name": "Be Fueled (30ct)", "price": "€147.50"},
    {"category": "deporte", "code": "3539", "name": "Hydrate Plus", "price": "€41.25"},

    # SUPERFOODS (3 productos)
    {"category": "superfoods", "code": "3540", "name": "Be Recharged Sachet", "price": "€9.75"},
    {"category": "superfoods", "code": "3541", "name": "Be Focused (Chocolate)", "price": "€87.75"},
    {"category": "superfoods", "code": "3542", "name": "Be Focused (Vanilla)", "price": "€87.75"},

    # FOREVER YOUNG (7 productos)
    {"category": "forever-young", "code": "3543", "name": "Be Sharp (Chocolate)", "price": "€87.75"},
    {"category": "forever-young", "code": "3544", "name": "Be Sharp (Vanilla)", "price": "€87.75"},
    {"category": "forever-young", "code": "3546", "name": "Be Sustained (Chocolate)", "price": "€93.50"},
    {"category": "forever-young", "code": "3547", "name": "Be Sustained (Vanilla)", "price": "€93.50"},
    {"category": "forever-young", "code": "3548", "name": "Be Strong (Chocolate)", "price": "€37.25"},
    {"category": "forever-young", "code": "3549", "name": "Be Strong (Vanilla)", "price": "€37.25"},
    {"category": "forever-young", "code": "3550", "name": "Be Fueled (Chocolate)", "price": "€82.25"},

    # PERSONAL (8 productos)
    {"category": "personal", "code": "3551", "name": "Be Fueled (Vanilla)", "price": "€82.25"},
    {"category": "personal", "code": "3552", "name": "Be Fueled (30ct, Chocolate)", "price": "€95.75"},
    {"category": "personal", "code": "3553", "name": "Be Fueled (30ct, Vanilla)", "price": "€95.75"},
    {"category": "personal", "code": "3554", "name": "Be Balanced (Chocolate)", "price": "€83.50"},
    {"category": "personal", "code": "3555", "name": "Be Balanced (Vanilla)", "price": "€83.50"},
    {"category": "personal", "code": "3556", "name": "Be Balanced (30ct, Chocolate)", "price": "€102.25"},
    {"category": "personal", "code": "3557", "name": "Be Balanced (30ct, Vanilla)", "price": "€102.25"},
    {"category": "personal", "code": "3558", "name": "Be Focused (Sugar-Free)", "price": "€84.75"},

    # ACCESORIOS (4 productos)
    {"category": "accesorios", "code": "6074", "name": "Botella mezcladora", "price": "€4.00"},
    {"category": "accesorios", "code": "7890", "name": "Cinta para medir", "price": "€10.75"},
    {"category": "accesorios", "code": "2178", "name": "Juego de cucharas de madera", "price": "€23.00"},
    {"category": "accesorios", "code": "4619", "name": "PH Plus tiras de test", "price": "€9.75"},

    # AGUA (2 productos)
    {"category": "agua", "code": "1496", "name": "Modelo de encimero pequeño", "price": "€439.25"},
    {"category": "agua", "code": "1497", "name": "Modelo bajo el fregadero pequeño", "price": "€576.25"},

    # NUTRICIONALES productos faltantes (14 productos)
    {"category": "nutricionales", "code": "3440", "name": "Lifeplus Enerxan®", "price": "€28.50"},
    {"category": "nutricionales", "code": "3408", "name": "X Cell", "price": "€73.75"},
    {"category": "nutricionales", "code": "3406", "name": "X Cell+", "price": "€75.00"},
    {"category": "nutricionales", "code": "3417", "name": "Somazyme", "price": "€52.00"},
    {"category": "nutricionales", "code": "3407", "name": "FY® Skin Formula", "price": "€73.75"},
    {"category": "nutricionales", "code": "3436", "name": "Fusions Red", "price": "€43.50"},
    {"category": "nutricionales", "code": "3472", "name": "Vita Saurus®", "price": "€55.00"},
    {"category": "nutricionales", "code": "3433", "name": "Yummies", "price": "€42.25"},
    {"category": "nutricionales", "code": "3428", "name": "Support Tabs Plus", "price": "€64.25"},
    {"category": "nutricionales", "code": "3443", "name": "Kompakt Plus", "price": "€24.25"},
    {"category": "nutricionales", "code": "3842", "name": "Key Tonic®", "price": "€79.25"},
    {"category": "nutricionales", "code": "3418", "name": "Cogelin®", "price": "€52.75"},
    {"category": "nutricionales", "code": "3409", "name": "Lifeplus Discovery®", "price": "€147.50"},
    {"category": "nutricionales", "code": "3446", "name": "PH Plus", "price": "€41.25"}
]

def calculate_asap_price(normal_price_str):
    """Calcular precio ASAP con 5.5% de descuento"""
    import re
    match = re.search(r'€(\d+\.?\d*)', normal_price_str)
    if match:
        normal_price = float(match.group(1))
        asap_price = normal_price * 0.945
        return f"€{asap_price:.2f}"
    return None

# Contador de productos actualizados
updated_count = 0

# Leer el archivo actual
with open('completar_categorias.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Actualizar cada producto que falta ASAP price
for product_info in products_missing_asap:
    category = product_info["category"]
    code = product_info["code"]
    price = product_info["price"]
    asap_price = calculate_asap_price(price)

    if asap_price:
        # Buscar el producto en la categoría específica
        if category in products_by_category:
            for i, product in enumerate(products_by_category[category]):
                if product["code"] == code and "price_asap" not in product:
                    # Añadir el precio ASAP
                    products_by_category[category][i]["price_asap"] = asap_price
                    updated_count += 1
                    print(f"✓ Actualizado: {category} - {code} - {product['name']} - {asap_price}")

print(f"\n¡Total de productos actualizados: {updated_count}")

# Guardar el archivo actualizado
import json
with open('completar_categorias.py', 'w', encoding='utf-8') as f:
    f.write('#!/usr/bin/env python3\n\n')
    f.write('# Productos completos del catálogo LifePlus organizados por categorías\n\n')
    f.write('products_by_category = {\n')

    for category, products in products_by_category.items():
        f.write(f"    '{category}': [\n")
        for product in products:
            f.write(f'        {json.dumps(product, ensure_ascii=False)},\n')
        f.write('    ],\n\n')

    f.write('}\n\n')

print(f"Archivo 'completar_categorias.py' actualizado con {updated_count} nuevos precios ASAP")