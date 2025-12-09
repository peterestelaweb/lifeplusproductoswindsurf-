#!/usr/bin/env python3

import re

def agregar_buscador_catalogo():
    """Agregar funcionalidad de buscador inteligente al catálogo existente"""

    # Leer el catálogo base
    with open('catalogo_lifeplus_final.html', 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Importar la base de datos para obtener atributos de búsqueda
    exec(open('completar_categorias.py').read())

    # Agregar atributos data-searchable a todas las tarjetas de producto
    print("Agregando atributos de búsqueda a los productos...")

    def agregar_atributos_search(match):
        card_html = match.group(0)

        # Buscar el código del producto
        code_match = re.search(r'<span class="product-code">(\d+)</span>', card_html)
        if code_match:
            code = code_match.group(1)

            # Buscar el producto en la base de datos
            category = None
            name = ""
            format_info = ""

            for cat, products in products_by_category.items():
                for product in products:
                    if product["code"] == code:
                        category = cat
                        name = product["name"]
                        format_info = product["format"]
                        break
                if category:
                    break

            if category:
                # Crear texto searchable
                searchable_text = f"{name} {code} {category} {format_info}".lower()
                # Agregar atributo data-searchable
                card_html = card_html.replace(
                    '<div class="product-card">',
                    f'<div class="product-card" data-category="{category}" data-searchable="{searchable_text}">'
                )

        return card_html

    # Aplicar función a todas las tarjetas de producto
    product_pattern = r'<div class="product-card">.*?</div>\s*</a>\s*</div>'
    contenido = re.sub(product_pattern, agregar_atributos_search, contenido, flags=re.DOTALL)

    # Agregar CSS para el buscador
    css_buscador = '''
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
            position: absolute;
            left: var(--space-sm);
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
            display: none !important;
        }

        .category-section.no-results .category-header::after {
            content: "No se encontraron productos en esta categoría";
            display: block;
            text-align: center;
            color: var(--text-secondary);
            font-style: italic;
            margin-top: var(--space-md);
        }

        .category-section:not(.no-results) .category-header::after {
            content: none;
        }
    '''

    # Insertar CSS antes del closing </style>
    style_end = contenido.find('</style>')
    if style_end != -1:
        contenido = contenido[:style_end] + css_buscador + contenido[style_end:]

    # Agregar HTML del buscador después del welcome section
    html_buscador = '''
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

    # Encontrar dónde insertar el buscador (después del welcome section)
    welcome_end = contenido.find('</div>\n\n            <!-- Sección Nutricionales -->')
    if welcome_end != -1:
        welcome_end = contenido.find('</div>', welcome_end) + 6
        contenido = contenido[:welcome_end] + html_buscador + contenido[welcome_end:]

    # Agregar JavaScript para el buscador
    js_buscador = '''
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
                        const isMatch = searchableText && searchableText.includes(searchTerm);

                        if (searchTerm === '' || isMatch) {
                            card.classList.remove('hidden');
                            visibleCount++;

                            // Find parent category and mark it as visible
                            const categorySection = card.closest('.category-section');
                            if (categorySection && categorySection.id !== 'welcome') {
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

    # Insertar JavaScript antes del closing </script>
    script_end = contenido.rfind('</script>')
    if script_end != -1:
        contenido = contenido[:script_end] + js_buscador + '\n    ' + contenido[script_end:]

    # Actualizar título
    contenido = contenido.replace(
        '<title>LifePlus Catálogo Premium - 111 Productos de Bienestar</title>',
        '<title>LifePlus Catálogo Premium con Buscador - 111 Productos</title>'
    )

    # Escribir el nuevo catálogo con buscador
    with open('catalogo_lifeplus_buscador.html', 'w', encoding='utf-8') as f:
        f.write(contenido)

    print("¡Catálogo con buscador inteligente creado exitosamente!")
    print("Archivo: catalogo_lifeplus_buscador.html")
    print("\n✅ Funcionalidades añadidas:")
    print("   • Búsqueda en tiempo real por nombre, código o categoría")
    print("   • Atributos data-searchable para cada producto")
    print("   • Contador de productos encontrados")
    print("   • Botón para limpiar búsqueda")
    print("   • Botón para mostrar todos los productos")
    print("   • Navegación con tecla Escape")
    print("   • Debounce para optimizar rendimiento")
    print("   • Indicadores visuales de categorías sin resultados")

if __name__ == "__main__":
    agregar_buscador_catalogo()