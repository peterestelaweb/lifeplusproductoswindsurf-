#!/usr/bin/env python3

def create_complete_catalog():
    # Importar el diccionario de productos
    with open('completar_categorias.py', 'r', encoding='utf-8') as f:
        code = compile(f.read(), 'completar_categorias.py', 'exec')
    exec(code, globals())

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

    # Start building the complete HTML
    html_content = '''<!DOCTYPE html>
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
            padding: var(--space-md);
        }

        .back-to-top {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: var(--primary-green);
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 18px;
            cursor: pointer;
            opacity: 0;
            transition: all 0.3s ease;
            z-index: 1000;
            box-shadow: var(--shadow-soft);
        }

        .back-to-top.show {
            opacity: 1;
        }

        .back-to-top:hover {
            background-color: var(--dark-green);
            transform: translateY(-3px);
            box-shadow: var(--shadow-medium);
        }

        .nav-container {
            background: var(--gradient-hero);
            border-radius: var(--radius-liquid);
            box-shadow: var(--shadow-medium);
            margin-bottom: var(--space-lg);
            padding: var(--space-md);
            position: sticky;
            top: 20px;
            z-index: 100;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .nav-buttons {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: var(--space-sm);
        }

        .nav-btn {
            background: rgba(255, 255, 255, 0.15);
            color: white;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: var(--radius-smooth);
            padding: 12px 20px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .nav-btn:hover {
            background: rgba(255, 255, 255, 0.25);
            border-color: rgba(255, 255, 255, 0.5);
            transform: translateY(-2px);
            box-shadow: var(--shadow-soft);
        }

        .nav-btn.active {
            background: rgba(255, 255, 255, 0.9);
            color: var(--primary-green);
            border-color: white;
        }

        .category-section {
            display: none;
            animation: fadeInUp 0.6s ease-out;
        }

        .category-section.active {
            display: block;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .category-header {
            text-align: center;
            margin-bottom: var(--space-lg);
            padding: var(--space-lg);
            background: white;
            border-radius: var(--radius-liquid);
            box-shadow: var(--shadow-soft);
        }

        .category-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--primary-green);
            margin-bottom: var(--space-sm);
            background: var(--lifeplus-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: var(--space-lg);
            margin-bottom: var(--space-lg);
        }

        .product-card {
            background: white;
            border-radius: var(--radius-liquid);
            padding: var(--space-md);
            box-shadow: var(--shadow-soft);
            transition: all 0.3s ease;
            border: 2px solid rgba(46, 125, 50, 0.05);
        }

        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-medium);
            border-color: var(--accent-green);
        }

        .product-image-container {
            width: 100%;
            height: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: var(--radius-smooth);
            overflow: hidden;
            margin-bottom: var(--space-sm);
            background: var(--bg-light-cream);
        }

        .product-image {
            width: 100%;
            height: 100%;
            object-fit: contain;
            transition: transform 0.3s ease;
        }

        .product-card:hover .product-image {
            transform: scale(1.05);
        }

        .product-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: var(--space-sm);
        }

        .product-code {
            font-size: 12px;
            color: var(--text-light);
            background: var(--bg-light-cream);
            padding: 4px 8px;
            border-radius: 12px;
            font-weight: 500;
        }

        .product-price {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--primary-green);
        }

        .product-name {
            font-size: 1rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: var(--space-sm);
            line-height: 1.4;
        }

        .product-format {
            font-size: 14px;
            color: var(--text-secondary);
            margin-bottom: var(--space-md);
        }

        .product-link {
            background: var(--lifeplus-gradient);
            color: white;
            text-decoration: none;
            border-radius: var(--radius-smooth);
            padding: 12px 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: var(--space-sm);
            font-weight: 500;
            transition: all 0.3s ease;
            border: none;
            width: 100%;
        }

        .product-link:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-soft);
        }

        @media (max-width: 768px) {
            body {
                padding-top: 60px;
            }

            .container {
                padding: var(--space-sm);
            }

            .nav-container {
                padding: var(--space-sm);
                position: sticky;
                top: 10px;
            }

            .nav-btn {
                font-size: 12px;
                padding: 10px 15px;
            }

            .category-title {
                font-size: 2rem;
            }

            .products-grid {
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: var(--space-md);
            }
        }

        @media (max-width: 480px) {
            .nav-buttons {
                gap: 5px;
            }

            .nav-btn {
                font-size: 11px;
                padding: 8px 12px;
            }

            .category-title {
                font-size: 1.5rem;
            }

            .products-grid {
                grid-template-columns: 1fr;
            }

            .category-header {
                padding: var(--space-md);
            }
        }
    </style>
</head>
<body>
    <button class="back-to-top" id="backToTop">
        <i class="fas fa-arrow-up"></i>
    </button>

    <div class="container">
        <div class="nav-container">
            <div class="nav-buttons">
                <button class="nav-btn" data-category="welcome">
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
                <button class="nav-btn" data-category="packs">
                    <i class="fas fa-box"></i> Packs
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
            </div>
        </div>

        <div class="main-content">
            <!-- Welcome Section -->
            <div id="welcome" class="category-section active">
                <div class="category-header">
                    <h2 class="category-title">Bienvenido al Catálogo LifePlus Premium</h2>
                    <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: var(--space-md);">
                        Descubre nuestra completa selección de productos de bienestar y salud
                    </p>
                    <p style="color: var(--text-light);">
                        <strong>118 productos</strong> distribuidos en <strong>9 categorías</strong>
                    </p>
                </div>

                <div class="products-grid">
                    <div class="preview-card" onclick="showCategory('nutricionales')" style="cursor: pointer; background: var(--lifeplus-gradient); color: white; text-align: center; padding: var(--space-lg); border-radius: var(--radius-liquid);">
                        <i class="fas fa-capsules" style="font-size: 3rem; margin-bottom: var(--space-sm);"></i>
                        <h3>Productos Nutricionales</h3>
                        <p>60 productos</p>
                    </div>
                    <div class="preview-card" onclick="showCategory('proteinas')" style="cursor: pointer; background: var(--lifeplus-gradient); color: white; text-align: center; padding: var(--space-lg); border-radius: var(--radius-liquid);">
                        <i class="fas fa-dumbbell" style="font-size: 3rem; margin-bottom: var(--space-sm);"></i>
                        <h3>Proteínas y Shakes</h3>
                        <p>11 productos</p>
                    </div>
                    <div class="preview-card" onclick="showCategory('deportiva')" style="cursor: pointer; background: var(--lifeplus-gradient); color: white; text-align: center; padding: var(--space-lg); border-radius: var(--radius-liquid);">
                        <i class="fas fa-running" style="font-size: 3rem; margin-bottom: var(--space-sm);"></i>
                        <h3>Nutrición Deportiva</h3>
                        <p>29 productos</p>
                    </div>
                    <div class="preview-card" onclick="showCategory('packs')" style="cursor: pointer; background: var(--lifeplus-gradient); color: white; text-align: center; padding: var(--space-lg); border-radius: var(--radius-liquid);">
                        <i class="fas fa-box" style="font-size: 3rem; margin-bottom: var(--space-sm);"></i>
                        <h3>Packs de Recomendación</h3>
                        <p>5 productos</p>
                    </div>
                    <div class="preview-card" onclick="showCategory('superfoods')" style="cursor: pointer; background: var(--lifeplus-gradient); color: white; text-align: center; padding: var(--space-lg); border-radius: var(--radius-liquid);">
                        <i class="fas fa-seedling" style="font-size: 3rem; margin-bottom: var(--space-sm);"></i>
                        <h3>Superfoods Solis</h3>
                        <p>4 productos</p>
                    </div>
                    <div class="preview-card" onclick="showCategory('forever-young')" style="cursor: pointer; background: var(--lifeplus-gradient); color: white; text-align: center; padding: var(--space-lg); border-radius: var(--radius-liquid);">
                        <i class="fas fa-spa" style="font-size: 3rem; margin-bottom: var(--space-sm);"></i>
                        <h3>Forever Young</h3>
                        <p>7 productos</p>
                    </div>
                    <div class="preview-card" onclick="showCategory('personal')" style="cursor: pointer; background: var(--lifeplus-gradient); color: white; text-align: center; padding: var(--space-lg); border-radius: var(--radius-liquid);">
                        <i class="fas fa-hand-sparkles" style="font-size: 3rem; margin-bottom: var(--space-sm);"></i>
                        <h3>Cuidado Personal</h3>
                        <p>9 productos</p>
                    </div>
                    <div class="preview-card" onclick="showCategory('accesorios')" style="cursor: pointer; background: var(--lifeplus-gradient); color: white; text-align: center; padding: var(--space-lg); border-radius: var(--radius-liquid);">
                        <i class="fas fa-toolbox" style="font-size: 3rem; margin-bottom: var(--space-sm);"></i>
                        <h3>Accesorios</h3>
                        <p>3 productos</p>
                    </div>
                    <div class="preview-card" onclick="showCategory('agua')" style="cursor: pointer; background: var(--lifeplus-gradient); color: white; text-align: center; padding: var(--space-lg); border-radius: var(--radius-liquid);">
                        <i class="fas fa-tint" style="font-size: 3rem; margin-bottom: var(--space-sm);"></i>
                        <h3>Sistemas de Filtrado de Agua</h3>
                        <p>2 productos</p>
                    </div>
                </div>
            </div>
'''

    # Generate all category sections
    categories = ['nutricionales', 'proteinas', 'deportiva', 'packs', 'superfoods', 'forever-young', 'personal', 'accesorios', 'agua']

    for category in categories:
        if category in products_by_category:
            products = products_by_category[category]

            html_content += f'''            <div id="{category}" class="category-section">
                <div class="category-header">
                    <h2 class="category-title"><i class="fas fa-{get_category_icon(category)}"></i> {get_category_name(category)}</h2>
                    <p>{len(products)} productos disponibles</p>
                </div>

                <div class="products-grid">
'''

            for product in products:
                html_content += generate_product_html(product) + '\n'

            html_content += '''                </div>
            </div>

'''

    # Add JavaScript
    html_content += '''        </div>
    </div>

    <script>
        function showCategory(categoryId) {
            // Ocultar todas las secciones
            document.querySelectorAll('.category-section').forEach(section => {
                section.classList.remove('active');
            });

            // Mostrar la sección seleccionada
            const targetSection = document.getElementById(categoryId);
            if (targetSection) {
                targetSection.classList.add('active');
            }

            // Actualizar botones de navegación
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('active');
            });

            const activeBtn = document.querySelector(`[data-category="${categoryId}"]`);
            if (activeBtn) {
                activeBtn.classList.add('active');
            }

            // Scroll al inicio del contenido
            window.scrollTo({
                top: 100,
                behavior: 'smooth'
            });
        }

        // Event listeners para botones de navegación
        document.addEventListener('DOMContentLoaded', function() {
            // Navegación principal
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    const category = this.getAttribute('data-category');
                    showCategory(category);
                });
            });

            // Botón de volver arriba
            const backToTopBtn = document.getElementById('backToTop');

            // Mostrar/ocultar botón de volver arriba
            window.addEventListener('scroll', function() {
                if (window.pageYOffset > 300) {
                    backToTopBtn.classList.add('show');
                } else {
                    backToTopBtn.classList.remove('show');
                }
            });

            // Funcionalidad del botón de volver arriba
            backToTopBtn.addEventListener('click', function() {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });

            // Iniciar mostrando mensaje de bienvenida
            showCategory('welcome');
        });

        // Prevenir que los enlaces de productos interfieran con la navegación
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('.product-link').forEach(link => {
                link.addEventListener('click', function(e) {
                    e.stopPropagation();
                });
            });
        });
    </script>
</body>
</html>'''

    # Handle Be Refueled images locally
    html_content = html_content.replace(
        'src="https://ww1.lifeplus.com/images/products/prodpic_4158_1@2x.jpg"',
        'src="./prodpic_4681_2@2x.jpg"'
    )
    html_content = html_content.replace(
        'src="https://ww1.lifeplus.com/images/products/prodpic_4156_1@2x.jpg"',
        'src="./prodpic_4681_2@2x.jpg"'
    )

    # Write the complete HTML file
    with open('catalogo_lifeplus_final_test.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("✅ Catálogo completo generado: catalogo_lifeplus_final_test.html")
    print("📱 Diseño responsivo incluido")
    print("🔍 Todas las 9 secciones funcionales")

if __name__ == "__main__":
    create_complete_catalog()