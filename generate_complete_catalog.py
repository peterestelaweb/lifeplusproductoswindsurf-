#!/usr/bin/env python3

# Importar el diccionario de productos completo
exec(open('completar_categorias.py').read())

def get_category_name(category):
    names = {
        'nutricionales': 'Nutricionales',
        'proteinas': 'Proteínas',
        'deportiva': 'Deporte',
        'control-peso': 'Control de Peso',
        'packs': 'Packs',
        'superfoods': 'Superfoods',
        'forever-young': 'Forever Young',
        'personal': 'Personal',
        'accesorios': 'Accesorios',
        'agua': 'Agua'
    }
    return names.get(category, category.title())

def get_category_icon(category):
    icons = {
        'nutricionales': 'fa-pills',
        'proteinas': 'fa-dumbbell',
        'deportiva': 'fa-running',
        'control-peso': 'fa-weight',
        'packs': 'fa-box',
        'superfoods': 'fa-leaf',
        'forever-young': 'fa-hourglass-half',
        'personal': 'fa-user',
        'accesorios': 'fa-shopping-bag',
        'agua': 'fa-tint'
    }
    return icons.get(category, 'fa-cube')

def generate_product_html(product):
    code = product["code"]
    name = product["name"]
    price = product["price"]
    price_asap = product.get("price_asap", "")
    format_info = product["format"]

    # Generate clean URL for the link
    clean_name = name.lower()
    clean_name = clean_name.replace("®", "").replace("™", "").replace("&", "and")
    clean_name = clean_name.replace(" – ", "-").replace(": ", "-").replace(".", "").replace("(", "").replace(")", "")
    clean_name = clean_name.replace(" ", "-")
    clean_name = clean_name.replace("--", "-")
    # Handle special characters
    clean_name = clean_name.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    clean_name = clean_name.replace("ñ", "n").replace("ü", "u")

    buy_url = f"https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/{code}/{clean_name}"

    # Placeholder for images
    placeholder_text = name.split()[0][:8] if len(name.split()[0]) > 8 else name.split()[0]

    # Generate price HTML with both prices
    if price_asap:
        price_html = f'''<div class="product-prices">
                            <span class="product-price">{price}</span>
                            <span class="product-price-asap">{price_asap}</span>
                        </div>'''
    else:
        price_html = f'''<span class="product-price">{price}</span>'''

    return f'''                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_{code}_1@2x.jpg"
                                 alt="{name}"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=&quot;http://www.w3.org/2000/svg&quot; width=&quot;80&quot; height=&quot;80&quot; viewBox=&quot;0 0 80 80&quot;><rect width=&quot;80&quot; height=&quot;80&quot; fill=&quot;%23f0f0f0&quot;/><text x=&quot;40&quot; y=&quot;40&quot; text-anchor=&quot;middle&quot; dy=&quot;0.3em&quot; font-family=&quot;Arial&quot; font-size=&quot;10&quot; fill=&quot;%23666&quot;>{placeholder_text}</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">{code}</span>
                            {price_html}
                        </div>
                        <h3 class="product-name">{name}</h3>
                        <p class="product-format">{format_info}</p>
                        <a href="{buy_url}" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>'''

# Read the base template with contact functionality
with open('catalogo_lifeplus_con_contacto.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# Generate all sections
sections_html = ""

total_products = 0
for category, products in products_by_category.items():
    if products:  # Solo generar secciones que tienen productos
        total_products += len(products)
        section_html = f'''            <!-- Sección {get_category_name(category)} -->
            <div id="{category}" class="category-section">
                <div class="category-header">
                    <h2 class="category-title"><i class="fas fa-{get_category_icon(category)}"></i> {get_category_name(category)}</h2>
                    <p>{len(products)} productos disponibles</p>
                </div>

                <div class="products-grid">
'''

        for product in products:
            section_html += generate_product_html(product) + '\n'

        section_html += '''                </div>
            </div>

'''
        sections_html += section_html

print(f"Generando catálogo con {total_products} productos totales...")

# Find where to insert the sections in the template (after welcome section)
welcome_end = template_content.find('<div id="nutricionales"')
if welcome_end == -1:
    welcome_end = template_content.find('<div class="contact-section">')

if welcome_end != -1:
    # Insert all sections before the contact section
    before_sections = template_content[:welcome_end]
    after_sections = template_content[welcome_end:]

    # Find the actual start of first section to replace
    first_section_start = before_sections.rfind('<div id="')
    if first_section_start != -1:
        before_sections = before_sections[:first_section_start]

    final_content = before_sections + sections_html + after_sections

    # Add CSS for dual prices if not already present
    if '.product-prices' not in final_content:
        dual_prices_css = '''
        .product-prices {
            display: flex;
            flex-direction: row;
            gap: 4px;
            align-items: center;
            white-space: nowrap;
            line-height: 1.1;
        }

        .product-price {
            font-weight: 700;
            color: var(--primary-green);
            font-size: 0.8rem;
        }

        .product-price-asap {
            font-weight: 600;
            color: var(--secondary-green);
            font-size: 0.7rem;
        }
        '''

        # Insert CSS before the closing </style> tag
        style_end = final_content.find('</style>')
        if style_end != -1:
            final_content = final_content[:style_end] + dual_prices_css + final_content[style_end:]

    # Write the complete catalog
    with open('catalogo_lifeplus_completo_precios_dobles.html', 'w', encoding='utf-8') as f:
        f.write(final_content)

    print("¡Catálogo completo generado exitosamente!")
    print("Archivo creado: catalogo_lifeplus_completo_precios_dobles.html")
    print(f"Total productos: {total_products}")

    # Count products with ASAP prices
    with_asap_count = sum(1 for category in products_by_category.values()
                          for product in category if 'price_asap' in product)
    print(f"Productos con precios ASAP: {with_asap_count}/{total_products}")
else:
    print("Error: No se pudo encontrar el punto de inserción en el template")