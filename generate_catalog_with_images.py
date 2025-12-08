#!/usr/bin/env python3
import json

def generate_catalog_with_images():
    # Cargar las URLs de imágenes
    with open('product_images.json', 'r', encoding='utf-8') as f:
        product_images = json.load(f)

    # Productos representativos para mostrar
    selected_products = {
        '3401': {'name': 'Daily BioBasics®', 'price': '€86.00', 'format': '786g'},
        '3400': {'name': 'Proanthenols® 100', 'price': '€75.75', 'format': '60 tabletas'},
        '3402': {'name': 'OmeGold®', 'price': '€47.75', 'format': '60 cápsulas'},
        '3431': {'name': 'EPA Plus', 'price': '€27.50', 'format': '90 cápsulas'},
        '3530': {'name': 'Lifeplus Triple Protein Shake: Chocolate', 'price': '€87.75', 'format': '867g'},
        '3442': {'name': 'Lifeplus Vegan Protein Shake: Chocolate', 'price': '€93.50', 'format': '1235g'},
        '3434': {'name': 'Be Focused – Frutos del Bosque', 'price': '€82.25', 'format': '384g'},
        '3484': {'name': 'SOLIS Purple Flash®', 'price': '€79.75', 'format': '183g', 'highlight': '⭐ Más Vendido'},
        '4144': {'name': 'Forever Young Day Crème SPF 25', 'price': '€73.25', 'format': '50 ml'},
        '6134': {'name': 'Lifeplus Wonder Gel', 'price': '€38.00', 'format': '114 ml'},
        '3507': {'name': 'Maintain & Protect VEGAN', 'price': '€165.00', 'format': 'Pack vegano', 'badge': '🌱 Vegano'}
    }

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
            /* Colores exactos de lifepluspdf.peterestela.com */
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
            --radius-organic: 50px 20px 40px 25px;
            --radius-liquid: 30px;
            --radius-smooth: 20px;
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
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2.5rem;
        }

        .header {
            background: var(--gradient-hero);
            color: white;
            padding: 4rem 2rem;
            text-align: center;
            border-radius: var(--radius-organic);
            margin-bottom: 4rem;
            box-shadow: 0 20px 50px rgba(46, 125, 50, 0.20);
            position: relative;
            overflow: hidden;
        }

        .header h1 {
            font-size: 3.5em;
            font-weight: 700;
            margin-bottom: 1.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .subtitle {
            font-size: 1.4em;
            font-weight: 400;
            margin-bottom: 2rem;
            opacity: 0.95;
        }

        .products-showcase {
            text-align: center;
            margin-bottom: 4rem;
        }

        .showcase-title {
            font-size: 2.2em;
            font-weight: 600;
            background: var(--lifeplus-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
        }

        .showcase-subtitle {
            color: var(--text-secondary);
            font-size: 1.2em;
            margin-bottom: 3rem;
        }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
            margin-bottom: 4rem;
        }

        .product-card {
            background: var(--bg-white);
            border-radius: var(--radius-smooth);
            padding: 2rem;
            box-shadow: var(--shadow-soft);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            border: 2px solid transparent;
        }

        .product-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 50px rgba(46, 125, 50, 0.20);
            border-color: var(--light-green);
        }

        .product-image-container {
            width: 100%;
            height: 200px;
            border-radius: var(--radius-liquid);
            overflow: hidden;
            margin-bottom: 1.5rem;
            position: relative;
            background: var(--bg-light-cream);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .product-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }

        .product-card:hover .product-image {
            transform: scale(1.05);
        }

        .product-placeholder {
            width: 80px;
            height: 80px;
            background: var(--gradient-soft);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            color: var(--primary-green);
        }

        .product-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
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
            line-height: 1.4;
        }

        .product-format {
            color: var(--text-light);
            font-size: 0.95em;
            margin-bottom: 1.5rem;
        }

        .badge {
            display: inline-block;
            background: var(--sun-gold);
            color: var(--text-primary);
            padding: 0.25rem 0.75rem;
            border-radius: var(--radius-liquid);
            font-size: 0.8em;
            font-weight: 700;
            margin-bottom: 0.75rem;
            animation: pulse 2s infinite;
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
            background: var(--gradient-hero);
            transform: translateY(-2px);
            box-shadow: var(--shadow-medium);
        }

        .full-catalog-cta {
            text-align: center;
            margin: 4rem 0;
        }

        .cta-button {
            display: inline-flex;
            align-items: center;
            gap: 1rem;
            background: var(--sun-gold);
            color: var(--text-primary);
            text-decoration: none;
            padding: 1.5rem 3rem;
            border-radius: var(--radius-liquid);
            font-size: 1.2em;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: var(--shadow-soft);
        }

        .cta-button:hover {
            background: linear-gradient(135deg, #f4a261 0%, #e76f51 100%);
            transform: translateY(-3px);
            box-shadow: var(--shadow-medium);
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2.2em;
            }

            .products-grid {
                grid-template-columns: 1fr;
            }

            .container {
                padding: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-leaf"></i> LifePlus Catálogo Premium</h1>
            <div class="subtitle">Descubre nuestros productos más populares con imágenes reales</div>
        </div>

        <div class="products-showcase">
            <h2 class="showcase-title">Productos Destacados</h2>
            <p class="showcase-subtitle">Conoce las imágenes reales de nuestros productos más vendidos</p>

            <div class="products-grid">
'''

    # Generar tarjetas de productos con imágenes
    for code, product_info in selected_products.items():
        name = product_info['name']
        price = product_info['price']
        format_info = product_info['format']
        highlight = product_info.get('highlight', '')
        badge = product_info.get('badge', '')

        # URL de la imagen
        img_url = product_images.get(code, {}).get('images', {}).get('main', '')

        # Generar URL de compra
        clean_name = name.lower().replace('®', '').replace(' ', '-').replace('–', '-').replace(':', '').replace('.', '')
        buy_url = f"https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/{code}/{clean_name}"

        html_content += f'''
                <div class="product-card">
                    <div class="product-image-container">
                        {'<div class="product-placeholder"><i class="fas fa-capsules"></i></div>' if not img_url else f'<img src="{img_url}" alt="{name}" class="product-image" onerror="this.parentElement.innerHTML=\'<div class=\\'product-placeholder\\'><i class=\\'fas fa-capsules\\'></i></div>\';">'}
                    </div>

                    <div class="product-header">
                        <span class="product-code">{code}</span>
                        <span class="product-price">{price}</span>
                    </div>

                    {f'<div class="badge">{highlight}</div>' if highlight else ''}
                    {f'<div class="badge">{badge}</div>' if badge else ''}

                    <h3 class="product-name">{name}</h3>
                    <p class="product-format">{format_info}</p>

                    <a href="{buy_url}" target="_blank" class="product-link">
                        <i class="fas fa-shopping-cart"></i>
                        <span>Comprar en Tienda</span>
                    </a>
                </div>
        '''

    html_content += '''
            </div>
        </div>

        <div class="full-catalog-cta">
            <h2 style="font-size: 2.5em; margin-bottom: 1rem; background: var(--lifeplus-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">¿Quieres ver los 118 productos completos?</h2>
            <p style="font-size: 1.2em; color: var(--text-secondary); margin-bottom: 2rem;">
                Explora nuestro catálogo completo con todos los productos LifePlus organizados por categorías
            </p>

            <a href="catalogo_lifeplus_empatizado.html" class="cta-button">
                <i class="fas fa-th-large"></i>
                <span>Ver Catálogo Completo</span>
            </a>

            <a href="https://ww1.lifeplus.com/SHVCB5/S/" target="_blank" class="cta-button" style="margin-left: 1rem; background: var(--lifeplus-gradient); color: white;">
                <i class="fas fa-shopping-bag"></i>
                <span>Tienda Oficial LifePlus</span>
            </a>
        </div>
    </div>

    <script>
        // Animación de entrada para las tarjetas
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observar todas las tarjetas de productos
        document.addEventListener('DOMContentLoaded', () => {
            document.querySelectorAll('.product-card').forEach((card, index) => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(30px)';
                card.style.transition = `all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) ${index * 0.1}s`;
                observer.observe(card);
            });
        });
    </script>
</body>
</html>'''

    return html_content

# Generar el catálogo con imágenes
catalog_html = generate_catalog_with_images()

# Guardar el archivo
with open('catalogo_lifeplus_con_imagenes.html', 'w', encoding='utf-8') as f:
    f.write(catalog_html)

print("✅ Catálogo con imágenes generado exitosamente!")
print("📁 Archivo: catalogo_lifeplus_con_imagenes.html")
print("🎨 Incluye imágenes reales de productos destacados")
print("🔗 Enlaces directos a cada producto")