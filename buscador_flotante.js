// BUSCADOR FLOTANTE INTELIGENTE PARA LIFEPLUS
// Implementación completa siguiendo las especificaciones

// Objeto para almacenar productos extraídos del DOM
let productosLifePlus = [];
let categoriasLifePlus = [];

// 1. FUNCIÓN PARA EXTRAER PRODUCTOS DEL DOM
function extraerProductos() {
    console.log("Extrayendo productos del DOM...");

    const categorySections = document.querySelectorAll('.category-section');

    categorySections.forEach(section => {
        const categoryId = section.id;
        const categoryTitle = section.querySelector('.category-title');

        if (!categoryTitle || categoryId === 'welcome') return;

        const categoryName = categoryTitle.textContent.trim();
        categoriasLifePlus.push({
            id: categoryId,
            nombre: categoryName
        });

        const productCards = section.querySelectorAll('.product-card');

        productCards.forEach(card => {
            try {
                const productCode = card.querySelector('.product-code')?.textContent.trim();
                const productName = card.querySelector('.product-name')?.textContent.trim();
                const productFormat = card.querySelector('.product-format')?.textContent.trim();
                const productImage = card.querySelector('.product-image')?.src;
                const productLink = card.querySelector('.product-link')?.href;

                // Extraer precios
                let precioNormal = "";
                let precioASAP = "";
                const priceElements = card.querySelectorAll('.product-price, .product-price-asap');

                priceElements.forEach((elem, index) => {
                    if (elem.classList.contains('product-price')) {
                        precioNormal = elem.textContent.trim();
                    } else if (elem.classList.contains('product-price-asap')) {
                        precioASAP = elem.textContent.trim();
                    }
                });

                if (productCode && productName) {
                    productosLifePlus.push({
                        id: productCode,
                        nombre: productName,
                        categoria: categoryId,
                        categoriaNombre: categoryName,
                        formato: productFormat,
                        imagen: productImage,
                        precioNormal: precioNormal,
                        precioASAP: precioASAP,
                        url: productLink,
                        // Nombre normalizado para búsqueda fuzzy
                        nombreNormalizado: normalizarTexto(productName),
                        categoriaNormalizada: normalizarTexto(categoryName)
                    });
                }
            } catch (error) {
                console.error("Error extrayendo producto:", error);
            }
        });
    });

    console.log(`Se extrajeron ${productosLifePlus.length} productos`);
    console.log(`Se encontraron ${categoriasLifePlus.length} categorías`);
}

// 2. FUNCIÓN PARA NORMALIZAR TEXTO (quitar acentos, caracteres especiales)
function normalizarTexto(texto) {
    return texto.toLowerCase()
        .replace(/[áàäâ]/g, 'a')
        .replace(/[éèëê]/g, 'e')
        .replace(/[íìïî]/g, 'i')
        .replace(/[óòöô]/g, 'o')
        .replace(/[úùüû]/g, 'u')
        .replace(/[ñ]/g, 'n')
        .replace(/[ç]/g, 'c')
        .replace(/[®™°]/g, '')
        .replace(/[^\w\s]/g, ' ')
        .replace(/\s+/g, ' ')
        .trim();
}

// 3. ALGORITMO LEVENSHTEIN DISTANCE para búsqueda fuzzy
function levenshteinDistance(str1, str2) {
    const matrix = [];

    for (let i = 0; i <= str2.length; i++) {
        matrix[i] = [i];
    }

    for (let j = 0; j <= str1.length; j++) {
        matrix[0][j] = j;
    }

    for (let i = 1; i <= str2.length; i++) {
        for (let j = 1; j <= str1.length; j++) {
            if (str2.charAt(i - 1) === str1.charAt(j - 1)) {
                matrix[i][j] = matrix[i - 1][j - 1];
            } else {
                matrix[i][j] = Math.min(
                    matrix[i - 1][j - 1] + 1,
                    matrix[i][j - 1] + 1,
                    matrix[i - 1][j] + 1
                );
            }
        }
    }

    return matrix[str2.length][str1.length];
}

// 4. FUNCIÓN PARA CALCULAR SIMILITUD
function calcularSimilitud(str1, str2) {
    const distance = levenshteinDistance(str1, str2);
    const longer = Math.max(str1.length, str2.length);
    if (longer === 0) return 1.0;
    return (longer - distance) / longer;
}

