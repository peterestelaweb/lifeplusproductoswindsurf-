#!/usr/bin/env python3

def fix_missing_sections():
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
        # Handle special characters
        clean_name = clean_name.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        clean_name = clean_name.replace("ñ", "n").replace("ü", "u")

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

    # Read the current HTML file
    with open('catalogo_lifeplus_final_corregido.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate missing sections
    missing_categories = ['superfoods', 'forever-young', 'personal', 'accesorios', 'agua']
    sections_to_add = []

    for category in missing_categories:
        if category in products_by_category:
            products = products_by_category[category]

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
            sections_to_add.append(section_html)

    # Find where to insert the sections (after packs section, before closing divs)
    insert_point = content.find('        </div>\n    </div>\n\n    <script>')
    if insert_point != -1:
        # Insert all missing sections
        new_content = content[:insert_point] + '\n'.join(sections_to_add) + content[insert_point:]

        # Write the updated content back to the file
        with open('catalogo_lifeplus_final_corregido.html', 'w', encoding='utf-8') as f:
            f.write(new_content)

        print("Missing sections added successfully!")
    else:
        print("Could not find insertion point")

if __name__ == "__main__":
    fix_missing_sections()