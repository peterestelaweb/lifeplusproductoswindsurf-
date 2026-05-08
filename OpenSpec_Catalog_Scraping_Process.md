# OpenSpec: Flujo de Trabajo para Incorporar Nuevos Productos LifePlus

> Documento complementario. Ver **`OpenSpec_MASTER.md`** para la referencia completa del proyecto.

## 1. Visión General
Este documento (OpenSpec) define el procedimiento técnico y metodológico (el "escarapín" o scraping) que utilizamos para integrar nuevos productos de LifePlus —como la línea **Pets**— al catálogo web inteligente y funcional. Mantener este documento actualizado asegura que cualquier producto nuevo se pueda incorporar en cuestión de minutos siguiendo los mismos estándares de calidad y diseño de la página.

---

## 2. Paso a Paso: El Proceso de Integración

### FASE 1: Recopilación de Datos (Data Scraping)
Cuando LifePlus lanza una nueva línea de productos, necesitamos recopilar su información básica.
1. **Fichas Técnicas (PDF):** Se descargan los PDF informativos desde la web oficial a una carpeta local (Ej. `/PETS FICHAS/`).
2. **Extracción con Python:** Se utiliza un script de Python con la librería `pypdf` para escanear estos documentos y extraer automáticamente:
   - Nombre completo del producto
   - Formato (Peso, cápsulas, aerosol, etc.)
   - Beneficios y breve descripción
3. **Mapeo de Códigos Exactos (CRÍTICO):** A veces, el código interno del PDF no coincide con el código de tienda web (Store ID). **Se debe verificar el ID de tienda** mirando la URL de compra del producto. 
   *Ejemplo: El PDF de "Pets Calm" menciona el código 6687, pero el enlace de la tienda utiliza el ID **3534** (`/product-details/3534/`). Siempre debemos usar el ID de la tienda para que funcionen las fotos y los botones de compra.*

### FASE 2: Inserción en la Base de Datos (`products_data.py`)
Toda la información estructurada se inserta en el diccionario principal de Python que alimenta el catálogo. Se debe crear una nueva categoría si es necesario (ej. `"pets": [...]`).

```python
{
    'code': '3534', # Código verificado de la tienda
    'name': 'Lifeplus Pets™ Calm',
    'format': '90 Masticables (135g)',
    'price': 0.00, # Se actualiza manualmente
    'price_asap': 0.00,
    'description': 'Masticables blandos para equilibrar el comportamiento.',
    'benefits': ['Calma', 'Bienestar']
}
```

### FASE 3: Generación Automática de Recursos Visuales
El sistema depende del "Store ID" para automatizar la inserción de imágenes y enlaces:
- **Fotos:** El generador construye la URL de la imagen automáticamente usando este patrón: `https://ww1.lifeplus.com/images/products/prodpic_[CÓDIGO]_1@2x.jpg`. 
  - *(Nota: Si la foto no existe, como en el caso de la Mobile App, el sistema insertará una imagen SVG temporal por defecto con el nombre del producto, hasta que se proporcione una URL de imagen oficial).*
- **Enlaces de Compra:** El generador inserta el enlace de afiliado o directo estructurado como: `https://ww1.lifeplus.com/SHVCB5/M/es/es/product-details/[CÓDIGO]/[SLUG_DEL_PRODUCTO]`.

### FASE 4: Actualización del Generador Principal (`crear_buscador_funcional.py`)
Para que la nueva categoría aparezca en la Interfaz de Usuario (UI) y en el buscador:
1. **Actualizar el menú `<select>`:** Se añade la nueva opción de categoría en el HTML del modal de búsqueda (`<option value="pets">🐾 Pets</option>`).
2. **Actualizar diccionarios de Iconos en JS:** Se inyecta el icono asociado (`'pets': '🐾'`) y su etiqueta de texto (`'pets': 'Pets'`) en las variables de inicialización del archivo generador.
3. **Inyectar la sección en el HTML (`catalogo_lifeplus_final.html`):** Añadir el botón en el menú de navegación principal (`.nav-btn`), la tarjeta de presentación en la cuadrícula de bienvenida (`.category-preview-card`) y el contenedor final de los productos (`<div id="pets" class="category-section">`).

### FASE 5: Compilación Final (Build)
Se ejecuta en la terminal el script principal:
```bash
python3 crear_buscador_funcional.py
```
Este script coge la base de datos, mapea las imágenes, inserta el modal, activa la función de búsqueda interactiva y emite el archivo final: **`catalogo_lifeplus_buscador_funcional.html`**, listo para ser subido a producción (ej. servidor o GitHub).

---

## 3. Registro Histórico de Implementaciones

### Implementación Línea "PETS" (Abril 2026)
Se integraron 7 productos tras corrección de códigos de catálogo a códigos de tienda:
- **3534**: Lifeplus Pets™ Calm
- **3535**: Lifeplus Pets™ Move
- **3536**: Lifeplus Pets™ Digest
- **3540**: Lifeplus Pets™ Care & Comfort
- **5390**: Lifeplus Pets™ Peanut Butter Biscuits
- **3545**: Lifeplus Pets™ Ahiflower® Oil
- **4164**: Lifeplus Pets™ Mobile App (Sin imagen oficial de producto, requiere validación manual de banner)

### Implementación Packs Nutricionales (Mayo 2026)
Se escrapearon los 33 productos de la búsqueda "pack" en la tienda LifePlus (3 páginas, 12 por página). De ellos, 30 son packs nutricionales (3 eran promocionales: Member estándar, Mochila, Member premium). Se actualizaron precios reales (normal + ASAP) y se añadieron 24 tarjetas HTML nuevas (6 ya existían).

**URL de scraping:** `https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products?search=pack`