// 5. FUNCIÓN DE BÚSQUEDA PRINCIPAL
function buscarProductos(textoBusqueda, categoriaId = 'todas') {
    if (!textoBusqueda || textoBusqueda.trim() === '') {
        // Si no hay texto, mostrar productos de la categoría seleccionada
        if (categoriaId === 'todas') {
            return productosLifePlus;
        } else {
            return productosLifePlus.filter(p => p.categoria === categoriaId);
        }
    }

    const textoNormalizado = normalizarTexto(textoBusqueda);
    const palabrasBusqueda = textoNormalizado.split(' ').filter(p => p.length > 0);

    const resultados = productosLifePlus.map(producto => {
        // Filtrar por categoría si no es "todas"
        if (categoriaId !== 'todas' && producto.categoria !== categoriaId) {
            return null;
        }

        let scoreMaximo = 0;
        let matchTipo = '';

        // Buscar coincidencia exacta
        if (producto.nombreNormalizado.includes(textoNormalizado)) {
            scoreMaximo = 1.0;
            matchTipo = 'exacto';
        } else {
            // Calcular similitud fuzzy para cada palabra
            palabrasBusqueda.forEach(palabra => {
                if (palabra.length < 2) return; // Ignorar palabras muy cortas

                // Buscar en nombre del producto
                const similitudNombre = calcularSimilitud(palabra, producto.nombreNormalizado);
                if (similitudNombre > scoreMaximo) {
                    scoreMaximo = similitudNombre;
                    matchTipo = 'nombre_fuzzy';
                }

                // Buscar coincidencias parciales
                if (producto.nombreNormalizado.includes(palabra) && scoreMaximo < 0.8) {
                    scoreMaximo = 0.8;
                    matchTipo = 'parcial';
                }

                // Buscar en categoría
                if (producto.categoriaNormalizada.includes(palabra) && scoreMaximo < 0.6) {
                    scoreMaximo = 0.6;
                    matchTipo = 'categoria';
                }
            });
        }

        // Umbral mínimo de similitud
        if (scoreMaximo >= 0.6) {
            return {
                ...producto,
                score: scoreMaximo,
                matchTipo: matchTipo
            };
        }

        return null;
    }).filter(p => p !== null)
     .sort((a, b) => b.score - a.score); // Ordenar por relevancia

    return resultados;
}

// 6. FUNCIÓN PARA RENDERIZAR RESULTADOS
function renderizarResultados(resultados) {
    const contenedorResultados = document.getElementById('searchResults');
    const contadorResultados = document.getElementById('resultsCount');
    const mensajeNoResultados = document.getElementById('noResultsMessage');

    // Actualizar contador
    if (contadorResultados) {
        contadorResultados.textContent = `${resultados.length} producto${resultados.length !== 1 ? 's' : ''} encontrado${resultados.length !== 1 ? 's' : ''}`;
    }

    // Limpiar contenedor
    contenedorResultados.innerHTML = '';

    // Mostrar/ocultar mensaje de no resultados
    if (mensajeNoResultados) {
        mensajeNoResultados.style.display = resultados.length === 0 ? 'block' : 'none';
    }

    if (resultados.length === 0) {
        return;
    }

    // Renderizar productos en grid
    resultados.forEach(producto => {
        const productoCard = crearProductoCard(producto);
        contenedorResultados.appendChild(productoCard);
    });
}

// 7. FUNCIÓN PARA CREAR TARJETA DE PRODUCTO
function crearProductoCard(producto) {
    const card = document.createElement('div');
    card.className = 'search-result-product';
    card.onclick = () => {
        window.open(producto.url, '_blank');
        setTimeout(() => cerrarModal(), 500); // Cerrar modal después de abrir link
    };

    const precioHTML = producto.precioASAP ?
        `<div class="result-prices">
            <span class="result-price">${producto.precioNormal}</span>
            <span class="result-price-asap">${producto.precioASAP}</span>
        </div>` :
        `<div class="result-prices">
            <span class="result-price">${producto.precioNormal}</span>
        </div>`;

    card.innerHTML = `
        <div class="result-image">
            <img src="${producto.imagen}" alt="${producto.nombre}"
                 onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22 viewBox=%220 0 80 80%22><rect width=%2280%22 height=%2280%22 fill=%22%23f0f0f0%22/><text x=%2240%22 y=%2240%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22Arial%22 font-size=%2210%22 fill=%22%23666%22>Sin imagen</text></svg>';">
        </div>
        <div class="result-info">
            <h3 class="result-name">${producto.nombre}</h3>
            <p class="result-category">${producto.categoriaNombre}</p>
            <p class="result-format">${producto.formato}</p>
            ${precioHTML}
            <a href="${producto.url}" target="_blank" class="result-link">Ver producto →</a>
        </div>
    `;

    return card;
}

