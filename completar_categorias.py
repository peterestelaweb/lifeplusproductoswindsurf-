#!/usr/bin/env python3

# Productos completos del catálogo LifePlus organizados por categorías

products_by_category = {
    'nutricionales': [
        {"code": "3401", "name": "Daily BioBasics®", "price": "€86.00", "format": "786g"},
        {"code": "3424", "name": "Daily BioBasics® Light", "price": "€73.75", "format": "378g"},
        {"code": "3427", "name": "Daily BioBasics® Veggie Caps", "price": "€115.50", "format": "480 cápsulas"},
        {"code": "3405", "name": "TVM Plus", "price": "€29.75", "format": "180 tabletas"},
        {"code": "3452", "name": "TVM Plus (sin yodo)", "price": "€32.00", "format": "180 tabletas"},
        {"code": "3413", "name": "Vitamin C-Plus", "price": "€34.75", "format": "300 tabletas"},
        {"code": "3414", "name": "Vitamins D&K", "price": "€21.50", "format": "60 tabletas"},
        {"code": "3462", "name": "Vitamin E-Complex", "price": "€43.50", "format": "60 cápsulas"},
        {"code": "3437", "name": "Micro Mins Plus", "price": "€51.50", "format": "60 tabletas"},
        {"code": "3400", "name": "Proanthenols® 100", "price": "€75.75", "format": "60 tabletas"},
        {"code": "3420", "name": "Proanthenols® 50 (pequeño)", "price": "€43.50", "format": "60 tabletas"},
        {"code": "3471", "name": "Proanthenols® 50 (grande)", "price": "€161.00", "format": "240 tabletas"},
        {"code": "3544", "name": "Proanthenols® 200 SV", "price": "€77.50", "format": "30 cápsulas"},
        {"code": "3459", "name": "Xtra Antioxidants", "price": "€67.75", "format": "120 tabletas"},
        {"code": "3455", "name": "Co Q-10 Plus", "price": "€78.00", "format": "60 cápsulas"},
        {"code": "3435", "name": "Ubiquinol 100 (30ct)", "price": "€77.00", "format": "30 cápsulas"},
        {"code": "3487", "name": "Ubiquinol 100 (60ct)", "price": "€125.50", "format": "60 cápsulas"},
        {"code": "3467", "name": "Heart Formula", "price": "€104.00", "format": "300 tabletas"},
        {"code": "3448", "name": "Circulation Formula", "price": "€55.00", "format": "180 tabletas"},
        {"code": "3441", "name": "RYR Plus", "price": "€38.50", "format": "180 tabletas"},
        {"code": "3482", "name": "Digestive Formula", "price": "€48.50", "format": "90 tabletas"},
        {"code": "3412", "name": "Biotic Blast®", "price": "€43.50", "format": "60 cápsulas"},
        {"code": "3426", "name": "Aloe Vera Caps", "price": "€60.50", "format": "60 cápsulas"},
        {"code": "3415", "name": "Phase'oMine", "price": "€61.50", "format": "180 tabletas"},
        {"code": "3454", "name": "D Mannose Plus", "price": "€61.00", "format": "120 tabletas"},
        {"code": "3410", "name": "Joint Formula", "price": "€37.00", "format": "120 tabletas"},
        {"code": "3430", "name": "CalMag Plus", "price": "€44.00", "format": "300 tabletas"},
        {"code": "3447", "name": "Iron Plus", "price": "€37.50", "format": "60 tabletas"},
        {"code": "3439", "name": "Immune Formula", "price": "€68.75", "format": "120 tabletas"},
        {"code": "3486", "name": "Zinc Boost", "price": "€50.00", "format": "120 tabletas"},
        {"code": "3438", "name": "Brain Formula", "price": "€87.00", "format": "180 tabletas"},
        {"code": "3423", "name": "Eye Formula", "price": "€31.25", "format": "60 tabletas"},
        {"code": "3402", "name": "OmeGold®", "price": "€47.75", "format": "60 cápsulas"},
        {"code": "3425", "name": "Vegan OmeGold®", "price": "€51.75", "format": "60 cápsulas"},
        {"code": "3431", "name": "EPA Plus", "price": "€27.50", "format": "90 cápsulas"},
        {"code": "3416", "name": "Evening Primrose Oil", "price": "€15.50", "format": "60 cápsulas"},
        {"code": "3422", "name": "Lyprinex (60ct)", "price": "€52.25", "format": "60 cápsulas"},
        {"code": "3488", "name": "Lyprinex (180ct)", "price": "€121.00", "format": "180 cápsulas"},
        {"code": "3489", "name": "mangOmega", "price": "€47.25", "format": "355 ml"},
        {"code": "3456", "name": "Women's Gold Formula", "price": "€34.00", "format": "60 tabletas"},
        {"code": "3444", "name": "Lifeplus Menaplus®", "price": "€87.50", "format": "240 tabletas"},
        {"code": "3538", "name": "Parabalance", "price": "€52.75", "format": "180 tabletas"},
        {"code": "3460", "name": "Men's Gold Formula", "price": "€34.00", "format": "60 tabletas"},
        {"code": "3445", "name": "Men's Formula", "price": "€65.00", "format": "120 tabletas"},
        {"code": "3440", "name": "Lifeplus Enerxan®", "price": "€28.50", "format": "60 tabletas"},
        {"code": "3533", "name": "Real NRG", "price": "€48.50", "format": "817g"},
        {"code": "3408", "name": "X Cell", "price": "€73.75", "format": "274g"},
        {"code": "3406", "name": "X Cell+", "price": "€75.00", "format": "336g"},
        {"code": "3417", "name": "Somazyme", "price": "€52.00", "format": "120 tabletas"},
        {"code": "3407", "name": "FY® Skin Formula", "price": "€73.75", "format": "60 tabletas"},
        {"code": "3436", "name": "Fusions Red", "price": "€43.50", "format": "60 cápsulas"},
        {"code": "3472", "name": "Vita Saurus®", "price": "€55.00", "format": "180 tabletas"},
        {"code": "3433", "name": "Yummies", "price": "€42.25", "format": "200 tabletas"},
        {"code": "3428", "name": "Support Tabs Plus", "price": "€64.25", "format": "240 tabletas"},
        {"code": "3443", "name": "Kompakt Plus", "price": "€24.25", "format": "60 tabletas"},
        {"code": "3842", "name": "Key Tonic®", "price": "€79.25", "format": "150g"},
        {"code": "3418", "name": "Cogelin®", "price": "€52.75", "format": "762g"},
        {"code": "3409", "name": "Lifeplus Discovery®", "price": "€147.50", "format": "30 tabletas"},
        {"code": "3446", "name": "PH Plus", "price": "€41.25", "format": "270 tabletas"},
        {"code": "4619", "name": "PH Plus tiras de test", "price": "€9.75", "format": "1 unidad"}
    ],

    'proteinas': [
        {"code": "3530", "name": "Lifeplus Triple Protein Shake: Chocolate", "price": "€87.75", "format": "867g"},
        {"code": "3547", "name": "Lifeplus Triple Protein Shake: Chocolate (sin edulcorante)", "price": "€87.75", "format": "867g"},
        {"code": "3531", "name": "Lifeplus Triple Protein Shake: Vainilla", "price": "€87.75", "format": "813g"},
        {"code": "3532", "name": "Lifeplus Triple Protein Shake: Vainilla (sin edulcorante)", "price": "€87.75", "format": "813g"},
        {"code": "3442", "name": "Lifeplus Vegan Protein Shake: Chocolate", "price": "€93.50", "format": "1235g"},
        {"code": "3464", "name": "Lifeplus Vegan Protein Shake: Vainilla", "price": "€93.50", "format": "1232g"},
        {"code": "1800", "name": "Smart Bar", "price": "€37.25", "format": "12 x 50g"}
    ],

    'deportiva': [
        {"code": "3434", "name": "Be Focused – Frutos del bosque", "price": "€82.25", "format": "384g"},
        {"code": "3421", "name": "Be Focused – Cítricos", "price": "€82.25", "format": "384g"},
        {"code": "4145", "name": "Be Focused en sobres – Frutos del bosque", "price": "€95.75", "format": "30 x 13.4g"},
        {"code": "4146", "name": "Be Focused en sobres – Cítricos", "price": "€95.75", "format": "30 x 13.4g"},
        {"code": "3470", "name": "Be Sustained – Frutos del bosque", "price": "€83.50", "format": "663g"},
        {"code": "3461", "name": "Be Sustained – Cítricos", "price": "€83.50", "format": "663g"},
        {"code": "4147", "name": "Be Sustained en sobres – Frutos del bosque", "price": "€102.25", "format": "30 x 22.3g"},
        {"code": "4148", "name": "Be Sustained en sobres – Cítricos", "price": "€102.25", "format": "30 x 22.3g"},
        {"code": "3466", "name": "Be Recharged – Frutos del bosque", "price": "€84.75", "format": "624g"},
        {"code": "3449", "name": "Be Recharged – Cítricos", "price": "€84.75", "format": "624g"},
        {"code": "4149", "name": "Be Recharged en sobres – Frutos del bosque", "price": "€99.00", "format": "30 x 20.8g"},
        {"code": "4150", "name": "Be Recharged en sobres – Cítricos", "price": "€99.00", "format": "30 x 20.8g"},
        {"code": "4158", "name": "Be Refueled – Sabor a Chocolate", "price": "€81.50", "format": "804g"},
        {"code": "4156", "name": "Be Refueled – Sabor a Vainilla", "price": "€81.50", "format": "804g"},
        {"code": "4157", "name": "Be Refueled – Sabor específico", "price": "€81.50", "format": "804g"}
    ],

    'superfoods': [
        {"code": "3483", "name": "SOLIS Green Medley", "price": "€69.75", "format": "171g"},
        {"code": "3484", "name": "SOLIS Purple Flash®", "price": "€79.75", "format": "183g"},
        {"code": "3485", "name": "SOLIS Cacao Boost", "price": "€49.50", "format": "210g"},
        {"code": "3525", "name": "SOLIS Golden Milk", "price": "€50.00", "format": "182g"}
    ],

    'forever-young': [
        {"code": "4144", "name": "Forever Young Day Crème SPF 25", "price": "€73.25", "format": "50 ml"},
        {"code": "4129", "name": "Forever Young Gentle Cream Cleanser", "price": "€32.00", "format": "150 ml"},
        {"code": "4130", "name": "Forever Young Rejuvenating Eye Crème", "price": "€29.25", "format": "15 ml"},
        {"code": "4131", "name": "Forever Young Radiance Serum", "price": "€71.50", "format": "30 ml"},
        {"code": "4132", "name": "Forever Young Rich Moisturizing Crème", "price": "€64.50", "format": "50 ml"},
        {"code": "4133", "name": "Forever Young Strengthen and Restore Shampoo", "price": "€18.75", "format": "250 ml"},
        {"code": "4134", "name": "Forever Young Repair and Protect Conditioner", "price": "€35.75", "format": "250 ml"}
    ],

    'personal': [
        {"code": "6695", "name": "Pasta dentífrica del árbol del té (sin flúor)", "price": "€20.25", "format": "170g"},
        {"code": "1021", "name": "MSM Plus Vital Care Lotion", "price": "€26.50", "format": "242 ml"},
        {"code": "6134", "name": "Lifeplus Wonder Gel", "price": "€38.00", "format": "114 ml"},
        {"code": "6654", "name": "Natural Gold Hand & Body Bar", "price": "€7.75", "format": "113g"},
        {"code": "2632", "name": "Natural Hand Cream", "price": "€24.25", "format": "100 ml"},
        {"code": "2631", "name": "Natural Body Wash", "price": "€17.00", "format": "500 ml"},
        {"code": "2630", "name": "Natural Hand & Body Lotion", "price": "€21.75", "format": "300 ml"},
        {"code": "2629", "name": "Natural Hand Wash", "price": "€18.25", "format": "500 ml"},
        {"code": "2633", "name": "Natural Deodorant", "price": "€20.25", "format": "100g"}
    ],

    'accesorios': [
        {"code": "6074", "name": "Botella mezcladora", "price": "€4.00", "format": "1 unidad"},
        {"code": "7890", "name": "Cinta para medir", "price": "€10.75", "format": "1 unidad"},
        {"code": "2178", "name": "Juego de cucharas de madera", "price": "€23.00", "format": "1 unidad"}
    ],

    'agua': [
        {"code": "1496", "name": "Modelo de encimero pequeño", "price": "€439.25", "format": "Sistema de filtrado"},
        {"code": "1497", "name": "Modelo bajo el fregadero pequeño", "price": "€576.25", "format": "Sistema de filtrado"}
    ],

    'packs': [
        {"code": "3502", "name": "Maintain & Protect 50", "price": "€123.00", "format": "Pack recomendado"},
        {"code": "3503", "name": "Maintain & Protect 50 Gold", "price": "€168.50", "format": "Pack premium"},
        {"code": "3504", "name": "Maintain & Protect 100", "price": "€153.75", "format": "Pack recomendado"},
        {"code": "3505", "name": "Maintain & Protect 100 Gold", "price": "€199.00", "format": "Pack premium"},
        {"code": "3506", "name": "Maintain & Protect 100 Gold Light", "price": "€187.50", "format": "Pack premium ligero"},
        {"code": "3507", "name": "Maintain & Protect VEGAN", "price": "€165.00", "format": "Pack vegano"}
    ]
}

