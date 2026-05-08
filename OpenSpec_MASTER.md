# OpenSpec MASTER — LIFEPLUS WEB PRODUCTOS

> Fuente única de verdad. Todo lo que existe, cómo funciona y cómo se trabaja en este proyecto.

---

## 1. Qué es este proyecto

Catálogo web estático de productos LifePlus con buscador flotante. Un solo archivo HTML (`index.html`) contiene todo: estructura, estilos, JavaScript y base de datos de productos. No hay backend, no hay framework, no hay base de datos externa.

**URL producción:** la que apunte tu servidor al `index.html`
**Repo GitHub:** `https://github.com/peterestelaweb/lifeplusproductoswindsurf-.git`
**Código afiliado LifePlus:** `SHVCB5`
**País/idioma:** España / Español (`es/es`)

---

## 2. Stack Tecnológico

| Capa | Tecnología | Detalle |
|------|-----------|---------|
| Frontend | HTML estático + JavaScript vanilla | Sin framework |
| Estilos | CSS inline embebido | Montserrat, Font Awesome, colores LifePlus |
| Buscador | MicroModal.js (1.8KB) | Modal accesible MIT |
| Generadores | Python 3 | Scripts que producen el HTML final |
| Scraping | Playwright (Python) | Navegación headless de tienda LifePlus |
| Servidor local | `npx http-server -p 8080` | Para desarrollo |
| Segundo cerebro | NotebookLM (WrapUp) | Contexto persistente entre sesiones |

### Paleta de colores
- Verde principal: `#2E7D32`
- Verde medio: `#4CAF50`
- Verde claro: `#66BB6A`
- Botón buscador: naranja (diferenciado del verde WhatsApp)
- Fondo: `#faf8f5` (crema)

### Tipografía
- Headlines: Montserrat 700
- Cuerpo: Montserrat 400
- Precios: Montserrat 600

---

## 3. Arquitectura Dual de Datos (CRÍTICO)

El catálogo tiene **DOS capas independientes** que deben actualizarse por separado:

### Capa 1: Tarjetas HTML (visualización)
- Archivo: `catalogo_lifeplus_final.html`
- Son las tarjetas de producto que se ven en la web
- Dentro de `<div class="products-grid">` de cada sección de categoría
- Cada tarjeta es un `<div class="product-card">` con imagen, código, precios, nombre, formato y enlace

### Capa 2: Arrays JavaScript (buscador modal)
- Archivo: `crear_buscador_funcional.py` → sección de datos de productos
- Diccionario Python que se convierte a objeto JS `productosLifePlus`
- Alimenta el buscador flotante con filtros por categoría

**Ambas capas deben coincidir.** Si añades un producto solo en una, no aparecerá completo.

---

## 4. Flujo de Build (Cómo se genera el HTML final)

```
catalogo_lifeplus_final.html    ← Base HTML con tarjetas estáticas
        │
        ▼
crear_buscador_funcional.py     ← Lee la base, inyecta CSS+JS+datos
        │
        ▼
catalogo_lifeplus_buscador_funcional.html  ← HTML completo generado
        │
        ▼ (copia)
index.html                      ← ARCHIVO DE PRODUCCIÓN (subir solo este)
```

### Comando de build
```bash
python3 crear_buscador_funcional.py
cp catalogo_lifeplus_buscador_funcional.html index.html
```

### Despliegue
**Solo se sube `index.html` al servidor.** Todo está embebido.

```bash
git add index.html catalogo_lifeplus_final.html crear_buscador_funcional.py
git commit -m "feat: descripción del cambio"
git push origin main
```

---

## 5. Inventario de Archivos

### Archivos que importan (los que se tocan)

| Archivo | Para qué sirve | Cuándo se modifica |
|---------|---------------|-------------------|
| `catalogo_lifeplus_final.html` | Base HTML con tarjetas visibles | Al añadir/modificar productos |
| `crear_buscador_funcional.py` | Generador principal + datos JS del buscador | Al añadir/modificar productos |
| `index.html` | Producción (copia del generado) | Siempre después del build |
| `completar_categorias.py` | Base de datos maestra (dict Python) | Al actualizar datos de productos |
| `products_data.py` | Base de datos alternativa (usa `robot_lifeplus.py`) | Al detectar nuevos productos |
| `robot_lifeplus.py` | Robot Playwright de detección de novedades | Si cambia la web de LifePlus |

