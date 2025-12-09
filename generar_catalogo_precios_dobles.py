#!/usr/bin/env python3

# Importar el diccionario de productos actualizado
exec(open('completar_categorias.py').read())

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
    price_html = f'''<span class="product-price">{price}</span>
                            <span class="product-price-asap">{price_asap}</span>''' if price_asap else f'''<span class="product-price">{price}</span>'''

    return f'''                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_{code}_1@2x.jpg"
                                 alt="{name}"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>{placeholder_text}</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">{code}</span>
                            <div class="product-prices">
                                {price_html}
                            </div>
                        </div>
                        <h3 class="product-name">{name}</h3>
                        <p class="product-format">{format_info}</p>
                        <a href="{buy_url}" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>'''

def get_category_name(category):
    names = {
        'nutricionales': 'Nutricionales',
        'deporte': 'Deporte',
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
        'deporte': 'fa-dumbbell',
        'control-peso': 'fa-weight',
        'packs': 'fa-box',
        'superfoods': 'fa-leaf',
        'forever-young': 'fa-hourglass-half',
        'personal': 'fa-user',
        'accesorios': 'fa-shopping-bag',
        'agua': 'fa-tint'
    }
    return icons.get(category, 'fa-cube')

# Read the base template
with open('catalogo_lifeplus_con_contacto.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# Generate all sections
sections_html = ""

for category, products in products_by_category.items():
    if products:  # Solo generar secciones que tienen productos
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

# Replace the sections in the template
# First find the start and end of existing product sections
import re

# Find where the product sections start (after the welcome section)
pattern = r'(<div id="welcome".*?</div>\s*)(.*?)(<div id="nutricionales")'
match = re.search(pattern, template_content, re.DOTALL)

if match:
    # Keep the welcome section and replace everything after it with our new sections
    welcome_section = match.group(1)
    new_content = welcome_section + sections_html + match.group(3)

    # Now find the rest of the template from the start of nutricionales
    pattern2 = r'(<div id="nutricionales".*?)(<div class="contact-section">.*?</html>)'
    match2 = re.search(pattern2, template_content, re.DOTALL)

    if match2:
        # Get the rest of the template (including all existing sections that we'll replace)
        rest_of_template = match2.group(2)
        # Remove the old sections from the template by finding the contact section
        contact_start = template_content.find('<div class="contact-section">')
        if contact_start != -1:
            rest_of_template = template_content[contact_start:]

        # Combine everything
        final_content = new_content + rest_of_template

        # Add CSS for dual prices
        dual_prices_css = '''
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

        # Insert the CSS before the closing </style> tag
        style_end = final_content.find('</style>')
        if style_end != -1:
            final_content = final_content[:style_end] + dual_prices_css + final_content[style_end:]

        # Write the new catalog
        with open('catalogo_lifeplus_precios_dobles.html', 'w', encoding='utf-8') as f:
            f.write(final_content)

        print("¡Catálogo con precios dobles generado exitosamente!")
        print(f"Archivo creado: catalogo_lifeplus_precios_dobles.html")
    else:
        print("Error: No se encontró la estructura del template")
else:
    print("Error: No se encontró la sección de bienvenida")