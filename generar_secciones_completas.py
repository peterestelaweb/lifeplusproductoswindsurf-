#!/usr/bin/env python3

# Importar el diccionario de productos
exec(open('completar_categorias.py').read())

def generate_product_html(product):
    code = product["code"]
    name = product["name"]
    price = product["price"]
    format_info = product["format"]

    # Generar URL limpia para el enlace
    clean_name = name.lower()
    clean_name = clean_name.replace("®", "").replace("™", "").replace("&", "and")
    clean_name = clean_name.replace(" – ", "-").replace(": ", "-").replace(".", "").replace("(", "").replace(")", "")
    clean_name = clean_name.replace(" ", "-")
    clean_name = clean_name.replace("--", "-")

    buy_url = f"https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/{code}/{clean_name}"

    # Placeholder para imágenes
    placeholder_text = name.split()[0][:8] if len(name.split()[0]) > 8 else name.split()[0]

    return f'''                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_{code}_1@2x.jpg"
                                 alt="{name}"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>{placeholder_text}</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">{code}</span>
                            <span class="product-price">{price}</span>
                        </div>
                        <h3 class="product-name">{name}</h3>
                        <p class="product-format">{format_info}</p>
                        <a href="{buy_url}" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>'''

# Productos adicionales que mencionaste
productos_adicionales = [
    # Proteínas faltantes
    {"code": "3531", "name": "Lifeplus Triple Protein Shake: Vainilla", "price": "€87.75", "format": "813g", "categoria": "proteinas"},
    {"code": "3547", "name": "Lifeplus Triple Protein Shake: Chocolate (sin edulcorante)", "price": "€87.75", "format": "867g", "categoria": "proteinas"},
    {"code": "3532", "name": "Lifeplus Triple Protein Shake: Vainilla (sin edulcorante)", "price": "€87.75", "format": "813g", "categoria": "proteinas"},
    {"code": "3464", "name": "Lifeplus Vegan Protein Shake: Vainilla", "price": "€93.50", "format": "1232g", "categoria": "proteinas"},

    # Packs adicionales
    {"code": "3499", "name": "Daily Protein Pack Chocolate", "price": "€175.50", "format": "Pack", "categoria": "packs"},

    # Deportiva - Be Refueled
    {"code": "4156", "name": "Be Refueled – Vainilla", "price": "€81.50", "format": "804g", "categoria": "deportiva"},
    {"code": "4158", "name": "Be Refueled – Chocolate", "price": "€81.50", "format": "804g", "categoria": "deportiva"}
]

# Añadir productos adicionales a las categorías correspondientes
for producto in productos_adicionales:
    categoria = producto["categoria"]
    if categoria in products_by_category:
        # Verificar si ya existe un producto con ese código
        codigos_existentes = [p["code"] for p in products_by_category[categoria]]
        if producto["code"] not in codigos_existentes:
            products_by_category[categoria].append(producto)

# Generar HTML para todas las categorías
for category, products in products_by_category.items():
    if category == 'nutricionales':
        continue  # Saltar nutricionales porque ya está en el archivo base

    print(f'            <!-- Sección {get_category_name(category)} -->')
    print(f'            <div id="{category}" class="category-section">')
    print(f'                <div class="category-header">')
    print(f'                    <h2 class="category-title"><i class="fas fa-{get_category_icon(category)}"></i> {get_category_name(category)}</h2>')
    print(f'                    <p>{len(products)} productos disponibles</p>')
    print(f'                </div>')
    print(f'')
    print(f'                <div class="products-grid">')

    for product in products:
        print(generate_product_html(product))

    print(f'                </div>')
    print(f'            </div>')
    print(f'')

print('        </div>')
print('    </div>')
print()
print('    <script>')
print('        function showCategory(categoryId) {')
print('            document.querySelectorAll(\'.category-section\').forEach(section => {')
print('                section.classList.remove(\'active\');')
print('            });')
print('')
print('            const targetSection = document.getElementById(categoryId);')
print('            if (targetSection) {')
print('                targetSection.classList.add(\'active\');')
print('            }')
print('')
print('            document.querySelectorAll(\'.nav-btn\').forEach(btn => {')
print('                btn.classList.remove(\'active\');')
print('            });')
print('')
print('            const activeBtn = document.querySelector(`[data-category="${categoryId}"]`);')
print('            if (activeBtn) {')
print('                activeBtn.classList.add(\'active\');')
print('            }')
print('')
print('            window.scrollTo({')
print('                top: 100,')
print('                behavior: \'smooth\'')
print('            });')
print('        }')
print('')
print('        document.addEventListener(\'DOMContentLoaded\', function() {')
print('            document.querySelectorAll(\'.nav-btn\').forEach(btn => {')
print('                btn.addEventListener(\'click\', function() {')
print('                    const category = this.getAttribute(\'data-category\');')
print('                    showCategory(category);')
print('                });')
print('            });')
print('')
print('            const backToTopBtn = document.getElementById(\'backToTop\');')
print('')
print('            window.addEventListener(\'scroll\', function() {')
print('                if (window.pageYOffset > 300) {')
print('                    backToTopBtn.classList.add(\'show\');')
print('                } else {')
print('                    backToTopBtn.classList.remove(\'show\');')
print('                }')
print('            });')
print('')
print('            backToTopBtn.addEventListener(\'click\', function() {')
print('                window.scrollTo({')
print('                    top: 0,')
print('                    behavior: \'smooth\'')
print('                });')
print('            });')
print('')
print('            showCategory(\'welcome\');')
print('        });')
print('')
print('        document.querySelectorAll(\'.product-link\').forEach(link => {')
print('            link.addEventListener(\'click\', function(e) {')
print('                e.stopPropagation();')
print('            });')
print('        });')
print('    </script>')
print('</body>')
print('</html>')