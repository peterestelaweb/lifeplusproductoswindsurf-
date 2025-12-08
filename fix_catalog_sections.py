#!/usr/bin/env python3

def fix_catalog_sections():
    # Import the product data
    with open('completar_categorias.py', 'r', encoding='utf-8') as f:
        code = compile(f.read(), 'completar_categorias.py', 'exec')
    exec(code, globals())

    def generate_product_html(product):
        code = product["code"]
        name = product["name"]
        price = product["price"]
        format_info = product["format"]

        # Generate clean URL for the link
        clean_name = name.lower()
        clean_name = clean_name.replace("®", "").replace("™", "").replace("&", "and")
        clean_name = clean_name.replace(" – ", "-").replace(": ", "-").replace(".", "").replace("(", "").replace(")", "")
        clean_name = clean_name.replace(" ", "-")
        clean_name = clean_name.replace("--", "-")

        buy_url = f"https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/{code}/{clean_name}"

        # Placeholder for images
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

    # Generate HTML sections for categories that need fixing
    categories_to_fix = ['forever-young', 'personal', 'accesorios', 'agua', 'packs']

    for category in categories_to_fix:
        if category in products_by_category:
            products = products_by_category[category]

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

if __name__ == "__main__":
    fix_catalog_sections()