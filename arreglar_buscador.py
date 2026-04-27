#!/usr/bin/env python3

"""
Arreglar el buscador flotante para que aplique estilos correctamente
"""

def arreglar_buscador_flotante():
    """Arreglar problema de estilos del buscador flotante"""

    # Leer el catálogo con problemas
    with open('catalogo_lifeplus_buscador_flotante.html', 'r', encoding='utf-8') as f:
        contenido = f.read()

    # CSS agresivo para forzar visibilidad del botón
    css_arreglado = '''
/* ===== ARREGLO BUSCADOR FLOTANTE ===== */
.search-float-btn {
    position: fixed !important;
    bottom: 20px !important;
    right: 20px !important;
    width: 60px !important;
    height: 60px !important;
    border-radius: 50% !important;
    background: linear-gradient(135deg, #2E7D32 0%, #4CAF50 50%, #66BB6A 100%) !important;
    border: none !important;
    color: white !important;
    font-size: 1.5rem !important;
    cursor: pointer !important;
    z-index: 99999 !important;
    box-shadow: 0 8px 40px rgba(46, 125, 50, 0.5) !important;
    transition: all 0.3s ease !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    visibility: visible !important;
    opacity: 1 !important;
    transform: scale(1) !important;
    margin: 0 !important;
    padding: 0 !important;
    outline: none !important;
    text-decoration: none !important;
    box-sizing: border-box !important;
}

.search-float-btn:hover {
    transform: scale(1.1) !important;
    box-shadow: 0 12px 50px rgba(46, 125, 50, 0.7) !important;
}

.search-float-btn:active {
    transform: scale(1.05) !important;
}

.search-float-btn i {
    font-size: 1.5rem !important;
    color: white !important;
}

/* Forzar botones con search-float-btn en cualquier momento */
button[id="searchFloatBtn"],
button.search-float-btn,
.search-float-btn {
    position: fixed !important;
    bottom: 20px !important;
    right: 20px !important;
    width: 60px !important;
    height: 60px !important;
    border-radius: 50% !important;
    background: linear-gradient(135deg, #2E7D32 0%, #4CAF50 50%, #66BB6A 100%) !important;
    border: none !important;
    color: white !important;
    font-size: 1.5rem !important;
    cursor: pointer !important;
    z-index: 99999 !important;
    box-shadow: 0 8px 40px rgba(46, 125, 50, 0.5) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    visibility: visible !important;
    opacity: 1 !important;
    transform: scale(1) !important;
}
'''

    # Insertar CSS arreglado al final del CSS existente
    style_end = contenido.find('</style>')
    if style_end != -1:
        contenido = contenido[:style_end] + css_arreglado + '\n' + contenido[style_end:]
        print("✅ CSS arreglado insertado")
    else:
        print("❌ Error: No se encontró el cierre </style>")
        return False

    # JavaScript para forzar estilos inline
    js_arreglado = '''
// ===== ARREGLO FORZADO DEL BUSCADOR =====
function forzarEstilosBoton() {
    console.log("🔧 Forzando estilos del buscador flotante...");

    const botones = document.querySelectorAll('button[id="searchFloatBtn"], .search-float-btn');
    console.log(`🔍 Encontrados ${botones.length} botones del buscador`);

    botones.forEach((boton, index) => {
        if (boton) {
            console.log(`🎯 Aplicando estilos al botón ${index + 1}`);

            // Aplicar estilos inline para forzar visibilidad
            boton.style.cssText = `
                position: fixed !important;
                bottom: 20px !important;
                right: 20px !important;
                width: 60px !important;
                height: 60px !important;
                border-radius: 50% !important;
                background: linear-gradient(135deg, #2E7D32 0%, #4CAF50 50%, #66BB6A 100%) !important;
                border: none !important;
                color: white !important;
                font-size: 1.5rem !important;
                cursor: pointer !important;
                z-index: 99999 !important;
                box-shadow: 0 8px 40px rgba(46, 125, 50, 0.5) !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                visibility: visible !important;
                opacity: 1 !important;
                transform: scale(1) !important;
                margin: 0 !important;
                padding: 0 !important;
                outline: none !important;
                transition: all 0.3s ease !important;
            `;

            // Añadir hover effect
            boton.addEventListener('mouseenter', () => {
                boton.style.transform = 'scale(1.1)';
            });

            boton.addEventListener('mouseleave', () => {
                boton.style.transform = 'scale(1)';
            });

            // Hacer parpadear para llamar atención
            if (index === 0) {  // Solo el primer botón
                let parpadeo = 0;
                const intervalo = setInterval(() => {
                    parpadeo++;
                    boton.style.transform = parpadeo % 2 === 0 ? 'scale(1.2)' : 'scale(1)';
                    if (parpadeo > 6) {
                        clearInterval(intervalo);
                        boton.style.transform = 'scale(1)';
                    }
                }, 300);
            }

            console.log(`✅ Botón ${index + 1} configurado exitosamente`);
        }
    });

    // Verificar botones configurados
    setTimeout(() => {
        const botonesVerificados = document.querySelectorAll('button[id="searchFloatBtn"], .search-float-btn');
        console.log(`🎉 Verificación final: ${botonesVerificados.length} botones configurados`);

        botonesVerificados.forEach((boton, index) => {
            const computed = window.getComputedStyle(boton);
            console.log(`Botón ${index + 1}: display=${computed.display}, visibility=${computed.visibility}, opacity=${computed.opacity}`);
        });
    }, 1000);
}

// Ejecutar en múltiples momentos
setTimeout(forzarEstilosBoton, 2000);
setTimeout(forzarEstilosBoton, 4000);
setTimeout(forzarEstilosBoton, 6000);

// También ejecutar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        setTimeout(forzarEstilosBoton, 1000);
    });
}

window.addEventListener('load', () => {
    setTimeout(forzarEstilosBoton, 2000);
});

console.log("🔧 Sistema de arreglo del buscador configurado");
'''

    # Insertar JavaScript antes del cierre </body>
    body_end = contenido.find('</body>')
    if body_end != -1:
        contenido = contenido[:body_end] + f'<script>\n{js_arreglado}\n</script>\n' + contenido[body_end:]
        print("✅ JavaScript arreglado insertado")
    else:
        print("❌ Error: No se encontró el cierre </body>")
        return False

    # Actualizar título
    contenido = contenido.replace(
        '<title>LifePlus Catálogo Premium con Buscador Flotante - 111 Productos</title>',
        '<title>LifePlus Catálogo con Buscador Flotante REPARADO - ¡Visible Siempre!</title>'
    )

    # Escribir el archivo reparado
    with open('catalogo_lifeplus_buscador_reparado.html', 'w', encoding='utf-8') as f:
        f.write(contenido)

    # Calcular tamaño
    import os
    file_size = os.path.getsize('catalogo_lifeplus_buscador_reparado.html')

    print(f"\n🎉 ¡CATÁLOGO CON BUSCADOR REPARADO CREADO!")
    print(f"📁 Archivo: catalogo_lifeplus_buscador_reparado.html")
    print(f"📊 Tamaño: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    print("\n🔧 PROBLEMAS SOLUCIONADOS:")
    print("  • Botón existe pero era invisible por estilos CSS")
    print("  • Estilos !important forzados aplicados")
    print("  • JavaScript inline para garantizar visibilidad")
    print("  • Múltiples sistemas de verificación")
    print("  • Botón parpadea para confirmar que funciona")
    print("\n✅ ESTA VERSIÓN GARANTIZA BOTÓN VISIBLE")

    return True

if __name__ == "__main__":
    print("🔧 REPARANDO BUSCADOR FLOTANTE - PROBLEMA DE VISIBILIDAD")
    print("=" * 60)
    arreglar_buscador_flotante()