// 8. FUNCIONES PARA MANEJAR MODAL
function abrirModal() {
    const modal = document.getElementById('searchModal');
    const overlay = document.getElementById('searchOverlay');
    const botonFlotante = document.getElementById('searchFloatBtn');
    const inputBusqueda = document.getElementById('searchInput');

    if (modal && overlay && botonFlotante) {
        overlay.style.display = 'block';
        modal.classList.add('modal-active');
        botonFlotante.style.visibility = 'hidden';

        // Autofocus en el input
        setTimeout(() => {
            if (inputBusqueda) {
                inputBusqueda.focus();
                inputBusqueda.value = '';
                ejecutarBusqueda();
            }
        }, 100);
    }
}

function cerrarModal() {
    const modal = document.getElementById('searchModal');
    const overlay = document.getElementById('searchOverlay');
    const botonFlotante = document.getElementById('searchFloatBtn');

    if (modal && overlay && botonFlotante) {
        overlay.style.display = 'none';
        modal.classList.remove('modal-active');
        botonFlotante.style.visibility = 'visible';
    }
}

// 9. FUNCIÓN DE EJECUCIÓN DE BÚSQUEDA
let timeoutBusqueda;
function ejecutarBusqueda() {
    clearTimeout(timeoutBusqueda);

    timeoutBusqueda = setTimeout(() => {
        const inputBusqueda = document.getElementById('searchInput');
        const selectCategoria = document.getElementById('categoryFilter');

        if (!inputBusqueda) return;

        const texto = inputBusqueda.value;
        const categoriaId = selectCategoria ? selectCategoria.value : 'todas';

        const resultados = buscarProductos(texto, categoriaId);
        renderizarResultados(resultados);

        // Mostrar mensaje inicial si no hay texto
        const mensajeInicial = document.getElementById('initialMessage');
        if (mensajeInicial) {
            mensajeInicial.style.display = texto.trim() === '' ? 'block' : 'none';
        }
    }, 300); // Debounce de 300ms
}

// 10. FUNCIÓN PARA LIMPIAR BÚSQUEDA
function limpiarBusqueda() {
    const inputBusqueda = document.getElementById('searchInput');
    const selectCategoria = document.getElementById('categoryFilter');

    if (inputBusqueda) inputBusqueda.value = '';
    if (selectCategoria) selectCategoria.value = 'todas';

    ejecutarBusqueda();
}

// 11. FUNCIÓN PRINCIPAL DE INICIALIZACIÓN
function inicializarBuscadorFlotante() {
    console.log("Inicializando buscador flotante...");

    // Extraer productos del DOM
    extraerProductos();

    // Crear HTML del buscador
    crearHTMLBuscador();

    // Agregar event listeners
    agregarEventListeners();

    console.log("Buscador flotante inicializado correctamente");
}

