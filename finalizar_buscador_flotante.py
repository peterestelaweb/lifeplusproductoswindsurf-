#!/usr/bin/env python3
"""
Aplicar todas las correcciones pendientes al buscador flotante
"""

import re

# Aplicar todas las correcciones pendientes al buscador flotante
def fix_floating_search_final():
    """
    Aplicar todas las correcciones al catálogo con buscador flotante
    """
    try:
        # Leer el catálogo
        with open('catalogo_lifeplus_buscador_flotante.html', 'r', encoding='utf-8') as f:
            content = f.read()

        print("🔧 Aplicando correcciones finales al buscador flotante...")

        # 1. Eliminar el overflow-x: hidden del hero-section
        content = re.sub(
            r'(\.hero-section[^}]*)overflow-x:\s*hidden;',
            r'\1',
            content
        )

        # 2. Mejorar la visibilidad del buscador floating-button
        content = re.sub(
            r'(\.floating-button[^}]*)background:\s*rgba\(46, 125, 50, 0\.9\);',
            r'\1background: rgba(46, 125, 50, 0.95);',
            content
        )

        content = re.sub(
            r'(\.floating-button[^}]*)box-shadow:\s*0[^}]*}',
            r'\1box-shadow: 0 8px 30px rgba(46, 125, 50, 0.4), 0 2px 8px rgba(46, 125, 50, 0.3);\n    z-index: 9999;\n}',
            content
        )

        # 3. Mejorar el modal del buscador
        content = re.sub(
            r'(\.search-modal[^}]*)backdrop-filter:\s*blur\(10px\);',
            r'\1backdrop-filter: blur(15px);',
            content
        )

        content = re.sub(
            r'(\.modal-content[^}]*)background:\s*rgba\(255, 255, 255, 0\.98\);',
            r'\1background: rgba(255, 255, 255, 0.99);\n    border: 1px solid rgba(46, 125, 50, 0.1);\n    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);',
            content
        )

        # 4. Mejorar la visibilidad de los resultados en el modal
        content = re.sub(
            r'(\.search-result[^}]*margin-bottom:[^}]*})',
            r'\1\n    background: rgba(255, 255, 255, 0.9);\n    backdrop-filter: blur(10px);',
            content
        )

        # 5. Asegurar que el botón flotante tiene posición correcta
        floating_button_style = """
        .floating-button {
            position: fixed !important;
            bottom: 30px !important;
            right: 30px !important;
            z-index: 9999 !important;
        }"""

        # Buscar si ya existe el estilo y reemplazarlo
        if '.floating-button' in content:
            content = re.sub(
                r'\.floating-button\s*\{[^}]*\}',
                floating_button_style.strip(),
                content,
                flags=re.DOTALL
            )
        else:
            # Agregar antes de </style>
            content = content.replace('</style>', f'\n{floating_button_style}\n</style>')

        # 6. Consistency improvements para best-price
        content = re.sub(
            r'(\.best-price[^}]*)background:\s*linear-gradient\([^}]*\);',
            r'\1background: linear-gradient(135deg, #1a5c1a 0%, #2e7d32 50%, #1a5c1a 100%);\n    border: 1px solid #2e7d32;',
            content
        )

        # 7. Añadir estilos para mejorar contraste
        additional_styles = """
        /* Mejoras de visibilidad */
        .floating-button:hover {
            transform: translateY(-2px) scale(1.05);
        }

        .search-result strong {
            color: var(--primary-green);
        }

        .product-image-container img {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .product:hover .product-image-container img {
            transform: translateY(-5px);
        }"""

        content = content.replace('</style>', f'\n{additional_styles}\n</style>')

        # 8. Script improvements - consolidar eventos DOMContentLoaded
        # Buscar todos los eventos DOMContentLoaded y consolidarlos
        domContentLoaded_pattern = r'document\.addEventListener\(\'DOMContentLoaded\',\s*function\(\)\s*\{([^}]*)\}\);'

        # Encontrar todos los bloques DOMContentLoaded
        matches = re.findall(domContentLoaded_pattern, content, re.DOTALL)

        if matches:
            # Combinar todo el código en un solo evento
            combined_code = '\n'.join([match.strip() for match in matches])

            # Reemplazar todos los eventos con uno solo
            content = re.sub(
                domContentLoaded_pattern,
                '',
                content,
                flags=re.DOTALL
            )

            # Insertar el evento consolidado al final del body
            consolidated_event = f'''    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            {combined_code}
        }});
    </script>'''

            # Buscar y reemplazar el último script
            content = re.sub(
                r'<script>\s*$',
                consolidated_event,
                content
            )

        # 9. Asegurar que el buscador se inicialice último
        init_search_code = '''
            // Inicializar el buscador flotante
            initSearchModal();'''

        # Buscar si ya existe la inicialización
        if 'initSearchModal' not in content:
            # Agregar al final del evento DOMContentLoaded
            content = re.sub(
                r'(document\.addEventListener\(\'DOMContentLoaded\',\s*function\(\)\s*\{[^}]*)(\}\);)',
                r'\1' + init_search_code + r'\2',
                content,
                flags=re.DOTALL
            )

        # Escribir el archivo corregido
        with open('catalogo_lifeplus_buscador_flotante.html', 'w', encoding='utf-8') as f:
            f.write(content)

        print("✅ Correcciones aplicadas con éxito")
        print("📋 Cambios realizados:")
        print("   • Eliminado overflow-x: hidden del hero-section")
        print("   • Mejorada visibilidad del botón flotante (z-index: 9999)")
        print("   • Mejorado backdrop-filter del modal")
        print("   • Añadido borde y sombra al modal-content")
        print("   • Mejorado contraste de resultados")
        print("   • Consistencia en best-price")
        print("   • Efectos hover mejorados")
        print("   • Consolidados eventos DOMContentLoaded")
        print("   • Asegurada inicialización correcta del buscador")

        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    fix_floating_search_final()