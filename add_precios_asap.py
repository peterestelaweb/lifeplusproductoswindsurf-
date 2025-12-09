#!/usr/bin/env python3

import re

# Cargar la base de datos de productos
exec(open('completar_categorias.py').read())

# Leer el catálogo existente
with open('catalogo_final_precios_dobles.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Crear un diccionario de códigos a precios ASAP
prices_asap = {}
for category, products in products_by_category.items():
    for product in products:
        code = product["code"]
        price_asap = product.get("price_asap", "")
        if price_asap:
            prices_asap[code] = price_asap

print(f"Encontrados {len(prices_asap)} productos con precios ASAP")

# Función para actualizar un producto específico
def update_product_price(match):
    product_html = match.group(0)
    code_match = re.search(r'<span class="product-code">(\d+)</span>', product_html)

    if code_match:
        code = code_match.group(1)
        price_match = re.search(r'<span class="product-price">([^<]+)</span>', product_html)

        if price_match and code in prices_asap:
            original_price = price_match.group(1)
            asap_price = prices_asap[code]

            # Reemplazar el precio individual por un contenedor con ambos precios
            new_prices = f'''<div class="product-prices">
                            <span class="product-price">{original_price}</span>
                            <span class="product-price-asap">{asap_price}</span>
                        </div>'''

            updated_product = product_html.replace(price_match.group(0), new_prices)
            return updated_product

    return product_html

# Buscar y reemplazar todas las tarjetas de producto
product_pattern = r'<div class="product-card">.*?</div>\s*</a>\s*</div>'
updated_content = re.sub(product_pattern, update_product_price, content, flags=re.DOTALL)

# Añadir CSS para precios dobles
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
style_end = updated_content.find('</style>')
if style_end != -1:
    updated_content = updated_content[:style_end] + css_addition + updated_content[style_end:]

# Escribir el archivo actualizado
with open('catalogo_final_precios_dobles.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("¡Catálogo con precios dobles actualizado exitosamente!")

# Verificar algunos productos
print("\nVerificación de productos actualizados:")
import random
sample_codes = random.sample(list(prices_asap.keys()), min(5, len(prices_asap)))
for code in sample_codes:
    print(f"Producto {code}: Normal -> ASAP {prices_asap[code]}")