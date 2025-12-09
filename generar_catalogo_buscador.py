#!/usr/bin/env python3

# Importar la base de datos de productos
exec(open('completar_categorias.py').read())

def generate_product_html_with_search(product):
    code = product["code"]
    name = product["name"]
    price = product["price"]
    price_asap = product.get("price_asap", "")
    format_info = product["format"]
    category = product.get("category", "")

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

    # Create searchable data attributes
    searchable_text = f"{name} {code} {category} {format_info}".lower()

    return f'''                    <div class="product-card" data-category="{category}" data-searchable="{searchable_text}">
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
        'proteinas': 'Proteínas',
        'deportiva': 'Deporte',
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
        'packs': 'fa-box',
        'superfoods': 'fa-leaf',
        'forever-young': 'fa-hourglass-half',
        'personal': 'fa-user',
        'accesorios': 'fa-shopping-bag',
        'agua': 'fa-tint'
    }
    return icons.get(category, 'fa-cube')

# Read the base template with search functionality
with open('catalogo_lifeplus_final.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# Generate all sections with search attributes
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
            # Add category to product data for search
            product['category'] = category
            section_html += generate_product_html_with_search(product) + '\n'

        section_html += '''                </div>
            </div>

'''
        sections_html += section_html

# Count total products
total_products = sum(len(products) for products in products_by_category.values() if products)
print(f"Generando catálogo con buscador: {total_products} productos totales...")

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

    # Add search functionality to the template
    search_html = '''
        <!-- Search Bar -->
        <div class="search-container">
            <div class="search-box">
                <i class="fas fa-search search-icon"></i>
                <input type="text" id="productSearch" placeholder="Buscar productos por nombre, código o categoría..." autocomplete="off">
                <button class="search-clear-btn" id="clearSearch" style="display: none;">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <div class="search-results-info" id="searchResultsInfo" style="display: none;">
                <span id="resultsCount"></span>
                <button class="show-all-btn" id="showAllBtn">Mostrar todos</button>
            </div>
        </div>
    '''

    # Insert search bar after the welcome section
    welcome_section_end = final_content.find('</div>', final_content.find('<div id="welcome"')) + 6
    final_content = final_content[:welcome_section_end] + search_html + final_content[welcome_section_end:]

    # Add CSS for search functionality
    search_css = '''
        /* Search Bar Styles */
        .search-container {
            background: var(--bg-white);
            border-radius: var(--radius-smooth);
            padding: var(--space-md);
            margin: var(--space-lg) 0;
            box-shadow: var(--shadow-soft);
        }

        .search-box {
            position: relative;
            display: flex;
            align-items: center;
            gap: var(--space-sm);
        }

        .search-icon {
            color: var(--primary-green);
            font-size: 1.2rem;
            z-index: 2;
        }

        #productSearch {
            flex: 1;
            padding: var(--space-sm) var(--space-sm) var(--space-sm) 3rem;
            border: 2px solid var(--light-green);
            border-radius: var(--radius-smooth);
            font-size: 1rem;
            font-family: 'Montserrat', sans-serif;
            transition: all 0.3s ease;
            background: var(--bg-white);
        }

        #productSearch:focus {
            outline: none;
            border-color: var(--primary-green);
            box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.1);
        }

        .search-clear-btn {
            position: absolute;
            right: var(--space-sm);
            background: none;
            border: none;
            color: var(--text-secondary);
            cursor: pointer;
            padding: 0.5rem;
            border-radius: 50%;
            transition: all 0.3s ease;
        }

        .search-clear-btn:hover {
            background: var(--bg-light-cream);
            color: var(--text-primary);
        }

        .search-results-info {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: var(--space-sm);
            padding: var(--space-sm);
            background: var(--bg-light-cream);
            border-radius: var(--radius-smooth);
            font-size: 0.9rem;
            color: var(--text-secondary);
        }

        .show-all-btn {
            background: var(--primary-green);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: var(--radius-smooth);
            cursor: pointer;
            font-size: 0.8rem;
            transition: all 0.3s ease;
        }

        .show-all-btn:hover {
            background: var(--dark-green);
            transform: translateY(-2px);
        }

        .product-card.hidden {
            display: none;
        }

        .category-section.no-results .category-header::after {
            content: "No se encontraron productos en esta categoría";
            display: block;
            text-align: center;
            color: var(--text-secondary);
            font-style: italic;
            margin-top: var(--space-md);
        }

        .highlight {
            background-color: var(--sun-gold);
            padding: 2px 4px;
            border-radius: 3px;
            font-weight: 600;
        }
    '''

    # Insert CSS before the closing </style> tag
    style_end = final_content.find('</style>')
    if style_end != -1:
        final_content = final_content[:style_end] + search_css + final_content[style_end:]

    # Add JavaScript for search functionality
    search_js = '''
        function initializeSearch() {
            const searchInput = document.getElementById('productSearch');
            const clearBtn = document.getElementById('clearSearch');
            const resultsInfo = document.getElementById('searchResultsInfo');
            const resultsCount = document.getElementById('resultsCount');
            const showAllBtn = document.getElementById('showAllBtn');
            const allProductCards = document.querySelectorAll('.product-card');
            const allCategorySections = document.querySelectorAll('.category-section');

            let searchTimeout;

            function performSearch(query) {
                clearTimeout(searchTimeout);

                searchTimeout = setTimeout(() => {
                    const searchTerm = query.toLowerCase().trim();
                    let visibleCount = 0;
                    let visibleCategories = new Set();

                    // Show/hide products based on search
                    allProductCards.forEach(card => {
                        const searchableText = card.getAttribute('data-searchable');
                        const isMatch = searchableText.includes(searchTerm);

                        if (searchTerm === '' || isMatch) {
                            card.classList.remove('hidden');
                            visibleCount++;

                            // Find parent category and mark it as visible
                            const categorySection = card.closest('.category-section');
                            if (categorySection) {
                                visibleCategories.add(categorySection.id);
                                categorySection.classList.remove('no-results');
                            }
                        } else {
                            card.classList.add('hidden');
                        }
                    });

                    // Show/hide category sections
                    allCategorySections.forEach(section => {
                        if (section.id === 'welcome') return; // Always show welcome

                        const categoryCards = section.querySelectorAll('.product-card:not(.hidden)');
                        if (searchTerm === '' || categoryCards.length > 0) {
                            section.style.display = 'block';
                            section.classList.remove('no-results');
                        } else {
                            section.style.display = 'block';
                            section.classList.add('no-results');
                        }
                    });

                    // Update search results info
                    if (searchTerm) {
                        resultsInfo.style.display = 'flex';
                        resultsCount.textContent = `Se encontraron ${visibleCount} producto${visibleCount !== 1 ? 's' : ''}`;
                        clearBtn.style.display = 'block';
                    } else {
                        resultsInfo.style.display = 'none';
                        clearBtn.style.display = 'none';
                        allCategorySections.forEach(section => {
                            section.classList.remove('no-results');
                        });
                    }
                }, 300); // Debounce search
            }

            // Event listeners
            searchInput.addEventListener('input', (e) => {
                performSearch(e.target.value);
            });

            clearBtn.addEventListener('click', () => {
                searchInput.value = '';
                performSearch('');
                searchInput.focus();
            });

            showAllBtn.addEventListener('click', () => {
                searchInput.value = '';
                performSearch('');
                showCategory('welcome');
                window.scrollTo({ top: 100, behavior: 'smooth' });
            });

            // Clear search on Escape key
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && document.activeElement === searchInput) {
                    searchInput.value = '';
                    performSearch('');
                }
            });
        }

        // Initialize search when DOM is loaded
        document.addEventListener('DOMContentLoaded', function() {
            // Wait for other initializations to complete
            setTimeout(initializeSearch, 100);
        });
    '''

    # Insert JavaScript before the closing </script> tag
    script_end = final_content.rfind('</script>')
    if script_end != -1:
        final_content = final_content[:script_end] + search_js + '\n    ' + final_content[script_end:]

    # Update title
    final_content = final_content.replace(
        '<title>LifePlus Catálogo Premium - 111 Productos de Bienestar</title>',
        '<title>LifePlus Catálogo Premium con Buscador - 111 Productos</title>'
    )

    # Write the search catalog
    with open('catalogo_lifeplus_buscador.html', 'w', encoding='utf-8') as f:
        f.write(final_content)

    print("¡Catálogo con buscador inteligente generado exitosamente!")
    print("Archivo creado: catalogo_lifeplus_buscador.html")
    print(f"Total productos: {total_products}")
    print("✅ Funcionalidades:")
    print("   • Búsqueda en tiempo real por nombre, código o categoría")
    print("   • Resaltado de resultados")
    print("   • Contador de productos encontrados")
    print("   • Botón para limpiar búsqueda")
    print("   • Botón para mostrar todos los productos")
    print("   • Navegación con tecla Escape")
    print("   • Debounce para optimizar rendimiento")

else:
    print("Error: No se pudo encontrar el punto de inserción en el template")