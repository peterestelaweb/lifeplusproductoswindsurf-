#!/usr/bin/env python3
"""
Script para agregar IDs únicos y atributos data-categoria a todas las product-cards
en el HTML del catálogo de LifePlus.
"""

import re

# Mapeo de secciones a nombres de categorías
SECTION_TO_CATEGORY = {
    'Nutricionales': 'nutricionales',
    'Proteínas': 'proteinas',
    'Deportiva': 'deportiva',
    'Packs': 'packs',
    'Superfoods': 'superfoods',
    'Forever Young': 'forever-young',
    'Personal': 'personal',
    'Accesorios': 'accesorios',
    'Agua': 'agua'
}

def add_ids_to_products(html_path):
    """Agregar IDs y data-categoria a product-cards"""
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Variable para trackear la categoría actual
    current_category = None
    modified_content = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        # Detectar cambios de categoría por el título
        for section_name, category_slug in SECTION_TO_CATEGORY.items():
            if f'class="category-title"' in line and section_name in line:
                current_category = category_slug
                print(f"Found category: {section_name} -> {category_slug}")
                break
        
        # Buscar product-cards y agregar IDs
        if '<div class="product-card">' in line and current_category:
            # Buscar el código del producto en las próximas líneas
            code = None
            for j in range(i+1, min(i+20, len(lines))):
                code_match = re.search(r'<span class="product-code">(\d+)</span>', lines[j])
                if code_match:
                    code = code_match.group(1)
                    break
            
            if code:
                # Reemplazar la línea con el ID y data-categoria
                new_line = f'                    <div class="product-card" id="producto-{code}" data-categoria="{current_category}">'
                modified_content.append(new_line)
                print(f"Added ID: producto-{code} (categoria: {current_category})")
            else:
                modified_content.append(line)
        else:
            modified_content.append(line)
    
    # Escribir el archivo modificado
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(modified_content))
    
    print(f"\n✅ IDs agregados exitosamente al archivo: {html_path}")

if __name__ == '__main__':
    html_file = '/Users/maykacenteno/Desktop/WEBS EN LOCAL/LIFEPLUS WEB PRODUCTOS/catalogo_lifeplus_buscador_funcional.html'
    add_ids_to_products(html_file)
