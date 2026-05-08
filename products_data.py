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
    ],

    'nuevos': [
        {'code': '7890', 'name': 'Lifeplus Bodysmart Solutions® Cinta para medir', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3427', 'name': 'Daily BioBasics® Veggie Caps', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3519', 'name': 'Sport Pack - En bote - Cítricos', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3507', 'name': 'Maintain, Protect & Satisfy - Chocolate', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4619', 'name': 'pH Plus Test Strips', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2733', 'name': 'Manta con capucha', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3430', 'name': 'CalMag Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2629', 'name': 'Natural Hand Wash', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2205', 'name': 'Folleto de Lifeplus FR', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3546', 'name': 'OmegAhi Peach Mango', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3516', 'name': 'Everyday wellbeing Gold sin yodo', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '1496', 'name': 'Sistema de filtro de agua potable, Modelo de encimera - pequeño (MP400 SSCT)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3538', 'name': 'Parabalance', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3534', 'name': 'Lifeplus Pets® Calm', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '6695', 'name': 'Lifeplus Tea Tree Toothpaste 170g/6 oz', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2749', 'name': 'Cuaderno de tapa dura', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3536', 'name': 'Lifeplus Pets® Digest', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3426', 'name': 'Aloe Vera Caps', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2735', 'name': 'Funda para portátil', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3472', 'name': 'Vita-Saurus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3513', 'name': 'Everyday Wellbeing', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3409', 'name': 'Lifeplus Discovery®', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2499', 'name': 'Calcetines deportivos negros', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2586', 'name': 'Polo sin mangas para mujer', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '1029', 'name': 'Cuaderno geométrico A5', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '1498', 'name': 'Filtro de sustitución – pequeño Modelo 400', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2332', 'name': 'Daily flyer NL', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3514', 'name': 'Everyday wellbeing sin yodo', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2596', 'name': 'Organizador de juco', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3422', 'name': 'Lyprinex (60ct)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3506', 'name': 'Maintain & Protect 100 Gold Light', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4169', 'name': 'Sport Pack Sachet Citrus 30 ct', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3491', 'name': "Women's Special", 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3436', 'name': 'Fusions Red', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3521', 'name': 'MR Pack- Vainilla', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4168', 'name': 'Sport Pack Sachet Berry 30 ct', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2483', 'name': 'Cuaderno de tapa dura', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3540', 'name': 'Lifeplus Pets® Care & Comfort', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3532', 'name': 'Triple Protein Shake: Vainilla (sin edulcorante)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3413', 'name': 'Vitamin-C-Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2634', 'name': 'Pantalones cortos de doble capa para hombre', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3449', 'name': 'BE Recharged Citrus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3464', 'name': 'Lifeplus Bodysmart Solutions® Vegan Protein Shake: Vainilla', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2624', 'name': 'Leggings para mujer', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3428', 'name': 'Support Tabs Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2226', 'name': 'Folleto SV Lifeplus SV', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2736', 'name': 'Manta acogedora', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3523', 'name': 'MR Pack - Chocolate con opciones veganas', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3518', 'name': 'Everyday Wellbeing Plus Gold', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2207', 'name': 'Folleto de Lifeplus NL', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3471', 'name': 'Proanthenols® 50 (lg)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3533', 'name': 'Real NRG', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2598', 'name': 'Bañador', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2632', 'name': 'Natural Hand Cream', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2711', 'name': 'Camiseta con cremallera para mujer', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2716', 'name': 'Sudadera con capucha y cremallera para mujer', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3499', 'name': 'Daily Protein Pack - Chocolate', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '1800', 'name': 'Smart Bar', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3482', 'name': 'Digestive Formula', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2208', 'name': 'Folleto de Lifeplus IT', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2712', 'name': 'Camiseta con cremallera para hombre', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2729', 'name': 'Camiseta infantil negra', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3435', 'name': 'Ubiquinol 100 (30ct)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4134', 'name': 'Forever Young Repair & Protect Conditioner', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3425', 'name': 'Vegan OmeGold®', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '467', 'name': 'Filtro de sustitución Modelo 750', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '1499', 'name': 'Filtros de agua de Lifeplus  Placa cerámica SENSEH®', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3433', 'name': 'Yummies', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2209', 'name': 'Folleto de Lifeplus DE', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3438', 'name': 'Brain Formula', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2149', 'name': 'alemán', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4149', 'name': 'Be Recharged Sachet - Berry 30 ct', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '6654', 'name': 'Natural Gold Hand & Body Bar', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2713', 'name': 'Sudadera con capucha y cremallera para hombre', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3522', 'name': 'MR Pack - Vainilla  sin edulcorante', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2484', 'name': 'Bolsa de viaje', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2608', 'name': 'Sudadera Unisex con capucha Lifeplus verde', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3447', 'name': 'Iron Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3437', 'name': 'Micro•Mins Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4129', 'name': 'Forever Young Gentle Cream Cleanser', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4147', 'name': 'Be Sustained Sachet - Berry 30 ct', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3842', 'name': 'Key-Tonic®', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3460', 'name': "Lifeplus Bodysmart Solutions® Men's Gold Formula", 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2732', 'name': 'Member independiente de Lifeplus: carpa desplegable', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3501', 'name': 'Daily Protein Pack - Vainilla sin edulcorante', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2328', 'name': 'Daily flyer DE', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2606', 'name': 'Sudadera Unisex con capucha Lifeplus blanca', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2488', 'name': 'Delantal de cocina', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2597', 'name': 'Pegatinas para las ventanas del coche', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2148', 'name': 'Diario de gratitud - alemán', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2614', 'name': 'Camiseta para hombre verde', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3470', 'name': 'BE Sustained Berry', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3503', 'name': 'Maintain & Protect 50 Gold', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3462', 'name': 'Vitamin E Complex', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3500', 'name': 'Daily Protein Pack - Vainilla', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4680', 'name': 'Be Sustained en sobres - Sabor a frutos del bosque', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3488', 'name': 'Lyprinex (180ct)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3489', 'name': 'mangOmega', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3490', 'name': 'MR Light Pack - Chocolate con opciones veganas', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3452', 'name': 'TVM Plus sin yodo', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2329', 'name': 'Daily flyer FR', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3408', 'name': 'X-Cell', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3508', 'name': 'Maintain, Protect & Satisfy Gold - Chocolate', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3454', 'name': 'D-Mannose Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3517', 'name': 'Everyday Wellbeing Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2496', 'name': 'Gorra verde oliva', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2206', 'name': 'Folleto de Lifeplus ES', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2204', 'name': 'Folleto de Lifeplus EN', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3418', 'name': 'Cogelin', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2306', 'name': 'Vela de la Lifeplus Foundation', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '6074', 'name': 'Lifeplus Shaker Cup', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3415', 'name': 'Phase’oMine', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3410', 'name': 'Joint Formula', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3535', 'name': 'Lifeplus Pets® Move', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '1021', 'name': 'MSM + Vital Care Lotion', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3414', 'name': 'Vitamins D&K', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2482', 'name': 'Bolígrafo de bambú', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '6134', 'name': 'Lifeplus Wonder Gel', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4158', 'name': 'Be Refueled chocolate', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2327', 'name': 'Daily flyer EN', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3456', 'name': "Lifeplus Bodysmart Solutions® Multivitamin Gold Formula - Women's", 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2607', 'name': 'Sudadera Unisex con capucha Lifeplus gris', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3417', 'name': 'Somazyme', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3446', 'name': 'pH Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2305', 'name': 'Funda de fieltro para portátil de la Lifeplus Foundation', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '465', 'name': 'Sistema de Filtro de agua Potable, Modelo de encimera (MP750 SSCT)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3504', 'name': 'Maintain & Protect 100', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3461', 'name': 'BE Sustained Citrus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3510', 'name': 'Maintain, Protect & Satisfy Gold - Vainilla', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3407', 'name': 'Forever Young Skin Formula', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2605', 'name': 'Gorro Lifeplus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2330', 'name': 'Daily flyer ES', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3509', 'name': 'Maintain, Protect & Satisfy - Vainilla', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3493', 'name': 'Winter Boost Pack Ultra', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3457', 'name': 'Lycopin Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2631', 'name': 'Natural Body Wash', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3441', 'name': 'RYR Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2178', 'name': 'Juego de cucharas de madera', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4130', 'name': 'Forever Young Rejuvenating Eye Crème', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2715', 'name': 'Pantalones de jogging para mujer', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3455', 'name': 'Co-Q-10 Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2585', 'name': 'Bolsa de mano grande', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2177', 'name': 'Bolsa de juco', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3545', 'name': 'Lifeplus Pets® Ahiflower® Oil', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3486', 'name': 'Zinc Boost', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2304', 'name': 'Bolsa de fieltro de la Lifeplus Foundation', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3424', 'name': 'Daily BioBasics® Light', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2485', 'name': 'Neceser', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3487', 'name': 'Ubiquinol 100 (60ct)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2723', 'name': 'Botella negra CamelBak de 750 ml', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2714', 'name': 'Pantalones de jogging para hombre', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4150', 'name': 'Be Recharged Sachet - Citrus 30 ct', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2465', 'name': 'Mochila', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2504', 'name': 'Calcetines informales', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '5390', 'name': 'Lifeplus Pets® Peanut Butter Biscuits', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2358', 'name': 'Paquete de postales de la Lifeplus Foundation', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3444', 'name': 'Lifeplus Menaplus®', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2657', 'name': 'Descubra el folleto de productos Omega', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4156', 'name': 'Be Refueled vainilla', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3431', 'name': 'EPA Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3505', 'name': 'Maintain & Protect 100 Gold', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3544', 'name': 'Proanthenols® 200 SV', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2726', 'name': 'Member independiente de Lifeplus: paquete prémium', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3547', 'name': 'Triple Protein Malteada de Chocolate sin azúcar', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2630', 'name': 'Natural Hand & Body Lotion', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3448', 'name': 'Circulation Formula', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2464', 'name': 'Diario de concentración activa -  inglés', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3445', 'name': "Men's Formula", 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3420', 'name': 'Proanthenols® 50 (sm)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3520', 'name': 'MR Pack- Chocolate', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3492', 'name': 'Winter Boost Pack', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4146', 'name': 'Be Focused Sachet - Citrus 30 ct', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '1497', 'name': 'Sistema de Filtro de agua potable, Modelo bajo el fregadero - pequeño (MP400 SB)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2331', 'name': 'Daily flyer IT', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3440', 'name': 'Lifeplus Bodysmart Solutions® Enerxan®', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3512', 'name': 'Maintain, Protect & Satisfy Gold - Vainilla  sin edulcorante', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2599', 'name': 'Camiseta para mujer verde', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '466', 'name': 'Sistema de filtro de agua potable, Modelo bajo el fregadero (MP750 SB)', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '870', 'name': 'Vaso mezclador deluxe', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2441', 'name': 'Tarjetas de presentación de Lifeplus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2604', 'name': 'Gorra Lifeplus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2722', 'name': 'Member independiente de Lifeplus: paquete estándar', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3403', 'name': 'MSM Plus', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3439', 'name': 'Immune Formula', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4164', 'name': 'Lifeplus Pets App', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '4148', 'name': 'Be Sustained Sachet - Citrus 30 ct', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3423', 'name': 'Eye Formula', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '3502', 'name': 'Maintain & Protect 50', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []},
        {'code': '2587', 'name': 'Polo para hombre', 'format': 'Novedad', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []}
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