def get_category_name(category):
    names = {
        'nutricionales': 'Productos Nutricionales',
        'proteinas': 'Proteínas y Shakes',
        'deportiva': 'Nutrición Deportiva',
        'superfoods': 'Superfoods Solis',
        'forever-young': 'Forever Young',
        'personal': 'Cuidado Personal',
        'accesorios': 'Accesorios',
        'agua': 'Sistemas de Filtrado de Agua',
        'packs': 'Packs de Recomendación'
    }
    return names.get(category, category.title())

def get_category_icon(category):
    icons = {
        'nutricionales': 'capsules',
        'proteinas': 'dumbbell',
        'deportiva': 'running',
        'superfoods': 'seedling',
        'forever-young': 'spa',
        'personal': 'hand-sparkles',
        'accesorios': 'toolbox',
        'agua': 'tint',
        'packs': 'gift'
    }
    return icons.get(category, 'leaf')

# Función para generar HTML de un producto
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

    return f'''
                    <div class="product-card">
                        <div class="product-image-container">
                            <img src="https://ww1.lifeplus.com/images/products/prodpic_{code}_1@2x.jpg"
                                 alt="{name}"
                                 class="product-image"
                                 onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=&quot;http://www.w3.org/2000/svg&quot; width=&quot;80&quot; height=&quot;80&quot; viewBox=&quot;0 0 80 80&quot;><rect width=&quot;80&quot; height=&quot;80&quot; fill=&quot;%23f0f0f0&quot;/><text x=&quot;40&quot; y=&quot;40&quot; text-anchor=&quot;middle&quot; dy=&quot;0.3em&quot; font-family=&quot;Arial&quot; font-size=&quot;10&quot; fill=&quot;%23666&quot;>{placeholder_text}</text></svg>';">
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

# Generar HTML para todas las categorías
for category, products in products_by_category.items():
    print(f"// Categoría: {category}")
    print(f"// Total: {len(products)} productos")

    # Calcular total y estadísticas
    total_value = sum(float(price.replace('€', '').replace(',', '.')) for price in [p['price'] for p in products])

    print(f'<div id="{category}" class="category-section">')
    print(f'    <div class="category-header">')
    print(f'        <h2 class="category-title"><i class="fas fa-{get_category_icon(category)}"></i> {get_category_name(category)}</h2>')
    print(f'        <p class="category-subtitle">{len(products)} productos disponibles</p>')
    print(f'        <div class="category-stats">')
    print(f'            <div class="category-stat">')
    print(f'                <span class="category-stat-number">{len(products)}</span>')
    print(f'                <span class="category-stat-label">Disponibles</span>')
    print(f'            </div>')
    print(f'            <div class="category-stat">')
    print(f'                <span class="category-stat-number">€{total_value:.2f}</span>')
    print(f'                <span class="category-stat-label">Valor Total</span>')
    print(f'            </div>')
    print(f'        </div>')
    print(f'    </div>')
    print(f'')
    print(f'    <div class="products-grid">')

    for product in products:
        print(generate_product_html(product))

    print(f'    </div>')
    print(f'</div>')
    print(f'')

if __name__ == "__main__":
    print("HTML generado correctamente")