### Archivos de soporte

| Archivo | Para qué sirve |
|---------|---------------|
| `product_images_generator.py` | Genera `product_images.json` con URLs de imágenes |
| `extract_nuevos.py` | Extrae productos nuevos de la tienda → `nuevos_productos.json` |
| `inject_nuevos.py` | Inyecta productos del JSON en `products_data.py` |
| `fix_pets_codes.py` | Corrigió códigos de mascotas (6687→3534, etc.) |
| `buscador_flotante.js` | JS del buscador flotante (versión externa, no usada en producción) |
| `buscador_flotante.css` | CSS del buscador flotante (versión externa, no usada en producción) |
| `micromodal.min.js` | Librería MicroModal.js para modales accesibles |

### Archivos intermedios (no tocar)

Todos los `catalogo_lifeplus_*.html` excepto `catalogo_lifeplus_final.html` son versiones anteriores o intermedias del catálogo. No se usan en producción.

### Archivos de datos

| Archivo | Contenido |
|---------|----------|
| `nuevos_productos.json` | 189 productos scrapeados con precio 0.00 |
| `product_images.json` | Mapeo código→URLs de imágenes |
| `package.json` | Dependencia: playwright ^1.59.1 |

---

## 6. Patrones URL de LifePlus

### Tienda
- **Catálogo completo:** `https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products?tags=view_all`
- **Buscar packs:** `https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products?search=pack`
- **Buscar por texto:** `https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products?search=[TEXTO]`

### Producto individual
- **Página:** `https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/[CÓDIGO]/[SLUG]`
- **Imagen:** `https://ww1.lifeplus.com/images/products/prodpic_[CÓDIGO]_1@2x.jpg`

### Notas sobre URLs
- El código afiliado `SHVCB5` aparece en las URLs de compra
- La M mayúscula (`/M/`) es para la versión mobile/web-page
- La S mayúscula (`/S/`) es para product-details
- El slug es el nombre del producto en minúsculas, espacios→guiones, especiales eliminados
- Las imágenes siguen un patrón fijo basado en el código de producto

---

## 7. Cómo añadir un producto nuevo

### Opción A: Producto individual (manual)

**Paso 1 — Obtener datos:**
1. Buscar el producto en `https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products`
2. Anotar: código, nombre, precio normal, precio ASAP, formato, slug

**Paso 2 — Actualizar capa de datos (buscador):**
1. Abrir `crear_buscador_funcional.py`
2. Encontrar la sección de la categoría correspondiente
3. Añadir entrada: `{"code": "...", "name": "...", "price": "€...", "price_asap": "€...", "format": "..."}`

**Paso 3 — Actualizar capa visual (tarjetas HTML):**
1. Abrir `catalogo_lifeplus_final.html`
2. Encontrar la sección de categoría correcta (`<div id="[categoría]" class="category-section">`)
3. Copiar una tarjeta existente como plantilla
4. Cambiar: código, nombre, precios, formato, slug, alt de imagen
5. Actualizar el contador "X productos disponibles"

**Paso 4 — Build y deploy:**
```bash
python3 crear_buscador_funcional.py
cp catalogo_lifeplus_buscador_funcional.html index.html
```

### Opción B: Múltiples productos (scraping)

1. Ejecutar `python3 robot_lifeplus.py` para detectar novedades
2. Ejecutar `python3 extract_nuevos.py` para extraer datos a JSON
3. Ejecutar `python3 inject_nuevos.py` para inyectar en el sistema
4. Regenerar con build

### Opción C: Packs (proceso específico)

1. Scrapear `https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products?search=pack` con Playwright
2. Excluir productos promocionales (Member, Mochila)
3. Actualizar sección `packs` en `crear_buscador_funcional.py`
4. Añadir tarjetas HTML en `catalogo_lifeplus_final.html` dentro de `<div id="packs">`
5. Actualizar contador de productos
6. Build + deploy