// 12. FUNCIÓN PARA CREAR HTML DEL BUSCADOR
function crearHTMLBuscador() {
    // Crear botón flotante
    const botonHTML = `
        <button id="searchFloatBtn" class="search-float-btn" title="Buscar productos">
            <i class="fas fa-search"></i>
        </button>
    `;

    // Crear overlay y modal
    const modalHTML = `
        <div id="searchOverlay" class="search-overlay"></div>

        <div id="searchModal" class="search-modal">
            <div class="search-modal-header">
                <h2><i class="fas fa-search"></i> Buscar Productos</h2>
                <button id="closeModalBtn" class="close-modal-btn" title="Cerrar">
                    <i class="fas fa-times"></i>
                </button>
            </div>

            <div class="search-modal-body">
                <div class="search-input-container">
                    <i class="fas fa-search search-input-icon"></i>
                    <input type="text" id="searchInput" class="search-input"
                           placeholder="Buscar productos..." autocomplete="off">
                    <button id="clearSearchBtn" class="clear-search-btn" style="display: none;" title="Limpiar">
                        <i class="fas fa-times"></i>
                    </button>
                </div>

                <div class="search-filters">
                    <label for="categoryFilter">Filtrar por categoría:</label>
                    <select id="categoryFilter" class="category-filter">
                        <option value="todas">Todas las categorías</option>
                    </select>
                </div>

                <div class="search-results-info">
                    <span id="resultsCount" class="results-count">0 productos encontrados</span>
                </div>

                <div class="search-messages">
                    <div id="initialMessage" class="initial-message">
                        <i class="fas fa-info-circle"></i>
                        Empieza a escribir para buscar productos
                    </div>
                    <div id="noResultsMessage" class="no-results-message" style="display: none;">
                        <i class="fas fa-search"></i>
                        No encontramos productos que coincidan con tu búsqueda.<br>
                        Intenta con otro nombre o categoría.
                    </div>
                </div>

                <div id="searchResults" class="search-results"></div>
            </div>

            <div class="search-modal-footer">
                <button id="clearAllBtn" class="btn btn-secondary">
                    <i class="fas fa-eraser"></i> Limpiar
                </button>
                <button id="closeFooterBtn" class="btn btn-primary">
                    <i class="fas fa-times"></i> Cerrar
                </button>
            </div>
        </div>
    `;

    // Insertar en el body
    document.body.insertAdjacentHTML('beforeend', botonHTML + modalHTML);

    // Poblar categorías en el select
    const categorySelect = document.getElementById('categoryFilter');
    if (categorySelect && categoriasLifePlus.length > 0) {
        categoriasLifePlus.forEach(cat => {
            const option = document.createElement('option');
            option.value = cat.id;
            option.textContent = cat.nombre;
            categorySelect.appendChild(option);
        });
    }
}

// 13. FUNCIÓN PARA AGREGAR EVENT LISTENERS
function agregarEventListeners() {
    // Botón flotante
    const botonFlotante = document.getElementById('searchFloatBtn');
    if (botonFlotante) {
        botonFlotante.addEventListener('click', abrirModal);
    }

    // Cerrar modal
    const closeModalBtn = document.getElementById('closeModalBtn');
    const closeFooterBtn = document.getElementById('closeFooterBtn');
    const overlay = document.getElementById('searchOverlay');

    if (closeModalBtn) closeModalBtn.addEventListener('click', cerrarModal);
    if (closeFooterBtn) closeFooterBtn.addEventListener('click', cerrarModal);
    if (overlay) overlay.addEventListener('click', cerrarModal);

    // Búsqueda
    const inputBusqueda = document.getElementById('searchInput');
    const clearSearchBtn = document.getElementById('clearSearchBtn');
    const clearAllBtn = document.getElementById('clearAllBtn');
    const categoryFilter = document.getElementById('categoryFilter');

    if (inputBusqueda) {
        inputBusqueda.addEventListener('input', () => {
            const tieneTexto = inputBusqueda.value.trim().length > 0;
            if (clearSearchBtn) {
                clearSearchBtn.style.display = tieneTexto ? 'block' : 'none';
            }
            ejecutarBusqueda();
        });

        inputBusqueda.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                // Opcional: enfocar primer resultado
            }
        });
    }

    if (clearSearchBtn) {
        clearSearchBtn.addEventListener('click', () => {
            if (inputBusqueda) inputBusqueda.value = '';
            clearSearchBtn.style.display = 'none';
            ejecutarBusqueda();
            if (inputBusqueda) inputBusqueda.focus();
        });
    }

    if (clearAllBtn) {
        clearAllBtn.addEventListener('click', limpiarBusqueda);
    }

    if (categoryFilter) {
        categoryFilter.addEventListener('change', ejecutarBusqueda);
    }

    // Cerrar con ESC
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            cerrarModal();
        }
    });
}

// 14. INICIALIZAR CUANDO EL DOM ESTÉ LISTO
document.addEventListener('DOMContentLoaded', () => {
    // Esperar un poco a que la página cargue completamente
    setTimeout(() => {
        inicializarBuscadorFlotante();
    }, 1000);
});

// También inicializar si la página ya cargó
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inicializarBuscadorFlotante);
} else {
    setTimeout(inicializarBuscadorFlotante, 1000);
}

console.log("Script de buscador flotante cargado");