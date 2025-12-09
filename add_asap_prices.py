#!/usr/bin/env python3

import re

# Cargar el archivo actual
with open('completar_categorias.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Función para calcular precio ASAP (aproximadamente 5.5% de descuento)
def calculate_asap_price(normal_price_str):
    # Extraer el valor numérico del precio
    match = re.search(r'€(\d+\.?\d*)', normal_price_str)
    if match:
        normal_price = float(match.group(1))
        # Aplicar descuento del 5.5%
        asap_price = normal_price * 0.945
        # Redondear a 2 decimales
        asap_price_rounded = round(asap_price, 2)
        return f"€{asap_price_rounded:.2f}"
    return None

# Encontrar todas las líneas con productos y añadir precio ASAP
lines = content.split('\n')
updated_lines = []

for line in lines:
    # Buscar líneas que contienen productos (con "code", "name", "price")
    if '"code":' in line and '"name":' in line and '"price":' in line and '"price_asap":' not in line:
        # Extraer el precio normal
        price_match = re.search(r'"price": "([^"]+)"', line)
        if price_match:
            normal_price = price_match.group(1)
            asap_price = calculate_asap_price(normal_price)
            if asap_price:
                # Insertar precio_asap antes del "format"
                line = line.replace('"format":', f'"price_asap": "{asap_price}", "format":')

    updated_lines.append(line)

# Escribir el contenido actualizado
with open('completar_categorias.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(updated_lines))

print("¡Precios ASAP añadidos a todos los productos!")

# Mostrar algunos ejemplos
print("\nEjemplos de productos actualizados:")
with open('completar_categorias.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscar primeros productos con precios ASAP
import re
products_with_asap = re.findall(r'\{[^}]*"price_asap"[^}]*\}', content)
for i, product in enumerate(products_with_asap[:5]):  # Mostrar primeros 5
    print(f"{i+1}. {product}")