#!/usr/bin/env python3
"""
LifePlus Products Database
Complete product information for catalog generation
"""

PRODUCT_DATABASE = {
    "Nutritional Supplements": [
        {
            'code': '3401',
            'name': 'Daily BioBasics®',
            'format': '786g',
            'price': 86.00,
            'description': 'Premium nutritional foundation with 115+ ingredients including fruits, vegetables, and herbs',
            'benefits': ['Complete nutrition', 'Antioxidant support', 'Digestive health']
        },
        {
            'code': '3400',
            'name': 'Proanthenols® 100',
            'format': '60 tablets',
            'price': 75.75,
            'description': 'High-potency antioxidant formula with Real OPC from grape seed and pine bark extract',
            'benefits': ['Cellular protection', 'Circulatory health', 'Anti-aging']
        },
        {
            'code': '3402',
            'name': 'OmeGold®',
            'format': '60 capsules',
            'price': 47.75,
            'description': 'Premium omega-3 EPA/DHA formula for cardiovascular and brain health',
            'benefits': ['Heart health', 'Brain function', 'Anti-inflammatory']
        },
        {
            'code': '3405',
            'name': 'TVM-Plus',
            'format': '180 tablets',
            'price': 29.75,
            'description': 'Complete multivitamin and multimineral formula for busy lifestyles',
            'benefits': ['Energy support', 'Immune system', 'Daily wellness']
        },
        {
            'code': '3459',
            'name': 'Xtra Antioxidants',
            'format': '120 tablets',
            'price': 67.75,
            'description': 'Comprehensive antioxidant blend with Vitamins C, E and essential minerals',
            'benefits': ['Oxidative stress protection', 'Immune support', 'Cellular health']
        },
        {
            'code': '3406',
            'name': 'Coenzyme Q10',
            'format': '30 capsules',
            'price': 89.00,
            'description': 'High-potency CoQ10 for cellular energy and cardiovascular support',
            'benefits': ['Heart health', 'Energy production', 'Antioxidant protection']
        },
        {
            'code': '3412',
            'name': 'Calcium Magnesium',
            'format': '120 tablets',
            'price': 34.50,
            'description': 'Optimal 2:1 calcium to magnesium ratio with Vitamin D3',
            'benefits': ['Bone health', 'Muscle function', 'Nerve health']
        },
        {
            'code': '3416',
            'name': 'Prostate Formula',
            'format': '60 tablets',
            'price': 95.00,
            'description': 'Comprehensive prostate support with saw palmetto and lycopene',
            'benefits': ['Prostate health', 'Urinary function', 'Hormonal balance']
        }
    ],
    "Proteins & Shakes": [
        {
            'code': '3530',
            'name': 'Lifeplus Triple Protein Shake - Chocolate',
            'format': '867g',
            'price': 87.75,
            'description': 'Premium triple protein formula with whey, casein, and soy proteins',
            'benefits': ['Muscle recovery', 'Sustained energy', 'Complete amino acid profile']
        },
        {
            'code': '3531',
            'name': 'Lifeplus Triple Protein Shake - Vanilla',
            'format': '813g',
            'price': 87.75,
            'description': 'Premium triple protein formula with whey, casein, and soy proteins',
            'benefits': ['Muscle recovery', 'Sustained energy', 'Complete amino acid profile']
        },
        {
            'code': '3442',
            'name': 'Lifeplus Vegan Protein Shake - Chocolate',
            'format': '1235g',
            'price': 93.50,
            'description': 'Complete plant-based protein formula for vegan nutrition',
            'benefits': ['Plant-based protein', 'Digestive enzymes', 'Complete nutrition']
        },
        {
            'code': '3443',
            'name': 'Lifeplus Vegan Protein Shake - Vanilla',
            'format': '1235g',
            'price': 93.50,
            'description': 'Complete plant-based protein formula for vegan nutrition',
            'benefits': ['Plant-based protein', 'Digestive enzymes', 'Complete nutrition']
        },
        {
            'code': '3515',
            'name': 'Protein Plus Bar - Chocolate Peanut Butter',
            'format': '12 bars',
            'price': 55.00,
            'description': 'High-protein nutrition bar with 20g protein per serving',
            'benefits': ['Convenient protein', 'On-the-go nutrition', 'Great taste']
        }
    ],
    "Sports Nutrition": [
        {
            'code': '3434',
            'name': 'BE Focused - Berry',
            'format': '384g',
            'price': 82.25,
            'description': 'Pre-workout mental energy formula with 3g creatine for enhanced focus',
            'benefits': ['Mental clarity', 'Energy boost', 'Enhanced performance']
        },
        {
            'code': '3421',
            'name': 'BE Focused - Citrus',
            'format': '384g',
            'price': 82.25,
            'description': 'Pre-workout mental energy formula with 3g creatine for enhanced focus',
            'benefits': ['Mental clarity', 'Energy boost', 'Enhanced performance']
        },
        {
            'code': '3466',
            'name': 'BE Recharged - Berry',
            'format': '624g',
            'price': 84.75,
            'description': 'Recovery formula with 2:1:1 BCAA ratio for muscle development',
            'benefits': ['Muscle recovery', 'Reduced soreness', 'Lean muscle support']
        },
        {
            'code': '3467',
            'name': 'BE Recharged - Lemon Lime',
            'format': '624g',
            'price': 84.75,
            'description': 'Recovery formula with 2:1:1 BCAA ratio for muscle development',
            'benefits': ['Muscle recovery', 'Reduced soreness', 'Lean muscle support']
        },
        {
            'code': '3524',
            'name': 'BE Energized - Tropical',
            'format': '450g',
            'price': 79.50,
            'description': 'Natural energy formula with electrolytes and B-vitamins',
            'benefits': ['Hydration', 'Natural energy', 'Electrolyte balance']
        }
    ],
    "Superfoods SOLIS": [
        {
            'code': '3483',
            'name': 'SOLIS Green Medley',
            'format': '171g',
            'price': 69.75,
            'description': '27 superfoods blend with adaptogens for natural vitality',
            'benefits': ['Natural energy', 'Stress adaptation', 'Superfood nutrition']
        },
        {
            'code': '3484',
            'name': 'SOLIS Purple Flash®',
            'format': '183g',
            'price': 79.75,
            'description': 'Antioxidant-rich superfruit formula with premium Aronia berries',
            'benefits': ['Antioxidant power', 'Immune support', 'Cellular protection']
        },
        {
            'code': '3485',
            'name': 'SOLIS Cacao Boost',
            'format': '210g',
            'price': 49.50,
            'description': 'Natural energy blend with Reishi mushroom and maca root',
            'benefits': ['Natural stimulation', 'Mental focus', 'Adrenal support']
        },
        {
            'code': '3525',
            'name': 'SOLIS Golden Milk',
            'format': '182g',
            'price': 50.00,
            'description': 'Relaxation formula with premium Ashwagandha KSM-66® for nighttime wellness',
            'benefits': ['Relaxation', 'Sleep support', 'Stress relief']
        }
    ],
    "Forever Young Skincare": [
        {
            'code': '4144',
            'name': 'Forever Young Day Crème SPF 25',
            'format': '50 ml',
            'price': 73.25,
            'description': 'Daily moisturizer with SPF 25 protection and alpine rose extract',
            'benefits': ['Sun protection', 'Hydration', 'Anti-aging']
        },
        {
            'code': '4131',
            'name': 'Forever Young Radiance Serum',
            'format': '30 ml',
            'price': 71.50,
            'description': 'Intensive treatment serum with lifting effect and antioxidants',
            'benefits': ['Firming effect', 'Antioxidant protection', 'Radiant complexion']
        },
        {
            'code': '4132',
            'name': 'Forever Young Rich Moisturizing Crème',
            'format': '50 ml',
            'price': 64.50,
            'description': 'Deep hydration anti-aging formula with natural ingredients',
            'benefits': ['Deep hydration', 'Anti-aging', 'Nourishing']
        },
        {
            'code': '4145',
            'name': 'Forever Young Eye Contour Gel',
            'format': '15 ml',
            'price': 56.75,
            'description': 'Revitalizing eye gel to reduce puffiness and dark circles',
            'benefits': ['Eye area care', 'Reduces puffiness', 'Brightening effect']
        },
        {
            'code': '4133',
            'name': 'Forever Young Night Crème',
            'format': '50 ml',
            'price': 68.00,
            'description': 'Regenerating night cream with peptides and hyaluronic acid',
            'benefits': ['Night regeneration', 'Deep repair', 'Firming']
        }
    ],
    "Personal Care": [
        {
            'code': '4200',
            'name': 'Forever Young Body Lotion',
            'format': '200 ml',
            'price': 45.50,
            'description': 'Luxurious body lotion with natural moisturizers and antioxidants',
            'benefits': ['Body hydration', 'Soft skin', 'Antioxidant protection']
        },
        {
            'code': '4205',
            'name': 'Dental Plus Toothpaste',
            'format': '100 ml',
            'price': 18.00,
            'description': 'Natural toothpaste with enzymes for complete oral care',
            'benefits': ['Oral hygiene', 'Natural ingredients', 'Enzyme protection']
        },
        {
            'code': '4210',
            'name': 'Mouthwash Plus',
            'format': '500 ml',
            'price': 22.00,
            'description': 'Alcohol-free mouthwash with natural antiseptics',
            'benefits': ['Fresh breath', 'Gum health', 'Alcohol-free']
        }
    ],
    "Accessories": [
        {
            'code': '7001',
            'name': 'Shaker Bottle',
            'format': '750 ml',
            'price': 12.00,
            'description': 'Premium quality shaker bottle with mixing ball',
            'benefits': ['Easy mixing', 'BPA-free', 'Durable design']
        },
        {
            'code': '7002',
            'name': 'Pill Organizer',
            'format': '7 compartments',
            'price': 8.50,
            'description': 'Weekly pill organizer with clear compartments',
            'benefits': ['Daily organization', 'Portable', 'Easy to use']
        },
        {
            'code': '7003',
            'name': 'Measuring Scoop Set',
            'format': '3 sizes',
            'price': 6.00,
            'description': 'Precision measuring scoops for powder supplements',
            'benefits': ['Accurate dosing', 'Multiple sizes', 'Food grade']
        }
    ],
    "Water Filtration Systems": [
        {
            'code': '8001',
            'name': 'Pure Water Pitcher',
            'format': '2.5 L',
            'price': 45.00,
            'description': 'Advanced water filtration pitcher with multi-stage filtration',
            'benefits': ['Clean water', 'Removes contaminants', 'Improves taste']
        },
        {
            'code': '8002',
            'name': 'Pure Water Replacement Filters',
            'format': '3 pack',
            'price': 35.00,
            'description': 'Replacement filters for Pure Water system',
            'benefits': ['Continued filtration', 'Easy replacement', '3-month supply']
        },
        {
            'code': '8003',
            'name': 'Pure Water Faucet Filter',
            'format': 'Universal fit',
            'price': 65.00,
            'description': 'Direct faucet water filtration system',
            'benefits': ['Instant filtration', 'Space-saving', 'Universal fit']
        }
    ],
    "Recommendation Packs": [
        {
            'code': '9001',
            'name': 'Wellness Starter Pack',
            'format': 'Complete kit',
            'price': 245.00,
            'description': 'Essential daily nutrition kit for beginners',
            'benefits': ['Complete foundation', 'Daily essentials', 'Great value']
        },
        {
            'code': '9002',
            'name': 'Athlete Performance Pack',
            'format': 'Sports kit',
            'price': 320.00,
            'description': 'Comprehensive sports nutrition package',
            'benefits': ['Peak performance', 'Recovery support', 'Energy enhancement']
        },
        {
            'code': '9003',
            'name': 'Anti-Aging Beauty Pack',
            'format': 'Skincare kit',
            'price': 285.00,
            'description': 'Complete anti-aging skincare regimen',
            'benefits': ['Complete skincare', 'Anti-aging focus', 'Premium ingredients']
        }
    ],
    "Pets": [
        {
            'code': '6687',
            'name': 'Lifeplus Pets™ Calm',
            'format': '90 Masticables (135g)',
            'price': 0.00,
            'description': 'Masticables Blandos para Soporte de Comportamiento Avanzado. Promueve el equilibrio del comportamiento y el bienestar general.',
            'benefits': ['Equilibrio de comportamiento', 'Bienestar general', 'Ingredientes naturales']
        },
        {
            'code': '6688',
            'name': 'Lifeplus Pets™ Move',
            'format': 'Masticables Blandos',
            'price': 0.00,
            'description': 'Masticables Blandos para soporte avanzado de las articulaciones en cada etapa de la vida.',
            'benefits': ['Salud articular', 'Soporte de movilidad', 'Para todas las edades']
        },
        {
            'code': '6689',
            'name': 'Lifeplus Pets™ Digest',
            'format': 'Masticables Blandos',
            'price': 0.00,
            'description': 'Masticables Blandos para la Salud Digestiva. Promueve un intestino equilibrado y facilita la digestión.',
            'benefits': ['Salud digestiva', 'Intestino equilibrado', 'Fácil digestión']
        },
        {
            'code': '6692',
            'name': 'Lifeplus Pets™ Peanut Butter Biscuits',
            'format': 'Galletas',
            'price': 0.00,
            'description': 'Una deliciosa y saludable golosina para tu perro con sabor a crema de cacahuete.',
            'benefits': ['Golosina nutritiva', 'Ingredientes naturales', 'Sabor delicioso']
        },
        {
            'code': '6697',
            'name': 'Lifeplus Pets™ Care & Comfort',
            'format': 'Aerosol',
            'price': 0.00,
            'description': 'Defensa Segura y Calmante Contra las Pulgas y Garrapatas. Fórmula no tóxica con aceites naturales.',
            'benefits': ['Protección contra pulgas', 'Defensa contra garrapatas', 'Fórmula no tóxica']
        },
        {
            'code': '6698',
            'name': 'Lifeplus Pets™ Ahiflower® Oil',
            'format': 'Aerosol',
            'price': 0.00,
            'description': 'Apoyo avanzado para la piel y el pelaje con aceite de Ahiflower®. Rico en Omega-3 y Omega-6.',
            'benefits': ['Piel hidratada', 'Pelaje brillante', 'Soporte antioxidante']
        },
        {
            'code': 'PETS-APP',
            'name': 'Lifeplus Pets™ Mobile App',
            'format': 'Aplicación Móvil',
            'price': 0.00,
            'description': 'Aplicación móvil para realizar el seguimiento del bienestar y nutrición de tu mascota.',
            'benefits': ['Seguimiento digital', 'Recordatorios', 'Gestión de salud']
        }
    ]
}

def get_total_products():
    """Get total number of products across all categories"""
    return sum(len(products) for products in PRODUCT_DATABASE.values())

def get_price_range():
    """Get minimum and maximum product prices"""
    all_prices = []
    for products in PRODUCT_DATABASE.values():
        all_prices.extend([p['price'] for p in products])
    return min(all_prices), max(all_prices)

def get_categories():
    """Get list of all category names"""
    return list(PRODUCT_DATABASE.keys())