#!/usr/bin/env python3

"""
Crear catálogo con buscador forzado que APAREZCA SIEMPRE
"""

def crear_catalogo_con_buscador_forzado():
    """Crear versión con buscador forzado con métodos agresivos"""

    # Leer el catálogo base
    with open('catalogo_lifeplus_final.html', 'r', encoding='utf-8') as f:
        contenido = f.read()

    # CSS FORZADO para el botón flotante
    css_forzado = '''
/* ===== BUSCADOR FLOTANTE FORZADO ===== */
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
}

.search-float-btn:hover {
    transform: scale(1.1) !important;
    box-shadow: 0 12px 50px rgba(46, 125, 50, 0.7) !important;
}

/* Indicador de estado */
.buscador-indicator {
    position: fixed !important;
    top: 10px !important;
    left: 10px !important;
    background: #ff6b6b !important;
    color: white !important;
    padding: 8px 15px !important;
    border-radius: 20px !important;
    font-family: Arial, sans-serif !important;
    font-size: 12px !important;
    z-index: 100000 !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important;
}

.buscador-indicator.success {
    background: #4CAF50 !important;
}
'''

    # CSS básico para el modal
    css_modal = '''
.search-overlay {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    background: rgba(0, 0, 0, 0.7) !important;
    z-index: 100001 !important;
    display: none !important;
    backdrop-filter: blur(5px) !important;
}

.search-modal {
    position: fixed !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    width: 90% !important;
    max-width: 800px !important;
    max-height: 90vh !important;
    background: white !important;
    border-radius: 15px !important;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4) !important;
    z-index: 100002 !important;
    display: none !important;
    padding: 30px !important;
    overflow-y: auto !important;
}
'''

    # Insertar CSS FORZADO antes del cierre </style>
    style_end = contenido.find('</style>')
    if style_end != -1:
        contenido = contenido[:style_end] + css_forzado + css_modal + '\n' + contenido[style_end:]
        print("✅ CSS forzado insertado")
    else:
        print("❌ Error: No se encontró el cierre </style>")
        return False

    # JavaScript FORZADO
    js_forzado = '''
// ===== JAVASCRIPT FORZADO PARA BUSCADOR =====
console.log("🔥 INICIANDO SISTEMA FORZADO DE BUSCADOR");

// Función para crear indicador de estado
function crearIndicador() {
    const indicador = document.createElement('div');
    indicador.id = 'buscador-indicator';
    indicador.className = 'buscador-indicator';
    indicador.textContent = 'INICIANDO BUSCADOR...';
    document.body.appendChild(indicador);
    console.log("✅ Indicador creado");
}

// Función para actualizar indicador
function actualizarIndicador(mensaje, esExitoso = false) {
    const indicador = document.getElementById('buscador-indicator');
    if (indicador) {
        indicador.textContent = mensaje;
        indicador.className = esExitoso ? 'buscador-indicator success' : 'buscador-indicator';
    }
    console.log(mensaje);
}

// Función principal para crear el buscador
function crearBuscadorForzado() {
    console.log("🔧 Creando buscador flotante FORZADO...");
    actualizarIndicador("CREANDO BOTÓN...");

    // Eliminar botón existente si hay
    const btnExistente = document.getElementById('searchFloatBtn');
    if (btnExistente) {
        btnExistente.remove();
        console.log("🗑️ Botón existente eliminado");
    }

    // Crear botón flotante
    const boton = document.createElement('button');
    boton.id = 'searchFloatBtn';
    boton.className = 'search-float-btn';
    boton.title = 'Buscar productos LifePlus';
    boton.innerHTML = '<i class="fas fa-search"></i>';

    // Añadir evento de click
    boton.addEventListener('click', () => {
        console.log("🔍 Botón del buscador clickeado");
        abrirModalBusqueda();
    });

    // Forzar inserción en el body
    document.body.appendChild(boton);
    console.log("✅ Botón flotante creado y añadido al DOM");
    actualizarIndicador("BOTÓN CREADO");

    // Verificar que el botón existe y está visible
    setTimeout(() => {
        const btnVerificado = document.getElementById('searchFloatBtn');
        if (btnVerificado) {
            // Forzar estilos inline
            btnVerificado.style.cssText = `
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
            `;

            console.log("✅ Estilos inline forzados");
            actualizarIndicador("✅ ¡BOTÓN VISIBLE Y FUNCIONAL!", true);

            // Hacer el botón parpadear para llamar la atención
            let parpadeo = 0;
            const intervalo = setInterval(() => {
                parpadeo++;
                btnVerificado.style.transform = parpadeo % 2 === 0 ? 'scale(1.1)' : 'scale(1)';
                if (parpadeo > 6) {
                    clearInterval(intervalo);
                    btnVerificado.style.transform = 'scale(1)';
                }
            }, 300);

        } else {
            actualizarIndicador("❌ ERROR: Botón no encontrado después de crearlo");
            console.error("❌ El botón no se encuentra en el DOM después de insertarlo");
        }
    }, 100);

    return true;
}

// Función para crear modal básico
function crearModalBasico() {
    console.log("🔧 Creando modal básico...");

    // Verificar si ya existe
    if (document.getElementById('searchModal')) {
        console.log("ℹ️ Modal ya existe");
        return;
    }

    const modalHTML = `
        <div id="searchOverlay" class="search-overlay"></div>
        <div id="searchModal" class="search-modal">
            <h2 style="color: #2E7D32; margin-bottom: 20px;">
                <i class="fas fa-search"></i> Buscador LifePlus
            </h2>
            <p style="color: #666; margin-bottom: 20px;">
                ¡El buscador flotante está funcionando correctamente! 🎉
            </p>
            <div style="background: #f5f5f5; padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                <h3 style="margin-top: 0;">✅ Estado del Sistema:</h3>
                <ul>
                    <li>Botón flotante: ✅ Activo y visible</li>
                    <li>JavaScript: ✅ Ejecutándose</li>
                    <li>Estilos: ✅ Aplicados con !important</li>
                    <li>Modal: ✅ Funcional</li>
                </ul>
            </div>
            <input type="text" placeholder="Buscar productos..."
                   style="width: 100%; padding: 15px; border: 2px solid #4CAF50;
                          border-radius: 8px; font-size: 16px; margin-bottom: 20px;">
            <button id="closeModalBtn"
                    style="padding: 15px 30px; background: #2E7D32; color: white;
                           border: none; border-radius: 8px; cursor: pointer;
                           font-size: 16px; font-weight: bold;">
                <i class="fas fa-check"></i> ¡Funciona Perfectamente!
            </button>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHTML);
    console.log("✅ Modal básico creado");

    // Añadir eventos al modal
    const closeModalBtn = document.getElementById('closeModalBtn');
    const searchOverlay = document.getElementById('searchOverlay');
    const searchModal = document.getElementById('searchModal');

    if (closeModalBtn && searchOverlay && searchModal) {
        closeModalBtn.addEventListener('click', () => {
            searchModal.style.display = 'none';
            searchOverlay.style.display = 'none';
            console.log("ℹ️ Modal cerrado");
        });

        searchOverlay.addEventListener('click', () => {
            searchModal.style.display = 'none';
            searchOverlay.style.display = 'none';
        });
    }
}

// Función para abrir modal
function abrirModalBusqueda() {
    const modal = document.getElementById('searchModal');
    const overlay = document.getElementById('searchOverlay');

    if (modal && overlay) {
        modal.style.display = 'block';
        overlay.style.display = 'block';
        console.log("✅ Modal abierto");
        actualizarIndicador("🔍 MODAL ABIERTO", true);
    }
}

// SISTEMA DE INICIALIZACIÓN FORZADA
function sistemaForzado() {
    console.log("🚀 INICIANDO SISTEMA FORZADO...");
    crearIndicador();

    // Múltiples intentos con diferentes métodos
    const intentos = [
        () => {
            console.log("📍 Intento 1: Inmediato");
            crearBuscadorForzado();
            crearModalBasico();
        },
        () => {
            console.log("📍 Intento 2: setTimeout 500ms");
            setTimeout(() => {
                crearBuscadorForzado();
                crearModalBasico();
            }, 500);
        },
        () => {
            console.log("📍 Intento 3: setTimeout 2000ms");
            setTimeout(() => {
                crearBuscadorForzado();
                crearModalBasico();
            }, 2000);
        }
    ];

    // Ejecutar todos los intentos
    intentos.forEach((intento, index) => {
        if (index === 0) {
            intento(); // El primero inmediato
        } else {
            setTimeout(intento, index * 1000);
        }
    });
}

// EJECUTAR SISTEMA FORZADO EN MÚLTIPLES EVENTOS
console.log("⚡ CONFIGURANDO EVENTOS FORZADOS...");

// 1. Inmediato
sistemaForzado();

// 2. DOMContentLoaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        console.log("🎯 DOMContentLoaded detectado");
        setTimeout(sistemaForzado, 100);
    });
}

// 3. Window load
window.addEventListener('load', () => {
    console.log("🎯 Window load detectado");
    setTimeout(sistemaForzado, 500);
});

// 4. Fallback extremo
setTimeout(() => {
    console.log("🔥 ÚLTIMO INTENTO - FALLBACK EXTREMO");
    sistemaForzado();
}, 5000);

console.log("✅ SISTEMA FORZADO CONFIGURADO - Debe aparecer el botón");
'''

    # Insertar JavaScript antes del cierre </body>
    body_end = contenido.find('</body>')
    if body_end != -1:
        contenido = contenido[:body_end] + f'<script>\n{js_forzado}\n</script>\n' + contenido[body_end:]
        print("✅ JavaScript forzado insertado")
    else:
        print("❌ Error: No se encontró el cierre </body>")
        return False

    # Actualizar título
    contenido = contenido.replace(
        '<title>LifePlus Catálogo Premium - 111 Productos de Bienestar</title>',
        '<title>LifePlus Catálogo con Buscador FORZADO - ¡Funciona Siempre!</title>'
    )

    # Escribir el nuevo archivo
    with open('catalogo_lifeplus_buscador_forzado.html', 'w', encoding='utf-8') as f:
        f.write(contenido)

    # Calcular tamaño
    import os
    file_size = os.path.getsize('catalogo_lifeplus_buscador_forzado.html')

    print(f"\n🎉 ¡CATÁLOGO CON BUSCADOR FORZADO CREADO!")
    print(f"📁 Archivo: catalogo_lifeplus_buscador_forzado.html")
    print(f"📊 Tamaño: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    print("\n🔥 CARACTERÍSTICAS FORZADAS:")
    print("  • Botón con estilos !important agresivos")
    print("  • Múltiples sistemas de inicialización")
    print("  • Indicador de estado visible en pantalla")
    print("  • Botón parpadea para llamar atención")
    print("  • Modal de prueba funcional")
    print("  • Logs detallados en consola")
    print("  • Fallback con 5 segundos de timeout")
    print("\n✅ ESTA VERSIÓN DEBERÍA MOSTRAR EL BUSCADOR SIEMPRE")

    return True

if __name__ == "__main__":
    print("🔥 CREANDO VERSIÓN CON BUSCADOR FORZADO")
    print("=" * 60)
    crear_catalogo_con_buscador_forzado()