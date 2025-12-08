#!/usr/bin/env python3
"""
Generador de URLs de imágenes de productos LifePlus
Basado en el patrón descubierto: https://ww1.lifeplus.com/images/products/prodpic_[CODE]_1@2x.jpg
"""

import json
import os

def generate_product_image_urls():
    """
    Genera URLs de imágenes para todos los productos LifePlus del catálogo
    """

    # Lista completa de productos con sus códigos
    products = {
        # Nutricionales
        '3401': 'Daily BioBasics®',
        '3424': 'Daily BioBasics® Light',
        '3427': 'Daily BioBasics® Veggie Caps',
        '3405': 'TVM Plus',
        '3452': 'TVM Plus sin yodo',
        '3413': 'Vitamin C-Plus',
        '3414': 'Vitamins D&K',
        '3462': 'Vitamin E-Complex',
        '3437': 'Micro Mins Plus',
        '3400': 'Proanthenols® 100',
        '3420': 'Proanthenols® 50 pequeño',
        '3471': 'Proanthenols® 50 grande',
        '3544': 'Proanthenols® 200 SV',
        '3459': 'Xtra Antioxidants',
        '3455': 'Co Q-10 Plus',
        '3435': 'Ubiquinol 100 30ct',
        '3487': 'Ubiquinol 100 60ct',
        '3467': 'Heart Formula',
        '3448': 'Circulation Formula',
        '3441': 'RYR Plus',
        '3482': 'Digestive Formula',
        '3412': 'Biotic Blast®',
        '3426': 'Aloe Vera Caps',
        '3415': 'PhaseoMine',
        '3454': 'D Mannose Plus',
        '3410': 'Joint Formula',
        '3430': 'CalMag Plus',
        '3447': 'Iron Plus',
        '3439': 'Immune Formula',
        '3486': 'Zinc Boost',
        '3438': 'Brain Formula',
        '3423': 'Eye Formula',
        '3402': 'OmeGold®',
        '3425': 'Vegan OmeGold®',
        '3431': 'EPA Plus',
        '3416': 'Evening Primrose Oil',
        '3422': 'Lyprinex 60ct',
        '3488': 'Lyprinex 180ct',
        '3489': 'mangOmega',
        '3456': 'Women Gold Formula',
        '3444': 'Lifeplus Menaplus®',
        '3538': 'Parabalance',
        '3460': 'Men Gold Formula',
        '3445': 'Men Formula',
        '3440': 'Lifeplus Enerxan®',
        '3533': 'Real NRG',
        '3408': 'X Cell',
        '3406': 'X Cell+',
        '3417': 'Somazyme',
        '3407': 'FY® Skin Formula',
        '3436': 'Fusions Red',
        '3472': 'Vita Saurus®',
        '3433': 'Yummies',
        '3428': 'Support Tabs Plus',
        '3443': 'Kompakt Plus',
        '3842': 'Key Tonic®',
        '3418': 'Cogelin®',
        '3409': 'Lifeplus Discovery®',
        '3446': 'PH Plus',
        '4619': 'PH Plus tiras de test',

        # Proteínas y Shakes
        '3530': 'Lifeplus Triple Protein Shake Chocolate',
        '3547': 'Lifeplus Triple Protein Shake Chocolate sin edulcorante',
        '3531': 'Lifeplus Triple Protein Shake Vainilla',
        '3532': 'Lifeplus Triple Protein Shake Vainilla sin edulcorante',
        '3442': 'Lifeplus Vegan Protein Shake Chocolate',
        '3464': 'Lifeplus Vegan Protein Shake Vainilla',
        '1800': 'Smart Bar',

        # Nutrición Deportiva
        '3434': 'Be Focused frutos del bosque',
        '3421': 'Be Focused citricos',
        '4145': 'Be Focused sobres frutos del bosque',
        '4146': 'Be Focused sobres citricos',
        '3470': 'Be Sustained frutos del bosque',
        '3461': 'Be Sustained citricos',
        '4147': 'Be Sustained sobres frutos del bosque',
        '4148': 'Be Sustained sobres citricos',
        '3466': 'Be Recharged frutos del bosque',
        '3449': 'Be Recharged citricos',
        '4149': 'Be Recharged sobres frutos del bosque',
        '4150': 'Be Recharged sobres citricos',
        '4158': 'Be Refueled Chocolate',
        '4156': 'Be Refueled Vainilla',
        '4157': 'Be Refueled sabor especifico',

        # Superfoods Solis
        '3483': 'SOLIS Green Medley',
        '3484': 'SOLIS Purple Flash®',
        '3485': 'SOLIS Cacao Boost',
        '3525': 'SOLIS Golden Milk',

        # Forever Young
        '4144': 'Forever Young Day Crème SPF 25',
        '4129': 'Forever Young Gentle Cream Cleanser',
        '4130': 'Forever Young Rejuvenating Eye Crème',
        '4131': 'Forever Young Radiance Serum',
        '4132': 'Forever Young Rich Moisturizing Crème',
        '4133': 'Forever Young Strengthen and Restore Shampoo',
        '4134': 'Forever Young Repair and Protect Conditioner',

        # Cuidado Personal
        '6695': 'Pasta dentifrica del arbol del te sin fluor',
        '1021': 'MSM Plus Vital Care Lotion',
        '6134': 'Lifeplus Wonder Gel',
        '6654': 'Natural Gold Hand Body Bar',
        '2632': 'Natural Hand Cream',
        '2631': 'Natural Body Wash',
        '2630': 'Natural Hand Body Lotion',
        '2629': 'Natural Hand Wash',
        '2633': 'Natural Deodorant',

        # Accesorios
        '6074': 'Botella mezcladora',
        '7890': 'Cinta para medir',
        '2178': 'Juego de cucharas de madera',

        # Sistemas de Filtrado de Agua
        '1496': 'Modelo de encimera pequeno',
        '1497': 'Modelo bajo el fregadero pequeno',

        # Packs de Recomendación
        '3502': 'Maintain Protect 50',
        '3503': 'Maintain Protect 50 Gold',
        '3504': 'Maintain Protect 100',
        '3505': 'Maintain Protect 100 Gold',
        '3506': 'Maintain Protect 100 Gold Light',
        '3507': 'Maintain Protect VEGAN'
    }

    base_url = "https://ww1.lifeplus.com/images/products"
    product_images = {}

    for code, name in products.items():
        # Generar URLs para diferentes tamaños
        image_urls = {
            'main': f"{base_url}/prodpic_{code}_1@2x.jpg",
            'thumbnail': f"{base_url}/prodpic_{code}_1_thumb.jpg",
            'backup_1': f"{base_url}/prodpic_{code}_1@2x.jpg",
            'backup_2': f"{base_url}/prodpic_{code}_2@2x.jpg",
            'backup_3': f"{base_url}/prodpic_{code}_3@2x.jpg"
        }

        product_images[code] = {
            'name': name,
            'images': image_urls
        }

    return product_images

def save_product_images_json():
    """
    Guarda las URLs de imágenes en un archivo JSON
    """
    product_images = generate_product_image_urls()

    with open('product_images.json', 'w', encoding='utf-8') as f:
        json.dump(product_images, f, indent=2, ensure_ascii=False)

    print(f"✅ Generadas URLs de imágenes para {len(product_images)} productos")
    print(f"📁 Guardado en: product_images.json")

    return product_images

if __name__ == "__main__":
    save_product_images_json()