**Flujo utilizado:**
1. Navegación con Playwright MCP de las 3 páginas de resultados
2. Extracción de código, nombre, precio normal, precio ASAP y slug
3. Actualización de `crear_buscador_funcional.py` (sección `packs`: 6 → 30 entradas)
4. Eliminación de 59 stubs duplicados de la sección `nuevos`
5. Inserción de 24 tarjetas HTML en `catalogo_lifeplus_final.html`
6. Regeneración: `python3 crear_buscador_funcional.py` → copia a `index.html`

**30 Packs con precios reales:**

| Código | Nombre | Precio | Precio ASAP | Formato |
|--------|--------|--------|-------------|---------|
| 3502 | Maintain & Protect 50 | €123.00 | €111.75 | Pack recomendado |
| 3503 | Maintain & Protect 50 Gold | €168.50 | €155.00 | Pack premium |
| 3504 | Maintain & Protect 100 | €153.75 | €140.50 | Pack recomendado |
| 3505 | Maintain & Protect 100 Gold | €199.00 | €183.75 | Pack premium |
| 3506 | Maintain & Protect 100 Gold Light | €187.50 | €173.50 | Pack premium ligero |
| 3507 | Maintain, Protect & Satisfy - Chocolate | €237.00 | €218.25 | Pack completo |
| 3508 | Maintain, Protect & Satisfy Gold - Chocolate | €282.50 | €261.50 | Pack premium completo |
| 3509 | Maintain, Protect & Satisfy - Vainilla | €237.00 | €218.25 | Pack completo |
| 3510 | Maintain, Protect & Satisfy Gold - Vainilla | €282.50 | €261.50 | Pack premium completo |
| 3512 | Maintain, Protect & Satisfy Gold - Vainilla s/edulcorante | €282.50 | €261.50 | Pack premium completo |
| 3513 | Everyday Wellbeing | €100.25 | €95.00 | Pack esencial |
| 3514 | Everyday Wellbeing sin yodo | €102.25 | €97.00 | Pack esencial |
| 3515 | Everyday Wellbeing Gold | €145.50 | €138.25 | Pack premium |
| 3516 | Everyday Wellbeing Gold sin yodo | €147.75 | €140.00 | Pack premium |
| 3517 | Everyday Wellbeing Plus | €170.25 | €158.75 | Pack avanzado |
| 3518 | Everyday Wellbeing Plus Gold | €215.75 | €202.00 | Pack avanzado premium |
| 3520 | MR Pack - Chocolate | €395.50 | €366.75 | Pack reemplazo de comida |
| 3521 | MR Pack - Vainilla | €395.50 | €366.75 | Pack reemplazo de comida |
| 3522 | MR Pack - Vainilla s/edulcorante | €395.50 | €366.75 | Pack reemplazo de comida |
| 3523 | MR Pack - Chocolate vegano | €404.75 | €376.75 | Pack reemplazo de comida vegano |
| 3490 | MR Light Pack - Chocolate vegano | €393.00 | €366.25 | Pack ligero vegano |
| 3499 | Daily Protein Pack - Chocolate | €165.00 | €150.00 | Pack proteico |
| 3500 | Daily Protein Pack - Vainilla | €165.00 | €150.00 | Pack proteico |
| 3501 | Daily Protein Pack - Vainilla s/edulcorante | €165.00 | €150.00 | Pack proteico |
| 3519 | Sport Pack - Cítricos (Bote) | €238.00 | €226.00 | Pack deportivo |
| 4168 | Sport Pack Sachet Berry 30 ct | €282.25 | €268.50 | Pack deportivo |
| 4169 | Sport Pack Sachet Citrus 30 ct | €282.25 | €268.50 | Pack deportivo |
| 3492 | Winter Boost Pack | €101.00 | €96.25 | Pack inmunidad |
| 3493 | Winter Boost Pack Ultra | €207.50 | €197.50 | Pack inmunidad premium |
| 3491 | Women's Special | €149.50 | €142.00 | Pack mujer |

**Productos NO nutricionales excluidos:**
- 2722: Member paquete estándar (€240.00) — promocional
- 2465: Mochila (€35.00) — promocional
- 2726: Member paquete prémium (€580.00) — promocional

---

## 4. Despliegue a Producción
El flujo de despliegue es simple:
1. Ejecutar `python3 crear_buscador_funcional.py` para regenerar el HTML final
2. Copiar el resultado a `index.html`
3. **Solo se sube `index.html` al servidor** — es el único archivo que se sirve en producción
4. Todo está embebido: HTML, CSS, JavaScript, datos de productos

```bash
python3 crear_buscador_funcional.py
cp catalogo_lifeplus_buscador_funcional.html index.html
# Subir solo index.html al servidor
```

Repositorio GitHub: `https://github.com/peterestelaweb/lifeplusproductoswindsurf-.git`

---

## 5. Notas para el Mantenimiento
- Siempre verificar los enlaces web generados para asegurar que redirigen al producto exacto en lugar de a la página de búsqueda general.
- En caso de fallos con las imágenes de LifePlus, el HTML incluye un script `onerror` en las etiquetas `<img>` para cargar un bloque SVG gris como "fallback" visual, impidiendo que el diseño se rompa.
- **Problema conocido**: Existen DOS secciones con `id="packs"` en el HTML (línea ~2832 y línea ~4474). La segunda es "Packs de Recomendación". Si se añaden más packs, verificar que se insertan en la sección correcta.
- **Capas duales de datos**: El catálogo tiene DOS capas independientes: (1) tarjetas HTML estáticas en `catalogo_lifeplus_final.html` para visualización, (2) arrays JS en `crear_buscador_funcional.py` para el buscador modal. Ambas deben actualizarse por separado.