---

## 8. Categorías de Productos

| ID en HTML | Nombre | Icono | Productos |
|-----------|--------|-------|-----------|
| `packs` | Packs | `fa-box` | 30 |
| `nutricionales` | Productos Nutricionales | `fa-capsules` | 60 |
| `alimentos` | Alimentos | `fa-utensils` | ~15 |
| `proteinas` | Proteínas | `fa-dumbbell` | 7 |
| `deportiva` | Línea Deportiva | `fa-running` | 14 |
| `superfoods` | Superfoods | `fa-leaf` | 4 |
| `forever-young` | Forever Young | `fa-spa` | 7 |
| `piel` | Salud de la Piel | `fa-heart` | ~8 |
| `personal` | Cuidado Personal | `fa-pump-soap` | 8 |
| `accesorios` | Accesorios | `fa-box-open` | 4 |
| `agua` | Agua | `fa-tint` | 2 |
| `pets` | Pets | `fa-paw` | 7 |
| `nuevos` | Novedades | `fa-star` | 189 (auto) |

---

## 9. Estructura HTML de una Tarjeta de Producto

```html
<div class="product-card">
    <div class="product-image-container">
        <img src="https://ww1.lifeplus.com/images/products/prodpic_[CÓDIGO]_1@2x.jpg"
             alt="[NOMBRE]"
             class="product-image"
             onerror="this.onerror=null; this.src='data:image/svg+xml,...';">
    </div>
    <div class="product-header">
        <span class="product-code">[CÓDIGO]</span>
        <div class="product-prices">
            <span class="product-price">€[PRECIO]</span>
            <span class="product-price-asap">€[PRECIO_ASAP]</span>
        </div>
    </div>
    <h3 class="product-name">[NOMBRE]</h3>
    <p class="product-format">[FORMATO]</p>
    <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/[CÓDIGO]/[SLUG]"
       target="_blank" class="product-link">
        <i class="fas fa-shopping-cart"></i>
        <span>Comprar en Tienda</span>
    </a>
</div>
```

### SVG Fallback (para imágenes que no cargan)
```
data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 80 80"><rect width="80" height="80" fill="%23f0f0f0"/><text x="40" y="40" text-anchor="middle" dy="0.3em" font-family="Arial" font-size="10" fill="%23666">[TEXTO_CORTO]</text></svg>
```

---

## 10. Buscador Flotante

### Cómo funciona
1. Botón naranja fijo en esquina inferior derecha (bottom: 320px, z-index: 9998)
2. Al pulsar abre un modal (MicroModal.js) con buscador
3. Búsqueda en tiempo real por nombre, código o formato
4. Filtro por categoría con dropdown
5. Resultados muestran imagen, nombre, código, precios y enlace

### Componentes
- **Botón flotante:** `<button id="searchFloatBtn">` con CSS fijo
- **Modal:** `<div class="micromodal-slide" id="modal-buscador">`
- **Datos:** Objeto JS `productosLifePlus` con todos los productos por categoría
- **Búsqueda:** Filtra en `productosLifePlus` y renderiza resultados dinámicamente

### Personalización
- El botón parpadea para indicar funcionamiento
- Cierra con X o tecla Escape
- Responsive: se adapta a móvil

---

## 11. Robot de Detección de Novedades

### Script: `robot_lifeplus.py`
- Usa Playwright en modo headless
- Navega la tienda LifePlus completa
- Extrae códigos y nombres de productos
- Compara con `products_data.py`
- Reporta: nuevos productos, descatalogados, o todo al día

### Instalación (solo primera vez)
```bash
pip install playwright
playwright install
```

### Ejecución
```bash
python3 robot_lifeplus.py
```

### Salida esperada
- Nuevos productos detectados con nombre y código
- Productos que ya no están en la tienda
- Confirmación de que todo está al día

---

## 12. Problemas Conocidos y Precauciones

