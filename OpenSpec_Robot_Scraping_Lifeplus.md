# OpenSpec: Robot de Detección de Noveldades LifePlus

> Documento complementario. Ver **`OpenSpec_MASTER.md`** para la referencia completa del proyecto.

## 1. Visión General
Este documento define el procedimiento para utilizar el **Robot LifePlus**, un script automatizado desarrollado en Python que visita la web oficial de LifePlus, lee todo el catálogo dinámico de productos, y lo compara con nuestra base de datos local (`products_data.py`). El objetivo es detectar rápidamente si la marca ha lanzado nuevos productos o ha retirado alguno, sin necesidad de revisar la web manualmente.

---

## 2. Requisitos Previos e Instalación
El robot utiliza una tecnología llamada **Playwright** que permite simular un navegador real (para poder leer páginas hechas en React que cargan contenido dinámicamente).

**Comandos de Instalación (Terminal del Mac):**
Solo necesitas ejecutar esto la primera vez en tu ordenador:
```bash
pip install playwright
playwright install
```

---

## 3. Archivos del Sistema
El sistema se compone de un archivo principal:
- **`robot_lifeplus.py`**: El script ejecutable.

---

## 4. Flujo de Trabajo (Cómo funciona)
1. **Ejecución:** Abres la terminal en tu carpeta `LIFEPLUS WEB PRODUCTOS` y escribes:
   ```bash
   python3 robot_lifeplus.py
   ```
2. **Navegación Oculta:** El script abre la tienda de LifePlus (`https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products?tags=view_all`) de forma invisible.
3. **Espera Inteligente:** El script espera unos segundos a que el motor React de la web cargue completamente los productos.
4. **Scraping (Extracción):** Extrae todos los títulos de los productos y sus enlaces (de los cuales se obtiene el "código de tienda" exacto).
5. **Auditoría Comparativa:** Cruza los códigos extraídos de la web oficial con los códigos de tu archivo local `products_data.py`.

---

## 5. Salida de Datos (Resultados)
El robot imprimirá en la terminal un reporte con este formato:
- 🟢 **PRODUCTOS NUEVOS DETECTADOS:** Si LifePlus ha añadido algo que tú no tienes, te dará el nombre y el ID para que puedas añadirlo usando el procedimiento documentado en `OpenSpec_Catalog_Scraping_Process.md`.
- 🔴 **PRODUCTOS DESCATALOGADOS:** Si tienes un producto en tu web que ya no aparece en la tienda oficial.
- ✅ **TODO AL DÍA:** Si tu catálogo y el oficial coinciden perfectamente.

---

## 6. Mantenimiento
- Si la web de LifePlus cambia de estructura radicalmente (ej. cambian el diseño de la tienda), el script `robot_lifeplus.py` podría necesitar una actualización en los selectores HTML que busca.
- La URL base de la tienda está configurada como `https://ww1.lifeplus.com/...`. Si el país de referencia cambia, se debe cambiar la URL en el script.

## 7. Proceso de Integración Automática (Auto-Inyección)
Se ha añadido una nueva funcionalidad avanzada (`extract_nuevos.py` y `inject_nuevos.py`) que permite no solo detectar los productos nuevos, sino integrarlos directamente en la web.

1. **Extracción**: El robot vuelca todos los descubrimientos a un archivo temporal `nuevos_productos.json`.
2. **Inyección**: El sistema lee este JSON e inyecta dinámicamente los 180+ productos en `products_data.py` bajo una nueva categoría llamada `"nuevos"`.
3. **Despliegue UI**: También inyecta el menú "✨ Novedades (Auto)" en el archivo generador `crear_buscador_funcional.py`.
4. **Seguridad (Ramas Git)**: Todo esto debe hacerse siempre creando primero una rama nueva (`git checkout -b actualizacion-productos`) para evitar romper la web principal (Main/Master) con una entrada masiva de productos sin revisar.

---

## 8. Proceso de Actualización de Packs (Mayo 2026)

### Contexto
La tienda LifePlus publica "packs" (combos de productos nutricionales). Estos packs cambian con frecuencia y tienen precios específicos (normal + ASAP). El proceso para mantenerlos al día es:

### URLs de referencia
- **Búsqueda de packs:** `https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products?search=pack`
- **Tienda completa:** `https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products?tags=view_all`

### Archivos que actualizar (capas duales)
El sistema tiene DOS capas independientes que deben actualizarse por separado:

1. **`crear_buscador_funcional.py`** → Sección `packs` del diccionario de datos JS
   - Datos: code, name, price, price_asap, format
   - Estos datos alimentan el buscador modal

2. **`catalogo_lifeplus_final.html`** → Tarjetas HTML dentro de `<div id="packs" class="category-section">`
   - Tarjetas visibles en la web
   - Patrón de imagen: `https://ww1.lifeplus.com/images/products/prodpic_[CODE]_1@2x.jpg`
   - Patrón de enlace: `https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/[CODE]/[SLUG]`

### Flujo completo
```bash
# 1. Scrapear precios actuales de la tienda (usar Playwright)
# 2. Actualizar crear_buscador_funcional.py (sección packs)
# 3. Añadir tarjetas HTML en catalogo_lifeplus_final.html
# 4. Regenerar el HTML final
python3 crear_buscador_funcional.py
# 5. Copiar a index.html (único archivo de producción)
cp catalogo_lifeplus_buscador_funcional.html index.html
# 6. Subir a GitHub
git add index.html catalogo_lifeplus_final.html crear_buscador_funcional.py catalogo_lifeplus_buscador_funcional.html
git commit -m "feat: actualizar packs"
git push origin main
```

### Despliegue en servidor
**Solo se sube `index.html`** al servidor. Todo está embebido (HTML + CSS + JS + datos).

### Datos actuales (30 packs)
Ver tabla completa en `OpenSpec_Catalog_Scraping_Process.md` → "Implementación Packs Nutricionales (Mayo 2026)".

### Precauciones
- **ID duplicado**: Existen DOS `<div id="packs">` en el HTML. Las tarjetas deben insertarse en la PRIMERA sección (la que tiene el `<h2>` "Packs").
- **Contador**: Actualizar el texto "X productos disponibles" en el `<p>` del header de la sección.
- **SVG fallback**: Cada tarjeta incluye un `onerror` con SVG por si la imagen de LifePlus no carga.
- **Excluir promocionales**: Los productos 2722 (Member estándar), 2465 (Mochila) y 2726 (Member premium) NO son packs nutricionales.
