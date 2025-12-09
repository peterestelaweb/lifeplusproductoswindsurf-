#!/usr/bin/env python3

"""
Crear versión segura del catálogo con buscador flotante
que garantice que el buscador aparezca siempre
"""

def crear_catalogo_buscador_seguro():
    """Crear una versión segura con múltiples capas de inicialización"""

    # Leer el catálogo base
    with open('catalogo_lifeplus_final.html', 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Leer CSS del buscador
    with open('buscador_flotante.css', 'r', encoding='utf-8') as f:
        css_buscador = f.read()

    # Leer JavaScript del buscador
    with open('buscador_flotante.js', 'r', encoding='utf-8') as f:
        js_buscador = f.read()

    # Leer script de carga manual
    with open('cargar_buscador_manual.js', 'r', encoding='utf-8') as f:
        js_carga_manual = f.read()

    # Insertar CSS antes del cierre </style>
    style_end = contenido.find('</style>')
    if style_end != -1:
        contenido = contenido[:style_end] + '\n\n/* ===== BUSCADOR FLOTANTE INTELIGENTE ===== */\n' + css_buscador + '\n' + contenido[style_end:]
    else:
        print("❌ Error: No se encontró el cierre </style>")
        return False

    # Insertar JavaScript del buscador antes del cierre </script>
    script_end = contenido.rfind('</script>')
    if script_end != -1:
        contenido = contenido[:script_end] + '\n\n// ===== BUSCADOR FLOTANTE INTELIGENTE =====\n' + js_buscador + '\n' + contenido[script_end:]
    else:
        print("❌ Error: No se encontró el cierre </script>")
        return False

    # Añadir el script de carga manual al final del body (justo antes de </body>)
    body_end = contenido.find('</body>')
    if body_end != -1:
        script_manual_tag = f'<script>\n{js_carga_manual}\n</script>\n'
        contenido = contenido[:body_end] + script_manual_tag + contenido[body_end:]
        print("✅ Script de carga manual añadido")
    else:
        print("❌ Error: No se encontró el cierre </body>")
        return False

    # Actualizar título
    contenido = contenido.replace(
        '<title>LifePlus Catálogo Premium - 111 Productos de Bienestar</title>',
        '<title>LifePlus Catálogo Premium con Buscador Flotante SEGURO - 111 Productos</title>'
    )
    print("✅ Título actualizado")

    # Escribir el nuevo archivo con buscador seguro
    with open('catalogo_lifeplus_buscador_seguro.html', 'w', encoding='utf-8') as f:
        f.write(contenido)

    print("\n🎉 ¡Catálogo con buscador flotante SEGURO creado exitosamente!")
    print("📁 Archivo generado: catalogo_lifeplus_buscador_seguro.html")
    print("\n🔍 Mejoras de seguridad:")
    print("  • Script de carga manual con múltiples intentos")
    print("  • Verificación de existencia de productos")
    print("  • Forzado de visibilidad del botón")
    print("  • Fallback con window.load")
    print("  • Logs detallados para debugging")
    print("  • Botón flotante con estilos !important")

    # Calcular tamaño del archivo
    import os
    file_size = os.path.getsize('catalogo_lifeplus_buscador_seguro.html')
    print(f"\n📊 Tamaño del archivo: {file_size:,} bytes ({file_size/1024:.1f} KB)")

    return True

if __name__ == "__main__":
    print("🛡️ CREANDO VERSIÓN SEGURA DEL BUSCADOR FLOTANTE")
    print("=" * 60)

    if crear_catalogo_buscador_seguro():
        print("\n✨ Proceso completado exitosamente!")
        print("📋 Archivo generado: catalogo_lifeplus_buscador_seguro.html")
        print("🎯 Esta versión garantiza que el buscador aparezca siempre")
    else:
        print("\n❌ Error durante la creación del catálogo seguro")