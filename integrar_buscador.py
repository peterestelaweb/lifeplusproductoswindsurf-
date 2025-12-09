#!/usr/bin/env python3

"""
Script para integrar el buscador flotante inteligente en el catálogo LifePlus
"""

def integrar_buscador_en_catalogo():
    """Integrar CSS y JavaScript del buscador en el catálogo existente"""

    # Leer el catálogo base
    with open('catalogo_lifeplus_final.html', 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Leer CSS del buscador
    with open('buscador_flotante.css', 'r', encoding='utf-8') as f:
        css_buscador = f.read()

    # Leer JavaScript del buscador
    with open('buscador_flotante.js', 'r', encoding='utf-8') as f:
        js_buscador = f.read()

    # Insertar CSS antes del cierre </style>
    style_end = contenido.find('</style>')
    if style_end != -1:
        contenido = contenido[:style_end] + '\n\n/* ===== BUSCADOR FLOTANTE INTELIGENTE ===== */\n' + css_buscador + '\n' + contenido[style_end:]
        print("✅ CSS del buscador integrado")
    else:
        print("❌ Error: No se encontró el cierre </style>")
        return False

    # Insertar JavaScript antes del cierre </script>
    script_end = contenido.rfind('</script>')
    if script_end != -1:
        contenido = contenido[:script_end] + '\n\n// ===== BUSCADOR FLOTANTE INTELIGENTE =====\n' + js_buscador + '\n' + contenido[script_end:]
        print("✅ JavaScript del buscador integrado")
    else:
        print("❌ Error: No se encontró el cierre </script>")
        return False

    # Actualizar título
    contenido = contenido.replace(
        '<title>LifePlus Catálogo Premium - 111 Productos de Bienestar</title>',
        '<title>LifePlus Catálogo Premium con Buscador Flotante - 111 Productos</title>'
    )
    print("✅ Título actualizado")

    # Escribir el nuevo archivo con buscador
    with open('catalogo_lifeplus_buscador_flotante.html', 'w', encoding='utf-8') as f:
        f.write(contenido)

    print("\n🎉 ¡Catálogo con buscador flotante creado exitosamente!")
    print("📁 Archivo generado: catalogo_lifeplus_buscador_flotante.html")
    print("\n🔍 Características del buscador:")
    print("  • Botón flotante en esquina inferior derecha")
    print("  • Búsqueda fuzzy con tolerancia a errores ortográficos")
    print("  • Filtro por categorías")
    print("  • Modal responsive para móvil, tablet y desktop")
    print("  • Búsqueda en tiempo real con debounce")
    print("  • Navegación con teclas ESC y click")
    print("  • Diseño integrado con estilos existentes")
    print("  • Sin dependencias externas")
    print("\n📱 Responsive:")
    print("  • Desktop: Modal 700px, botón 60px")
    print("  • Tablet: Modal 85% ancho, botón 55px")
    print("  • Mobile: Modal 95% ancho, botón 50px")

    # Calcular tamaño del archivo
    import os
    file_size = os.path.getsize('catalogo_lifeplus_buscador_flotante.html')
    print(f"\n📊 Tamaño del archivo: {file_size:,} bytes ({file_size/1024:.1f} KB)")

    return True

def verificar_archivos():
    """Verificar que los archivos necesarios existan"""
    import os

    archivos_requeridos = [
        'catalogo_lifeplus_final.html',
        'buscador_flotante.css',
        'buscador_flotante.js'
    ]

    print("🔍 Verificando archivos requeridos...")
    for archivo in archivos_requeridos:
        if os.path.exists(archivo):
            size = os.path.getsize(archivo)
            print(f"  ✅ {archivo} ({size:,} bytes)")
        else:
            print(f"  ❌ {archivo} - ARCHIVO NO ENCONTRADO")
            return False

    return True

if __name__ == "__main__":
    print("🚀 INTEGRANDO BUSCADOR FLOTANTE INTELIGENTE EN CATÁLOGO LIFEPLUS")
    print("=" * 60)

    if verificar_archivos():
        print()
        if integrar_buscador_en_catalogo():
            print("\n✨ Proceso completado exitosamente!")
        else:
            print("\n❌ Error durante la integración del buscador")
    else:
        print("\n❌ Faltan archivos requeridos. No se puede continuar.")