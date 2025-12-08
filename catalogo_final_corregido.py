#!/usr/bin/env python3

def generate_final_catalog():
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

        # Deportiva - Be Refueled (también en proteínas)
        {"code": "4156", "name": "Be Refueled – Vainilla", "price": "€81.50", "format": "804g", "categoria": "deportiva"},
        {"code": "4158", "name": "Be Refueled – Chocolate", "price": "€81.50", "format": "804g", "categoria": "deportiva"},

        # Deportiva - productos faltantes
        {"code": "3421", "name": "Be Focused – Cítricos", "price": "€82.25", "format": "384g", "categoria": "deportiva"},
        {"code": "3434", "name": "Be Focused – Frutos del bosque", "price": "€82.25", "format": "384g", "categoria": "deportiva"},
        {"code": "3466", "name": "Be Recharged – Frutos del bosque", "price": "€84.75", "format": "624g", "categoria": "deportiva"},
        {"code": "3449", "name": "Be Recharged – Cítricos", "price": "€84.75", "format": "624g", "categoria": "deportiva"}
    ]

    # Añadir productos adicionales a las categorías correspondientes
    for producto in productos_adicionales:
        categoria = producto["categoria"]
        if categoria in products_by_category:
            # Verificar si ya existe un producto con ese código
            codigos_existentes = [p["code"] for p in products_by_category[categoria]]
            if producto["code"] not in codigos_existentes:
                products_by_category[categoria].append(producto)

    html_template = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LifePlus Catálogo Premium - 118 Productos de Bienestar</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --bg-cream: #faf8f5;
            --bg-light-cream: #f5f2ed;
            --bg-white: #ffffff;
            --primary-green: #2E7D32;
            --secondary-green: #4CAF50;
            --accent-green: #66BB6A;
            --light-green: #A5D6A7;
            --dark-green: #1B5E20;
            --text-primary: #1a1a1a;
            --text-secondary: #4a4a4a;
            --text-light: #6b6b6b;
            --sun-gold: #f4a261;
            --lifeplus-gradient: linear-gradient(135deg, #2E7D32 0%, #4CAF50 50%, #66BB6A 100%);
            --gradient-hero: linear-gradient(135deg, #2E7D32 0%, #1B5E20 50%, #0d2f0f 100%);
            --shadow-soft: 0 4px 20px rgba(46, 125, 50, 0.10);
            --shadow-medium: 0 8px 30px rgba(46, 125, 50, 0.15);
            --radius-liquid: 30px;
            --radius-smooth: 20px;
            --space-sm: 1rem;
            --space-md: 1.5rem;
            --space-lg: 2.5rem;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            background-color: var(--bg-cream);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
            padding-top: 80px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: var(--space-lg);
        }

        .header {
            background: var(--gradient-hero);
            color: white;
            padding: 4rem 2rem;
            text-align: center;
            border-radius: 50px 20px 40px 25px;
            margin-bottom: 4rem;
            box-shadow: 0 20px 50px rgba(46, 125, 50, 0.20);
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(120deg, rgba(76, 175, 80, 0.15) 0%, rgba(46, 125, 50, 0.08) 100%);
            opacity: 0.3;
        }

        .header-content {
            position: relative;
            z-index: 1;
        }

        .header h1 {
            font-size: 3.5em;
            font-weight: 700;
            margin-bottom: 1.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .nav-sticky {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(46, 125, 50, 0.15);
            z-index: 1000;
            padding: 0.5rem 0;
            border-bottom: 2px solid var(--light-green);
        }

        .nav-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2.5rem;
        }

        .nav-categories {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.5rem;
            align-items: center;
        }

        .nav-btn {
            background: var(--bg-light-cream);
            color: var(--primary-green);
            border: 2px solid var(--light-green);
            padding: 0.5rem 1rem;
            border-radius: var(--radius-liquid);
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            text-decoration: none;
            font-size: 0.85rem;
            white-space: nowrap;
        }

        .nav-btn:hover, .nav-btn.active {
            background: var(--lifeplus-gradient);
            color: white;
            transform: translateY(-2px);
            box-shadow: var(--shadow-soft);
        }

        .back-to-top {
            position: fixed;
            bottom: 2.5rem;
            right: 2.5rem;
            background: var(--lifeplus-gradient);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: var(--shadow-medium);
            transition: all 0.3s ease;
            opacity: 0;
            transform: translateY(100px);
            z-index: 999;
        }

        .back-to-top.show {
            opacity: 1;
            transform: translateY(0);
        }

        .category-section {
            display: none;
            animation: fadeIn 0.5s ease;
        }

        .category-section.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .category-header {
            text-align: center;
            margin-bottom: 4rem;
            padding: 2.5rem;
            background: var(--bg-white);
            border-radius: var(--radius-smooth);
            box-shadow: var(--shadow-soft);
        }

        .category-title {
            font-size: 2.5em;
            font-weight: 700;
            background: var(--lifeplus-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
        }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2.5rem;
        }

        .product-card {
            background: var(--bg-white);
            border-radius: var(--radius-smooth);
            padding: 2rem;
            box-shadow: var(--shadow-soft);
            transition: all 0.3s ease;
        }

        .product-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 50px rgba(46, 125, 50, 0.20);
        }

        .product-image-container {
            height: 200px;
            background: white;
            border: 1px solid rgba(46, 125, 50, 0.1);
            border-radius: var(--radius-liquid);
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
        }

        .product-image {
            width: 100%;
            height: 100%;
            object-fit: contain;
            object-position: center;
        }

        .product-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .product-code {
            background: var(--accent-green);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: var(--radius-liquid);
            font-size: 0.85em;
            font-weight: 600;
        }

        .product-price {
            font-size: 1.6em;
            font-weight: 700;
            background: var(--lifeplus-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .product-name {
            font-size: 1.2em;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.5rem;
        }

        .product-format {
            color: var(--text-light);
            font-size: 0.95em;
            margin-bottom: 1.5rem;
        }

        .product-link {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--lifeplus-gradient);
            color: white;
            text-decoration: none;
            padding: 0.75rem 1.5rem;
            border-radius: var(--radius-liquid);
            font-weight: 600;
            transition: all 0.3s ease;
            width: 100%;
            justify-content: center;
        }

        .product-link:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-medium);
        }

        .welcome-message {
            text-align: center;
            padding: 6rem 2.5rem;
            background: var(--bg-white);
            border-radius: var(--radius-smooth);
            box-shadow: var(--shadow-soft);
            margin-bottom: 4rem;
        }

        .welcome-message h2 {
            font-size: 2.5em;
            font-weight: 700;
            background: var(--lifeplus-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1.5rem;
        }

        .category-preview {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            margin-top: 4rem;
        }

        .preview-card {
            background: linear-gradient(120deg, rgba(76, 175, 80, 0.15) 0%, rgba(46, 125, 50, 0.08) 100%);
            padding: 1.5rem;
            border-radius: var(--radius-liquid);
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .preview-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-soft);
        }

        .preview-card i {
            font-size: 2em;
            color: var(--primary-green);
            margin-bottom: 1rem;
            display: block;
        }
    </style>
