import json
import re

with open('nuevos_productos.json', 'r', encoding='utf-8') as f:
    nuevos = json.load(f)

# 1. Update products_data.py
with open('products_data.py', 'r', encoding='utf-8') as f:
    pd_content = f.read()

if '"nuevos":' not in pd_content:
    # Inject before the final closing brace of PRODUCT_DATABASE
    nuevos_str = ',\n    "nuevos": ' + json.dumps(nuevos, ensure_ascii=False, indent=8)
    pd_content = re.sub(r'\n}\s*$', nuevos_str + '\n}', pd_content)
    with open('products_data.py', 'w', encoding='utf-8') as f:
        f.write(pd_content)
    print("products_data.py actualizado con la categoría 'nuevos'.")

# 2. Update crear_buscador_funcional.py
with open('crear_buscador_funcional.py', 'r', encoding='utf-8') as f:
    cb_content = f.read()

# Add to the HTML dropdown
if '<option value="nuevos">' not in cb_content:
    dropdown_addition = '                    <option value="pets">🐾 Pets</option>\n                    <option value="nuevos">✨ Novedades (Auto)</option>'
    cb_content = cb_content.replace('<option value="pets">🐾 Pets</option>', dropdown_addition)

# Add to Javascript object
if 'nuevos: [' not in cb_content:
    # First convert Python list to JS string format
    js_list = []
    for p in nuevos:
        js_list.append(f'        {{"code": "{p["code"]}", "name": "{p["name"]}", "price": "{p["price"]}", "price_asap": "{p["price_asap"]}", "format": "{p["format"]}"}}')
    
    js_nuevos_str = ',\n    nuevos: [\n' + ',\n'.join(js_list) + '\n    ]'
    
    # Inject after pets list in JS
    cb_content = re.sub(r'(\s*\{"code": "4164"[^\}]+\}\n\s*\])', r'\1' + js_nuevos_str, cb_content)
    
# Add category icons
if "'nuevos': '✨'" not in cb_content:
    cb_content = cb_content.replace("'pets': '🐾'", "'pets': '🐾',\n        'nuevos': '✨'")
    cb_content = cb_content.replace("'pets': 'Pets'", "'pets': 'Pets',\n        'nuevos': 'Novedades Automáticas'")
    
with open('crear_buscador_funcional.py', 'w', encoding='utf-8') as f:
    f.write(cb_content)
    
print("crear_buscador_funcional.py actualizado con la categoría 'nuevos'.")