### ID duplicado "packs"
Existen DOS `<div id="packs">` en `catalogo_lifeplus_final.html`:
- Primero (~línea 2832): Sección "Packs" con los 30 productos
- Segundo (~línea 4474): "Packs de Recomendación"
- Al insertar tarjetas, verificar que van en la sección correcta

### Códigos de producto vs códigos de PDF
Los PDFs técnicos usan códigos internos distintos a los de tienda. Siempre usar el **código de tienda** (visible en la URL del producto). Ejemplo: PDF dice 6687, tienda usa 3534.

### Precios ASAP
Los precios ASAP son ~9.5% menores que el precio normal. Fórmula usada históricamente: `precio_normal * 0.945`. Los precios reales deben tomarse siempre de la tienda.

### Imágenes que no cargan
Algunos productos (ej. Pets Mobile App) no tienen imagen oficial. El `onerror` del `<img>` muestra un SVG gris con el nombre del producto.

### Scripts temporales
Los scripts como `_insert_packs.py` son de un solo uso. Se pueden eliminar tras ejecutarse.

---

## 13. Historial de Implementaciones

### Línea Pets (Abril 2026)
- 7 productos de mascotas integrados
- Corrección de códigos internos a códigos de tienda (6687→3534, etc.)
- Sección nueva con icono `fa-paw`

### Auto-incorporación masiva (Abril 2026)
- 189 productos nuevos detectados por robot Playwright
- Inyección automática en categoría "nuevos"
- Commit: `929dbcf feat: Auto-incorporación de 189 productos nuevos mediante robot Playwright`

### Packs nutricionales (Mayo 2026)
- 30 packs con precios reales extraídos de la tienda
- 24 tarjetas HTML nuevas añadidas
- 59 stubs duplicados eliminados de sección nuevos
- Scrapeados de 3 páginas de resultados (33 total, 3 promocionales excluidos)
- Commit: `a4bcb27 feat: Añadir 24 nuevos packs nutricionales con precios reales`

### Buscador funcional (Abril-Mayo 2026)
- Botón naranja flotante con MicroModal.js
- Búsqueda en tiempo real por nombre/código/formato
- Filtro por categorías
- Múltiples iteraciones para posicionar el botón sin solapar WhatsApp
- Commits: `a38a0c2`, `912790d`, `7e3c6dc`, `18890d2`

---

## 14. Cómo se trabaja con IA (Claude Code)

### Herramientas usadas
- **Claude Code CLI** como asistente principal
- **Playwright MCP** para scraping interactivo de la tienda
- **NotebookLM (WrapUp)** como segundo cerebro persistente
- **Dispatch rule** consulta reglas del cerebro antes de cada tarea

### Configuración
- `.claude/settings.local.json` — Permisos para Python, git, bash, browser MCP, NotebookLM
- `.wrapup-config` — ID del notebook del proyecto para WrapUp
- `~/.claude/rules/common/dispatch.md` — Regla de consulta al cerebro

### Flujo típico de sesión
1. Arrancar servidor: `npx http-server -p 8080`
2. Hacer la tarea (scraping, añadir productos, corregir)
3. Build: `python3 crear_buscador_funcional.py && cp output index.html`
4. Verificar en `http://localhost:8080`
5. Commit + push a GitHub
6. `/wrapup` para guardar contexto en NotebookLM

### Archivos que generó la IA y no se deben tocar manualmente
- `catalogo_lifeplus_buscador_funcional.html` — Se regenera automáticamente
- `index.html` — Es copia del anterior
- Los scripts patch (`_insert_packs.py`, etc.) son temporales

---

## 15. Contacto y Referencias

- **Tienda LifePlus:** https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products
- **GitHub:** https://github.com/peterestelaweb/lifeplusproductoswindsurf-.git
- **NotebookLM:** Brain LIFEPLUS-PETS (contexto del proyecto)
- **OpenSpec relacionados:**
  - `OpenSpec_Robot_Scraping_Lifeplus.md` — Guía del robot de detección
  - `OpenSpec_Catalog_Scraping_Process.md` — Flujo de integración de productos

---

*Última actualización: 8 de mayo de 2026*
*Mantenido por: Mayka Centeno + Claude Code*
