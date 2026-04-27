import re

with open('crear_buscador_funcional.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update <option> list
option_target = '''                    <option value="agua">💧 Agua</option>
                </select>'''
option_replace = '''                    <option value="agua">💧 Agua</option>
                    <option value="pets">🐾 Pets</option>
                </select>'''
if option_target in code:
    code = code.replace(option_target, option_replace)

# 2. Add Pets to productosLifePlus dictionary
dict_target = '''    packs: [
        {"code": "3502", "name": "Maintain & Protect 50", "price": "€123.00", "price_asap": "€116.23", "format": "Pack recomendado"},
        {"code": "3503", "name": "Maintain & Protect 50 Gold", "price": "€168.50", "price_asap": "€159.23", "format": "Pack premium"},
        {"code": "3504", "name": "Maintain & Protect 100", "price": "€153.75", "price_asap": "€145.29", "format": "Pack recomendado"},
        {"code": "3505", "name": "Maintain & Protect 100 Gold", "price": "€199.00", "price_asap": "€188.05", "format": "Pack premium"},
        {"code": "3506", "name": "Maintain & Protect 100 Gold Light", "price": "€187.50", "price_asap": "€177.19", "format": "Pack premium ligero"},
        {"code": "3507", "name": "Maintain & Protect VEGAN", "price": "€165.00", "price_asap": "€155.92", "format": "Pack vegano"}
    ]'''
dict_replace = dict_target + ''',

    pets: [
        {"code": "6687", "name": "Lifeplus Pets™ Calm", "price": "€0.00", "price_asap": "€0.00", "format": "90 Masticables"},
        {"code": "6688", "name": "Lifeplus Pets™ Move", "price": "€0.00", "price_asap": "€0.00", "format": "Masticables Blandos"},
        {"code": "6689", "name": "Lifeplus Pets™ Digest", "price": "€0.00", "price_asap": "€0.00", "format": "Masticables Blandos"},
        {"code": "6692", "name": "Lifeplus Pets™ Peanut Butter Biscuits", "price": "€0.00", "price_asap": "€0.00", "format": "Galletas"},
        {"code": "6697", "name": "Lifeplus Pets™ Care & Comfort", "price": "€0.00", "price_asap": "€0.00", "format": "Aerosol"},
        {"code": "6698", "name": "Lifeplus Pets™ Ahiflower® Oil", "price": "€0.00", "price_asap": "€0.00", "format": "Aerosol"},
        {"code": "PETS-APP", "name": "Lifeplus Pets™ Mobile App", "price": "€0.00", "price_asap": "€0.00", "format": "Aplicación Móvil"}
    ]'''
if dict_target in code:
    code = code.replace(dict_target, dict_replace)

# 3. Update getCategoryIcon
icon_target = '''        'accesorios': '🎒',
        'agua': '💧'
    };'''
icon_replace = '''        'accesorios': '🎒',
        'agua': '💧',
        'pets': '🐾'
    };'''
if icon_target in code:
    code = code.replace(icon_target, icon_replace)

# 4. Update formatCategoryName
name_target = '''        'accesorios': 'Accesorios',
        'agua': 'Agua'
    };'''
name_replace = '''        'accesorios': 'Accesorios',
        'agua': 'Agua',
        'pets': 'Pets'
    };'''
if name_target in code:
    code = code.replace(name_target, name_replace)

with open('crear_buscador_funcional.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("crear_buscador_funcional.py patched!")
