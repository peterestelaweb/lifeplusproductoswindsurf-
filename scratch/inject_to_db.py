import json
import re

with open('nuevos_productos.json', 'r', encoding='utf-8') as f:
    nuevos = json.load(f)

with open('products_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Create Python dictionary string for nuevos
python_list = ",\n        ".join([
    f"{{'code': '{p['code']}', 'name': '{p['name']}', 'format': '{p['format']}', 'price': 0.00, 'description': 'Novedad LifePlus', 'benefits': []}}"
    for p in nuevos
])

new_category = f"\n    'nuevos': [\n        {python_list}\n    ]\n"

# Inject before the last closing brace of the main dictionary
# Find the end of the PRODUCT_DATABASE dictionary
match = re.search(r'PRODUCT_DATABASE = \{.*?\n\s*\]\n\}', content, re.DOTALL)
if match:
    # Add a comma before adding the new key if it's not the first one
    updated_content = content.replace('    ]\n}', '    ],\n' + new_category + '}')
    with open('products_data.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("✅ Inyectados 189 productos en products_data.py")
else:
    print("❌ No se pudo encontrar el punto de inyección en products_data.py")
