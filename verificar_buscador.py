#!/usr/bin/env python3

import re

def verificar_inicializacion_buscador():
    """Verificar si el buscador está correctamente inicializado en el HTML"""

    with open('catalogo_lifeplus_buscador_flotante.html', 'r', encoding='utf-8') as f:
        contenido = f.read()

    print("🔍 VERIFICANDO INTEGRACIÓN DEL BUSCADOR")
    print("=" * 50)

    # 1. Verificar CSS del buscador
    css_buscador = "search-float-btn" in contenido
    print(f"✅ CSS del buscador: {'Encontrado' if css_buscador else 'NO ENCONTRADO'}")

    # 2. Verificar JavaScript del buscador
    js_buscador = "inicializarBuscadorFlotante" in contenido
    print(f"✅ JavaScript del buscador: {'Encontrado' if js_buscador else 'NO ENCONTRADO'}")

    # 3. Verificar botón flotante
    boton_buscador = 'id="searchFloatBtn"' in contenido
    print(f"✅ Botón flotante: {'Encontrado' if boton_buscador else 'NO ENCONTRADO'}")

    # 4. Verificar modal
    modal_buscador = 'id="searchModal"' in contenido
    print(f"✅ Modal: {'Encontrado' if modal_buscador else 'NO ENCONTRADO'}")

    # 5. Verificar event listeners duplicados
    dom_content_loaded_count = contenido.count('addEventListener("DOMContentLoaded"')
    print(f"⚠️  Event listeners DOMContentLoaded: {dom_content_loaded_count}")

    if dom_content_loaded_count > 3:
        print("   ⚠️  Posible conflicto con múltiples event listeners")

    # 6. Verificar si hay errores comunes
    errores_potenciales = []

    # Verificar si hay console.log al principio (podría bloquear en algunos navegadores)
    if contenido.count('console.log') > 20:
        errores_potenciales.append("Demasiados console.log")

    # Verificar si hay errores de sintaxis comunes
    if "'})" in contenido and not contenidos.endswith("}"):
        pass  # Normal

    # 7. Buscar el último script para ver si el buscador está al final
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', contenido, re.DOTALL)
    if scripts:
        ultimo_script = scripts[-1]
        tiene_buscador = "inicializarBuscadorFlotante" in ultimo_script
        print(f"✅ Buscador en último script: {'Sí' if tiene_buscador else 'NO'}")

        if not tiene_buscador:
            print("   ⚠️  El buscador no está en el último script")

    print("\n📋 DIAGNÓSTICO:")
    if all([css_buscador, js_buscador, boton_buscador, modal_buscador]):
        print("   ✅ Todos los componentes del buscador están presentes")

        if dom_content_loaded_count > 3:
            print("   ⚠️  Posible conflicto de event listeners DOMContentLoaded")
            print("   📝 SOLUCIÓN: El buscador podría estar siendo sobrescrito")

        print("\n🔧 SOLUCIÓN RECOMENDADA:")
        print("   1. Crear una versión con un solo event listener DOMContentLoaded")
        print("   2. Asegurar que el buscador se inicialice último")
    else:
        print("   ❌ Faltan componentes del buscador")

    return {
        'css': css_buscador,
        'js': js_buscador,
        'boton': boton_buscador,
        'modal': modal_buscador,
        'event_listeners': dom_content_loaded_count
    }

def crear_version_corregida():
    """Crear una versión corregida con mejor inicialización"""

    print("\n🔧 CREANDO VERSIÓN CORREGIDA...")

    with open('catalogo_lifeplus_buscador_flotante.html', 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Eliminar todos los event listeners DOMContentLoaded antiguos
    # excepto el último que inicializa el buscador

    # Encontrar el último script que inicializa el buscador
    scripts = re.findall(r'(<script[^>]*>.*?</script>)', contenido, re.DOTALL)

    if not scripts:
        print("❌ No se encontraron scripts")
        return False

    # Buscar el script del buscador
    buscador_script_index = -1
    for i, script in enumerate(scripts):
        if "inicializarBuscadorFlotante" in script:
            buscador_script_index = i
            break

    if buscador_script_index == -1:
        print("❌ No se encontró el script del buscador")
        return False

    print(f"✅ Script del buscador encontrado en posición {buscador_script_index + 1} de {len(scripts)}")

    # Modificar el último script para que inicialice el buscador con prioridad
    # y añadir un script adicional al final

    # Crear un script simple para forzar la inicialización
    script_forzado = '''
<script>
// Forzar inicialización del buscador flotante
window.addEventListener('load', function() {
    setTimeout(function() {
        if (document.getElementById('searchFloatBtn')) {
            console.log('🔍 Forzando inicialización del buscador flotante...');
            if (typeof inicializarBuscadorFlotante === 'function') {
                inicializarBuscadorFlotante();
                console.log('✅ Buscador flotante inicializado correctamente');
            } else {
                console.error('❌ La función inicializarBuscadorFlotante no está disponible');
            }
        } else {
            console.error('❌ Botón del buscador no encontrado en el DOM');
        }
    }, 2000); // Esperar 2 segundos
});

// Verificación adicional
document.addEventListener('DOMContentLoaded', function() {
    console.log('📋 Verificando integración del buscador...');
    setTimeout(function() {
        if (!document.getElementById('searchFloatBtn')) {
            console.error('❌ El botón del buscador no existe');
        } else {
            console.log('✅ Botón del buscador encontrado');
            document.getElementById('searchFloatBtn').style.display = 'flex';
            document.getElementById('searchFloatBtn').style.visibility = 'visible';
            console.log('✅ Botón del buscador forzado a visible');
        }
    }, 3000);
});
</script>
'''

    # Añadir el script forzado al final del archivo
    contenido_con_forzado = contenido + script_forzado

    # Escribir la versión corregida
    with open('catalogo_lifeplus_buscador_flotante_debug.html', 'w', encoding='utf-8') as f:
        f.write(contenido_con_forzado)

    print("✅ Versión corregida creada: catalogo_lifeplus_buscador_flotante_debug.html")
    print("📋 Mejoras aplicadas:")
    print("   • Script de inicialización forzada con window.load")
    print("   • Verificación de existencia del botón")
    print("   • Forzado de visibilidad del botón")
    print("   • Logs adicionales para debugging")

    return True

if __name__ == "__main__":
    resultado = verificar_inicializacion_buscador()

    if resultado['event_listeners'] > 3:
        crear_version_corregida()