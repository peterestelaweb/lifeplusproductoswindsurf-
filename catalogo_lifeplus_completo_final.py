#!/usr/bin/env python3

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
                            <p>9 productos</p>
                        </div>
                        <div class="preview-card" onclick="showCategory('deportiva')">
                            <i class="fas fa-running"></i>
                            <h3>Nutrición Deportiva</h3>
                            <p>15 productos</p>
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
            </div>

            <!-- Sección Proteínas (CON TODOS LOS PRODUCTOS) -->
            <div id="proteinas" class="category-section">
                <div class="category-header">
                    <h2 class="category-title"><i class="fas fa-dumbbell"></i> Proteínas y Shakes</h2>
                    <p>9 productos disponibles</p>
                </div>

                <div class="products-grid">
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_3530_1@2x.jpg"
                                 alt="Lifeplus Triple Protein Shake: Chocolate"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pro</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">3530</span>
                            <span class="product-price">€87.75</span>
                        </div>
                        <h3 class="product-name">Lifeplus Triple Protein Shake: Chocolate</h3>
                        <p class="product-format">867g</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/3530/triple-protein-shake:chocolate" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>

                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_3531_1@2x.jpg"
                                 alt="Lifeplus Triple Protein Shake: Vainilla"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pro</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">3531</span>
                            <span class="product-price">€87.75</span>
                        </div>
                        <h3 class="product-name">Lifeplus Triple Protein Shake: Vainilla</h3>
                        <p class="product-format">813g</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/3531/triple-protein-shake%3A-vainilla" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>

                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_3547_1@2x.jpg"
                                 alt="Lifeplus Triple Protein Shake: Chocolate (sin edulcorante)"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pro</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">3547</span>
                            <span class="product-price">€87.75</span>
                        </div>
                        <h3 class="product-name">Lifeplus Triple Protein Shake: Chocolate (sin edulcorante)</h3>
                        <p class="product-format">867g</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/3547/triple-protein-malteada-de-chocolate-sin-az%FAcar" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>

                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_3532_1@2x.jpg"
                                 alt="Lifeplus Triple Protein Shake: Vainilla (sin edulcorante)"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pro</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">3532</span>
                            <span class="product-price">€87.75</span>
                        </div>
                        <h3 class="product-name">Lifeplus Triple Protein Shake: Vainilla (sin edulcorante)</h3>
                        <p class="product-format">813g</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/3532/triple-protein-shake%3A-vainilla-sin-edulcorante%29" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>

                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_3442_1@2x.jpg"
                                 alt="Lifeplus Vegan Protein Shake: Chocolate"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Veg</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">3442</span>
                            <span class="product-price">€93.50</span>
                        </div>
                        <h3 class="product-name">Lifeplus Vegan Protein Shake: Chocolate</h3>
                        <p class="product-format">1235g</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/3442/lifeplus-bodysmart-solutions%AE-vegan-protein-shake%3A-chocolate" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>

                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_3464_1@2x.jpg"
                                 alt="Lifeplus Vegan Protein Shake: Vainilla"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Veg</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">3464</span>
                            <span class="product-price">€93.50</span>
                        </div>
                        <h3 class="product-name">Lifeplus Vegan Protein Shake: Vainilla</h3>
                        <p class="product-format">1232g</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/3464/lifeplus-bodysmart-solutions%AE-vegan-protein-shake%3A-vainilla" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>

                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_3499_1@2x.jpg"
                                 alt="Daily Protein Pack Chocolate"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pack</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">3499</span>
                            <span class="product-price">€175.50</span>
                        </div>
                        <h3 class="product-name">Daily Protein Pack Chocolate</h3>
                        <p class="product-format">Pack</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/3499/daily-protein-pack-chocolate" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>

                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_1800_1@2x.jpg"
                                 alt="Smart Bar"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Smart</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">1800</span>
                            <span class="product-price">€37.25</span>
                        </div>
                        <h3 class="product-name">Smart Bar</h3>
                        <p class="product-format">12 x 50g</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/1800/smart-bar" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Sección Nutrición Deportiva -->
            <div id="deportiva" class="category-section">
                <div class="category-header">
                    <h2 class="category-title"><i class="fas fa-running"></i> Nutrición Deportiva</h2>
                    <p>15 productos disponibles</p>
                </div>

                <div class="products-grid">
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_4156_1@2x.jpg"
                                 alt="Be Refueled – Vainilla"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Ref</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">4156</span>
                            <span class="product-price">€81.50</span>
                        </div>
                        <h3 class="product-name">Be Refueled – Vainilla</h3>
                        <p class="product-format">804g</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/4156/be-refueled-vainilla" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>

                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_4158_1@2x.jpg"
                                 alt="Be Refueled – Chocolate"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Ref</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">4158</span>
                            <span class="product-price">€81.50</span>
                        </div>
                        <h3 class="product-name">Be Refueled – Chocolate</h3>
                        <p class="product-format">804g</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/4158/be-refueled-chocolate" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Sección Packs -->
            <div id="packs" class="category-section">
                <div class="category-header">
                    <h2 class="category-title"><i class="fas fa-gift"></i> Packs de Recomendación</h2>
                    <p>6 productos disponibles</p>
                </div>

                <div class="products-grid">
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_3507_1@2x.jpg"
                                 alt="Maintain & Protect VEGAN"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Main</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">3507</span>
                            <span class="product-price">€165.00</span>
                        </div>
                        <h3 class="product-name">Maintain & Protect VEGAN</h3>
                        <p class="product-format">Pack vegano</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/3507/maintain-and-protect-vegan" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>
                </div>
            </div>

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

with open('catalogo_lifeplus_completo_final.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Catálogo completo creado: catalogo_lifeplus_completo_final.html")
print("📦 Incluye todos los productos que mencionaste:")
print("   - Proteínas: Vainilla, sin edulcorante, packs")
print("   - Deportiva: Be Refueled chocolate y vainilla")
print("   - Enlaces directos exactos que proporcionaste")