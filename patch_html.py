import re

with open('catalogo_lifeplus_final.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Nav Button
nav_button_target = '''                <button class="nav-btn" data-category="agua">
                    <i class="fas fa-tint"></i> Agua
                </button>'''
nav_button_replace = '''                <button class="nav-btn" data-category="agua">
                    <i class="fas fa-tint"></i> Agua
                </button>
                <button class="nav-btn" data-category="pets">
                    <i class="fas fa-paw"></i> Pets
                </button>'''
if nav_button_target in html:
    html = html.replace(nav_button_target, nav_button_replace)
else:
    print("nav_button_target not found!")

# 2. Add Category Preview
preview_target = '''                    <div class="category-preview-card" onclick="scrollToCategory('agua')">
                        <div class="category-icon-wrapper">
                            <i class="fas fa-tint"></i>
                        </div>
                        <h3>Agua</h3>
                        <p>Sistemas de purificación</p>
                    </div>
                </div>'''
preview_replace = '''                    <div class="category-preview-card" onclick="scrollToCategory('agua')">
                        <div class="category-icon-wrapper">
                            <i class="fas fa-tint"></i>
                        </div>
                        <h3>Agua</h3>
                        <p>Sistemas de purificación</p>
                    </div>

                    <div class="category-preview-card" onclick="scrollToCategory('pets')">
                        <div class="category-icon-wrapper">
                            <i class="fas fa-paw"></i>
                        </div>
                        <h3>Pets</h3>
                        <p>Nutrición para mascotas</p>
                    </div>
                </div>'''
if preview_target in html:
    html = html.replace(preview_target, preview_replace)
else:
    print("preview_target not found!")

# 3. Add Category Section at the end
section_target = '''        </div>
    </div>

    <script>'''

pets_section = '''
            <div id="pets" class="category-section">
                <div class="category-header">
                    <h2 class="category-title"><i class="fas fa-paw"></i> Pets</h2>
                    <p>7 productos disponibles</p>
                </div>

                <div class="products-grid">
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_6687_1@2x.jpg"
                                 alt="Lifeplus Pets™ Calm"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pets</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">6687</span>
                            <span class="product-price">€0.00</span>
                        </div>
                        <h3 class="product-name">Lifeplus Pets™ Calm</h3>
                        <p class="product-format">90 Masticables (135g)</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/6687/lifeplus-pets-calm" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_6688_1@2x.jpg"
                                 alt="Lifeplus Pets™ Move"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pets</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">6688</span>
                            <span class="product-price">€0.00</span>
                        </div>
                        <h3 class="product-name">Lifeplus Pets™ Move</h3>
                        <p class="product-format">Masticables Blandos</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/6688/lifeplus-pets-move" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_6689_1@2x.jpg"
                                 alt="Lifeplus Pets™ Digest"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pets</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">6689</span>
                            <span class="product-price">€0.00</span>
                        </div>
                        <h3 class="product-name">Lifeplus Pets™ Digest</h3>
                        <p class="product-format">Masticables Blandos</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/6689/lifeplus-pets-digest" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_6692_1@2x.jpg"
                                 alt="Lifeplus Pets™ Peanut Butter Biscuits"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pets</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">6692</span>
                            <span class="product-price">€0.00</span>
                        </div>
                        <h3 class="product-name">Lifeplus Pets™ Peanut Butter Biscuits</h3>
                        <p class="product-format">Galletas</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/6692/lifeplus-pets-peanut-butter-biscuits" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_6697_1@2x.jpg"
                                 alt="Lifeplus Pets™ Care & Comfort"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pets</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">6697</span>
                            <span class="product-price">€0.00</span>
                        </div>
                        <h3 class="product-name">Lifeplus Pets™ Care & Comfort</h3>
                        <p class="product-format">Aerosol</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/6697/lifeplus-pets-care-and-comfort" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_6698_1@2x.jpg"
                                 alt="Lifeplus Pets™ Ahiflower® Oil"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pets</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">6698</span>
                            <span class="product-price">€0.00</span>
                        </div>
                        <h3 class="product-name">Lifeplus Pets™ Ahiflower® Oil</h3>
                        <p class="product-format">Aerosol</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/6698/lifeplus-pets-ahiflower-oil" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar en Tienda</span>
                        </a>
                    </div>
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_PETS-APP_1@2x.jpg"
                                 alt="Lifeplus Pets™ Mobile App"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Pets</text></svg>';">
                        </div>
                        <div class="product-header">
                            <span class="product-code">PETS-APP</span>
                            <span class="product-price">€0.00</span>
                        </div>
                        <h3 class="product-name">Lifeplus Pets™ Mobile App</h3>
                        <p class="product-format">Aplicación Móvil</p>
                        <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/PETS-APP/" target="_blank" class="product-link">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Ver Aplicación</span>
                        </a>
                    </div>
                </div>
            </div>
'''
section_replace = pets_section + section_target

if section_target in html:
    html = html.replace(section_target, section_replace)
else:
    print("section_target not found!")

# 4. Add scrollToCategory mapping if needed
# Wait, scrollToCategory might just use the id. Let's verify.
# Yes, it uses the id of the section.

with open('catalogo_lifeplus_final.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("catalogo_lifeplus_final.html updated!")