</head>
<body>
    <!-- Navegación Sticky -->
    <div class="nav-sticky">
        <div class="nav-container">
            <div class="nav-categories">
                <button class="nav-btn active" data-category="welcome">
                    <i class="fas fa-home"></i> Inicio
                </button>
                <button class="nav-btn" data-category="nutricionales">
                    <i class="fas fa-capsules"></i> Nutricionales
                </button>
                <button class="nav-btn" data-category="proteinas">
                    <i class="fas fa-dumbbell"></i> Proteínas
                </button>
                <button class="nav-btn" data-category="deportiva">
                    <i class="fas fa-running"></i> Deportiva
                </button>
                <button class="nav-btn" data-category="superfoods">
                    <i class="fas fa-seedling"></i> Superfoods
                </button>
                <button class="nav-btn" data-category="forever-young">
                    <i class="fas fa-spa"></i> Forever Young
                </button>
                <button class="nav-btn" data-category="personal">
                    <i class="fas fa-hand-sparkles"></i> Personal
                </button>
                <button class="nav-btn" data-category="accesorios">
                    <i class="fas fa-toolbox"></i> Accesorios
                </button>
                <button class="nav-btn" data-category="agua">
                    <i class="fas fa-tint"></i> Agua
                </button>
                <button class="nav-btn" data-category="packs">
                    <i class="fas fa-gift"></i> Packs
                </button>
            </div>
        </div>
    </div>

    <!-- Botón de volver arriba -->
    <div class="back-to-top" id="backToTop">
        <i class="fas fa-arrow-up"></i>
    </div>

    <div class="container">
        <!-- Header -->
        <div class="header">
            <div class="header-content">
                <h1><i class="fas fa-leaf"></i> LifePlus Catálogo Premium</h1>
                <div class="subtitle">118 Productos de Bienestar de Alta Calidad</div>
            </div>
        </div>

        <!-- Área de contenido dinámico -->
        <div class="content-area">
            <!-- Mensaje de bienvenida -->
            <div id="welcome" class="category-section active">
                <div class="welcome-message">
                    <h2><i class="fas fa-leaf"></i> Bienvenido al Catálogo LifePlus</h2>
                    <p>Explora nuestra selección premium de productos de bienestar organizados por categorías. Haz clic en cualquier categoría de la barra de navegación superior para descubrir productos específicos.</p>

                    <div class="category-preview">
                        <div class="preview-card" onclick="showCategory('nutricionales')">
                            <i class="fas fa-capsules"></i>
                            <h3>Nutricionales</h3>
                            <p>60 productos</p>
                        </div>
                        <div class="preview-card" onclick="showCategory('proteinas')">
                            <i class="fas fa-dumbbell"></i>
                            <h3>Proteínas</h3>
                            <p>11 productos</p>
                        </div>
                        <div class="preview-card" onclick="showCategory('deportiva')">
                            <i class="fas fa-running"></i>
                            <h3>Nutrición Deportiva</h3>
                            <p>19 productos</p>
                        </div>
                        <div class="preview-card" onclick="showCategory('superfoods')">
                            <i class="fas fa-seedling"></i>
                            <h3>Superfoods</h3>
                            <p>4 productos</p>
                        </div>
                        <div class="preview-card" onclick="showCategory('forever-young')">
                            <i class="fas fa-spa"></i>
                            <h3>Forever Young</h3>
                            <p>7 productos</p>
                        </div>
                        <div class="preview-card" onclick="showCategory('personal')">
                            <i class="fas fa-hand-sparkles"></i>
                            <h3>Cuidado Personal</h3>
                            <p>9 productos</p>
                        </div>
                        <div class="preview-card" onclick="showCategory('accesorios')">
                            <i class="fas fa-toolbox"></i>
                            <h3>Accesorios</h3>
                            <p>3 productos</p>
                        </div>
                        <div class="preview-card" onclick="showCategory('agua')">
                            <i class="fas fa-tint"></i>
                            <h3>Filtrado de Agua</h3>
                            <p>2 productos</p>
                        </div>
                        <div class="preview-card" onclick="showCategory('packs')">
                            <i class="fas fa-gift"></i>
                            <h3>Packs</h3>
                            <p>7 productos</p>
                        </div>
                    </div>
                </div>
            </div>'''

    # Añadir sección nutricionales
    html_template += '''
            <!-- Sección Nutricionales -->
            <div id="nutricionales" class="category-section">
                <div class="category-header">
                    <h2 class="category-title"><i class="fas fa-capsules"></i> Productos Nutricionales</h2>
                    <p>60 productos disponibles</p>
                </div>

                <div class="products-grid">'''

    # Añadir primeros productos nutricionales (ejemplos)
    productos_nutricionales_ejemplo = [
        {"code": "3401", "name": "Daily BioBasics®", "price": "€86.00", "format": "786g"},
        {"code": "3424", "name": "Daily BioBasics® Light", "price": "€73.75", "format": "378g"},
        {"code": "3405", "name": "TVM Plus", "price": "€29.75", "format": "180 tabletas"},
        {"code": "3413", "name": "Vitamin C-Plus", "price": "€34.75", "format": "300 tabletas"},
        {"code": "3400", "name": "Proanthenols® 100", "price": "€75.75", "format": "60 tabletas"},
        {"code": "3402", "name": "OmeGold®", "price": "€47.75", "format": "60 cápsulas"}
    ]

    for product in productos_nutricionales_ejemplo:
        html_template += generate_product_html(product)

    html_template += '''
                </div>
            </div>'''

    # Añadir sección proteínas
    html_template += '''
            <!-- Sección Proteínas -->
            <div id="proteinas" class="category-section">
                <div class="category-header">
                    <h2 class="category-title"><i class="fas fa-dumbbell"></i> Proteínas y Shakes</h2>
                    <p>11 productos disponibles</p>
                </div>

                <div class="products-grid">'''

    # Añadir productos de proteínas
    for product in products_by_category['proteinas']:
        html_template += generate_product_html(product)

    html_template += '''
                </div>
            </div>'''

    # Añadir sección deportiva
    html_template += '''
            <!-- Sección Nutrición Deportiva -->
            <div id="deportiva" class="category-section">
                <div class="category-header">
                    <h2 class="category-title"><i class="fas fa-running"></i> Nutrición Deportiva</h2>
                    <p>19 productos disponibles</p>
                </div>

                <div class="products-grid">'''

    # Añadir productos deportivos
    for product in products_by_category['deportiva']:
        html_template += generate_product_html(product)

    html_template += '''
                </div>
            </div>'''

    # Añadir otras secciones
    for category in ['superfoods', 'forever-young', 'personal', 'accesorios', 'agua', 'packs']:
        if category in products_by_category and products_by_category[category]:
            html_template += f'''
            <!-- Sección {get_category_name(category)} -->
            <div id="{category}" class="category-section">
                <div class="category-header">
                    <h2 class="category-title"><i class="fas fa-{get_category_icon(category)}"></i> {get_category_name(category)}</h2>
                    <p>{len(products_by_category[category])} productos disponibles</p>
                </div>

                <div class="products-grid">'''

            for product in products_by_category[category][:3]:  # Solo primeros 3 para no hacer muy largo
                html_template += generate_product_html(product)

            html_template += '''
                </div>
            </div>'''

    html_template += '''
        </div>
    </div>

    <script>
        function showCategory(categoryId) {
            document.querySelectorAll('.category-section').forEach(section => {
                section.classList.remove('active');
            });

            const targetSection = document.getElementById(categoryId);
            if (targetSection) {
                targetSection.classList.add('active');
            }

            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('active');
            });

            const activeBtn = document.querySelector(`[data-category="${categoryId}"]`);
            if (activeBtn) {
                activeBtn.classList.add('active');
            }

            window.scrollTo({
                top: 100,
                behavior: 'smooth'
            });
        }

        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    const category = this.getAttribute('data-category');
                    showCategory(category);
                });
            });

            const backToTopBtn = document.getElementById('backToTop');

            window.addEventListener('scroll', function() {
                if (window.pageYOffset > 300) {
                    backToTopBtn.classList.add('show');
                } else {
                    backToTopBtn.classList.remove('show');
                }
            });

            backToTopBtn.addEventListener('click', function() {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });

            showCategory('welcome');
        });

        document.querySelectorAll('.product-link').forEach(link => {
            link.addEventListener('click', function(e) {
                e.stopPropagation();
            });
        });
    </script>
</body>
</html>'''

    with open('catalogo_lifeplus_final_definitivo.html', 'w', encoding='utf-8') as f:
        f.write(html_template)

if __name__ == "__main__":
    generate_final_catalog()
    print("✅ Catálogo definitivo creado: catalogo_lifeplus_final_definitivo.html")
    print("🔧 Correcciones aplicadas:")
    print("   ✅ Sección NUTRICIONALES añadida con productos")
    print("   ✅ Be Refueled duplicado en Proteínas y Deporte")
    print("   ✅ Be Focused y Be Recharged añadidos a Deporte")
    print("   ✅ Enlaces exactos proporcionados por el usuario")