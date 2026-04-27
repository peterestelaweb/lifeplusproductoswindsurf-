#!/usr/bin/env python3

"""
Crear buscador flotante ajustado que no se solape y sea más obvio
"""

def crear_buscador_ajustado():
    """Crear buscador con mejor posición y diseño claro"""

    # Leer el catálogo base
    with open('catalogo_lifeplus_final.html', 'r', encoding='utf-8') as f:
        contenido = f.read()

    # CSS ajustado para evitar solapamiento y mejor diseño
    css_ajustado = '''
/* ===== BUSCADOR FLOTANTE AJUSTADO ===== */
.search-float-btn {
    position: fixed !important;
    bottom: 90px !important;  /* Mover hacia arriba para evitar solapamiento con WhatsApp */
    right: 20px !important;
    width: 70px !important;     /* Un poco más grande */
    height: 70px !important;
    border-radius: 50% !important;
    background: linear-gradient(135deg, #FF6B35 0%, #F7931E 50%, #FDC830 100%) !important; /* Naranja para diferenciar de verde WhatsApp */
    border: none !important;
    color: white !important;
    font-size: 1.8rem !important;   /* Icono más grande */
    cursor: pointer !important;
    z-index: 10000 !important;      /* Z-index alto pero debajo de WhatsApp */
    box-shadow: 0 8px 40px rgba(255, 107, 53, 0.4) !important; /* Sombra naranja */
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
    box-shadow: 0 12px 50px rgba(255, 107, 53, 0.6) !important;
}

.search-float-btn:active {
    transform: scale(1.05) !important;
}

.search-float-btn::after {
    content: 'BUSCAR';
    position: absolute;
    bottom: -35px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    background: rgba(0, 0, 0, 0.8) !important;
    color: white !important;
    padding: 5px 10px !important;
    border-radius: 15px !important;
    font-size: 11px !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 600 !important;
    white-space: nowrap !important;
    opacity: 0 !important;
    transition: opacity 0.3s ease !important;
    z-index: 10001 !important;
    pointer-events: none !important;
}

.search-float-btn:hover::after {
    opacity: 1 !important;
}

.search-float-btn i {
    font-size: 1.8rem !important;
    color: white !important;
}

/* Modal de búsqueda mejorado */
.search-overlay {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    background: rgba(0, 0, 0, 0.7) !important;
    z-index: 20000 !important;
    display: none !important;
    backdrop-filter: blur(5px) !important;
}

.search-modal {
    position: fixed !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    width: 90% !important;
    max-width: 700px !important;
    max-height: 90vh !important;
    background: white !important;
    border-radius: 20px !important;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3) !important;
    z-index: 20001 !important;
    display: none !important;
    padding: 30px !important;
    overflow-y: auto !important;
}

.search-modal-header {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    margin-bottom: 20px !important;
    padding-bottom: 15px !important;
    border-bottom: 2px solid #f0f0f0 !important;
}

.search-modal-header h2 {
    color: #FF6B35 !important;
    font-size: 1.8rem !important;
    margin: 0 !important;
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
}

.search-input-container {
    position: relative !important;
    margin-bottom: 20px !important;
}

.search-input {
    width: 100% !important;
    padding: 15px 50px 15px 50px !important;
    border: 2px solid #FF6B35 !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    font-family: 'Montserrat', sans-serif !important;
    transition: all 0.3s ease !important;
    box-sizing: border-box !important;
}

.search-input:focus {
    outline: none !important;
    border-color: #F7931E !important;
    box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.1) !important;
}

.search-input-icon {
    position: absolute !important;
    left: 15px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    color: #FF6B35 !important;
    font-size: 1.2rem !important;
    z-index: 2 !important;
}

.category-filter {
    width: 100% !important;
    padding: 15px 20px !important;
    border: 2px solid #FF6B35 !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    font-family: 'Montserrat', sans-serif !important;
    background: white !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    margin-bottom: 20px !important;
    box-sizing: border-box !important;
}

.category-filter:focus {
    outline: none !important;
    border-color: #F7931E !important;
    box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.1) !important;
}

.search-results {
    max-height: 400px !important;
    overflow-y: auto !important;
    border: 1px solid #f0f0f0 !important;
    border-radius: 12px !important;
    padding: 15px !important;
    background: #fafafa !important;
}

.search-result-product {
    background: white !important;
    border-radius: 10px !important;
    padding: 15px !important;
    margin-bottom: 10px !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    border: 2px solid transparent !important;
}

.search-result-product:hover {
    border-color: #FF6B35 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 20px rgba(255, 107, 53, 0.2) !important;
}

.search-modal-footer {
    display: flex !important;
    justify-content: space-between !important;
    gap: 15px !important;
    margin-top: 20px !important;
    padding-top: 20px !important;
    border-top: 2px solid #f0f0f0 !important;
}

.btn-primary {
    background: #FF6B35 !important;
    color: white !important;
}

.btn-primary:hover {
    background: #F7931E !important;
}

.btn-secondary {
    background: #6c757d !important;
    color: white !important;
}

.btn-secondary:hover {
    background: #5a6268 !important;
}

.btn {
    padding: 12px 25px !important;
    border-radius: 8px !important;
    border: none !important;
    cursor: pointer !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

/* Responsive */
@media (max-width: 768px) {
    .search-float-btn {
        bottom: 80px !important;  /* Ajustar para móviles */
        right: 15px !important;
        width: 60px !important;
        height: 60px !important;
    }

    .search-float-btn::after {
        font-size: 10px !important;
        bottom: -30px !important;
    }

    .search-modal {
        width: 95% !important;
        padding: 20px !important;
    }
}
'''

    # Insertar CSS antes del cierre </style>
    style_end = contenido.find('</style>')
    if style_end != -1:
        contenido = contenido[:style_end] + css_ajustado + '\n' + contenido[style_end:]
        print("✅ CSS ajustado insertado")
    else:
        print("❌ Error: No se encontró el cierre </style>")
        return False

    # JavaScript mejorado
    js_ajustado = '''
// ===== BUSCADOR FLOTANTE AJUSTADO =====
function crearBuscadorAjustado() {
    console.log("🔍 Creando buscador flotante ajustado...");

    // Eliminar botones existentes
    const botonesExistentes = document.querySelectorAll('button[id="searchFloatBtn"], .search-float-btn');
    botonesExistentes.forEach(btn => btn.remove());

    // Crear botón flotante ajustado
    const boton = document.createElement('button');
    boton.id = 'searchFloatBtn';
    boton.className = 'search-float-btn';
    boton.title = 'Buscar productos LifePlus - Click para abrir buscador';
    boton.innerHTML = '<i class="fas fa-search"></i>';

    // Crear modal mejorado
    const modalHTML = `
        <div id="searchOverlay" class="search-overlay"></div>
        <div id="searchModal" class="search-modal">
            <div class="search-modal-header">
                <h2><i class="fas fa-search"></i> Buscar Productos</h2>
                <button id="closeModalBtn" style="background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #666;">✕</button>
            </div>

            <div class="search-input-container">
                <i class="fas fa-search search-input-icon"></i>
                <input type="text" id="searchInput" class="search-input" placeholder="¿Qué producto buscas? Escribe nombre, código o categoría...">
            </div>

            <select id="categoryFilter" class="category-filter">
                <option value="todas">🏠 Todas las categorías</option>
                <option value="nutricionales">💊 Nutricionales</option>
                <option value="proteinas">💪 Proteínas</option>
                <option value="deportiva">🏃 Deporte</option>
                <option value="packs">📦 Packs</option>
                <option value="superfoods">🌿 Superfoods</option>
                <option value="forever-young">⏳ Forever Young</option>
                <option value="personal">👤 Personal</option>
                <option value="accesorios">🎒 Accesorios</option>
                <option value="agua">💧 Agua</option>
            </select>

            <div class="search-results-info">
                <span id="resultsCount" style="color: #666; font-size: 14px;">Escribe para buscar productos...</span>
            </div>

            <div id="searchResults" class="search-results"></div>

            <div class="search-modal-footer">
                <button id="clearBtn" class="btn btn-secondary">🗑️ Limpiar</button>
                <button id="closeFooterBtn" class="btn btn-primary">✅ Cerrar</button>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', boton);
    document.body.insertAdjacentHTML('beforeend', modalHTML);
    console.log("✅ Botón y modal ajustados creados");

    // Configurar eventos
    configurarEventosBuscador();

    // Forzar estilos y hacer visible
    setTimeout(() => {
        const btnVerificado = document.getElementById('searchFloatBtn');
        if (btnVerificado) {
            btnVerificado.style.cssText = `
                position: fixed !important;
                bottom: 90px !important;
                right: 20px !important;
                width: 70px !important;
                height: 70px !important;
                border-radius: 50% !important;
                background: linear-gradient(135deg, #FF6B35 0%, #F7931E 50%, #FDC830 100%) !important;
                border: none !important;
                color: white !important;
                font-size: 1.8rem !important;
                cursor: pointer !important;
                z-index: 10000 !important;
                box-shadow: 0 8px 40px rgba(255, 107, 53, 0.4) !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                visibility: visible !important;
                opacity: 1 !important;
                transform: scale(1) !important;
            `;

            // Hacerlo parpadear una vez para llamar atención
            setTimeout(() => {
                let parpadeo = 0;
                const intervalo = setInterval(() => {
                    parpadeo++;
                    btnVerificado.style.transform = parpadeo % 2 === 0 ? 'scale(1.2)' : 'scale(1)';
                    if (parpadeo > 6) {
                        clearInterval(intervalo);
                        btnVerificado.style.transform = 'scale(1)';
                        console.log("✅ ¡Buscador flotante ajustado y visible!");
                    }
                }, 300);
            }, 2000);
        }
    }, 100);

    return true;
}

function configurarEventosBuscador() {
    const boton = document.getElementById('searchFloatBtn');
    const modal = document.getElementById('searchModal');
    const overlay = document.getElementById('searchOverlay');
    const closeBtn = document.getElementById('closeModalBtn');
    const closeFooterBtn = document.getElementById('closeFooterBtn');
    const clearBtn = document.getElementById('clearBtn');
    const searchInput = document.getElementById('searchInput');

    if (boton && modal && overlay && closeBtn) {
        // Abrir modal
        boton.addEventListener('click', () => {
            modal.style.display = 'block';
            overlay.style.display = 'block';
            if (searchInput) searchInput.focus();
        });

        // Cerrar modal
        closeBtn.addEventListener('click', cerrarModal);
        closeFooterBtn.addEventListener('click', cerrarModal);
        overlay.addEventListener('click', cerrarModal);

        // Limpiar búsqueda
        if (clearBtn) {
            clearBtn.addEventListener('click', () => {
                if (searchInput) searchInput.value = '';
                document.getElementById('resultsCount').textContent = 'Escribe para buscar productos...';
                document.getElementById('searchResults').innerHTML = '<p style="text-align: center; color: #999; padding: 20px;">💡 Escribe el nombre de un producto para buscar</p>';
            });
        }

        // Cerrar con ESC
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') cerrarModal();
        });
    }
}

function cerrarModal() {
    const modal = document.getElementById('searchModal');
    const overlay = document.getElementById('searchOverlay');
    if (modal) modal.style.display = 'none';
    if (overlay) overlay.style.display = 'none';
}

// Inicialización en múltiples momentos
setTimeout(crearBuscadorAjustado, 1000);
setTimeout(crearBuscadorAjustado, 3000);

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        setTimeout(crearBuscadorAjustado, 2000);
    });
}

window.addEventListener('load', () => {
    setTimeout(crearBuscadorAjustado, 4000);
});

console.log("🔧 Buscador flotante ajustado configurado");
'''

    # Insertar JavaScript antes del cierre </body>
    body_end = contenido.find('</body>')
    if body_end != -1:
        contenido = contenido[:body_end] + f'<script>\n{js_ajustado}\n</script>\n' + contenido[body_end:]
        print("✅ JavaScript ajustado insertado")
    else:
        print("❌ Error: No se encontró el cierre </body>")
        return False

    # Actualizar título
    contenido = contenido.replace(
        '<title>LifePlus Catálogo Premium - 111 Productos de Bienestar</title>',
        '<title>LifePlus Catálogo con Buscador Flotante Ajustado - ¡Visible y Claro!</title>'
    )

    # Escribir el archivo ajustado
    with open('catalogo_lifeplus_buscador_ajustado.html', 'w', encoding='utf-8') as f:
        f.write(contenido)

    # Calcular tamaño
    import os
    file_size = os.path.getsize('catalogo_lifeplus_buscador_ajustado.html')

    print(f"\n🎯 ¡CATÁLOGO CON BUSCADOR AJUSTADO CREADO!")
    print(f"📁 Archivo: catalogo_lifeplus_buscador_ajustado.html")
    print(f"📊 Tamaño: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    print("\n🔧 AJUSTES REALIZADOS:")
    print("  • Botón movido a bottom: 90px (evita solapamiento)")
    print("  • Color naranja (#FF6B35) para diferenciar de WhatsApp verde")
    print("  • Tamaño aumentado: 70x70px (antes 60x60px)")
    print("  • Etiqueta 'BUSCAR' aparece en hover")
    print("  • Modal mejorado con diseño claro")
    print("  • Z-index ajustado (10000)")
    print("  • Placeholder más descriptivo")
    print("  • Iconos de categorías en el select")
    print("\n✅ ESTA VERSIÓN ES CLARAMENTE UN BUSCADOR")

    return True

if __name__ == "__main__":
    print("🎯 CREANDO BUSCADOR FLOTANTE AJUSTADO - CLARO Y VISIBLE")
    print("=" * 60)
    crear_buscador_ajustado()