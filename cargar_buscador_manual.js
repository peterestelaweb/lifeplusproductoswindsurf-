// CARGADOR MANUAL DEL BUSCADOR FLOTANTE
// Este script se carga al final de la página para asegurar inicialización

console.log("🔍 Iniciando cargador manual del buscador...");

function cargarBuscadorManualmente() {
    // Verificar que el DOM esté listo
    if (!document || !document.body) {
        console.error("❌ DOM no está listo");
        return;
    }

    // Verificar si ya existe el buscador
    if (document.getElementById('searchFloatBtn')) {
        console.log("✅ El botón del buscador ya existe");
        return;
    }

    // Esperar a que los productos estén cargados
    let intentos = 0;
    const maxIntentos = 20;

    function verificarProductosYCrearBuscador() {
        intentos++;
        console.log(`🔍 Intento ${intentos}/${maxIntentos}: Verificando productos...`);

        const productos = document.querySelectorAll('.product-card');

        if (productos.length === 0 && intentos < maxIntentos) {
            console.log(`⏳ Esperando productos... (${productos.length} encontrados)`);
            setTimeout(verificarProductosYCrearBuscador, 500);
            return;
        }

        if (productos.length === 0) {
            console.error("❌ No se encontraron productos después de varios intentos");
            return;
        }

        console.log(`✅ Productos encontrados: ${productos.length}`);
        crearBuscador();
    }

    function crearBuscador() {
        console.log("🔧 Creando buscador flotante...");

        // Crear CSS si no existe
        if (!document.querySelector('#search-float-styles')) {
            const css = `
                <style id="search-float-styles">
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
                        z-index: 999 !important;
                        box-shadow: 0 8px 30px rgba(46, 125, 50, 0.15) !important;
                        transition: all 0.3s ease !important;
                        display: flex !important;
                        align-items: center !important;
                        justify-content: center !important;
                        visibility: visible !important;
                        opacity: 1 !important;
                    }
                    .search-float-btn:hover {
                        transform: scale(1.1) !important;
                        box-shadow: 0 8px 40px rgba(46, 125, 50, 0.3) !important;
                    }
                </style>
            `;
            document.head.insertAdjacentHTML('beforeend', css);
            console.log("✅ CSS del buscador añadido");
        }

        // Crear botón flotante
        const botonHTML = `
            <button id="searchFloatBtn" class="search-float-btn" title="Buscar productos">
                <i class="fas fa-search"></i>
            </button>
        `;

        document.body.insertAdjacentHTML('beforeend', botonHTML);
        console.log("✅ Botón flotante creado");

        // Crear modal básico
        const modalHTML = `
            <div id="searchOverlay" class="search-overlay" style="
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0, 0, 0, 0.5); z-index: 1000;
                display: none; backdrop-filter: blur(2px);
            "></div>
            <div id="searchModal" class="search-modal" style="
                position: fixed; top: 50%; left: 50%;
                transform: translate(-50%, -50%); width: 90%;
                max-width: 700px; max-height: 90vh;
                background: white; border-radius: 12px;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
                z-index: 1001; display: none;
                padding: 20px;
            ">
                <h2 style="margin-bottom: 15px;">🔍 Buscar Productos</h2>
                <input type="text" id="searchInput" placeholder="Buscar productos..."
                       style="width: 100%; padding: 12px; border: 2px solid #ddd;
                              border-radius: 8px; margin-bottom: 15px; font-size: 16px;">
                <div id="searchResults" style="max-height: 400px; overflow-y: auto;"></div>
                <button id="closeModalBtn" style="
                    margin-top: 15px; padding: 10px 20px;
                    background: #2E7D32; color: white;
                    border: none; border-radius: 8px;
                    cursor: pointer;
                ">Cerrar</button>
            </div>
        `;

        document.body.insertAdjacentHTML('beforeend', modalHTML);
        console.log("✅ Modal básico creado");

        // Añadir eventos básicos
        const boton = document.getElementById('searchFloatBtn');
        const modal = document.getElementById('searchModal');
        const overlay = document.getElementById('searchOverlay');
        const closeBtn = document.getElementById('closeModalBtn');
        const searchInput = document.getElementById('searchInput');

        if (boton && modal && overlay && closeBtn) {
            boton.addEventListener('click', () => {
                modal.style.display = 'block';
                overlay.style.display = 'block';
                boton.style.visibility = 'hidden';
                if (searchInput) searchInput.focus();
            });

            closeBtn.addEventListener('click', () => {
                modal.style.display = 'none';
                overlay.style.display = 'none';
                boton.style.visibility = 'visible';
            });

            overlay.addEventListener('click', () => {
                modal.style.display = 'none';
                overlay.style.display = 'none';
                boton.style.visibility = 'visible';
            });

            console.log("✅ Eventos del buscador configurados");

            // Forzar visibilidad del botón
            setTimeout(() => {
                boton.style.display = 'flex';
                boton.style.visibility = 'visible';
                boton.style.opacity = '1';
                console.log("✅ Botón del buscador forzado a visible");
            }, 100);

            console.log("🎉 ¡Buscador flotante cargado manualmente con éxito!");
        } else {
            console.error("❌ Error creando elementos del buscador");
        }
    }

    // Iniciar verificación
    verificarProductosYCrearBuscador();
}

// Iniciar cuando la página esté completamente cargada
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', cargarBuscadorManualmente);
} else {
    cargarBuscadorManualmente();
}

// Also try with window load as fallback
window.addEventListener('load', () => {
    setTimeout(() => {
        if (!document.getElementById('searchFloatBtn')) {
            console.log("🔄 Intentando carga alternativa del buscador...");
            cargarBuscadorManualmente();
        }
    }, 3000);
});

console.log("✅ Cargador manual del buscador inicializado");