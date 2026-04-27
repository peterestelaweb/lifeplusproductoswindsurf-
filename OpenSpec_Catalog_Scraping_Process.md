# OpenSpec: Flujo de Trabajo para Incorporar Nuevos Productos LifePlus

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

## 4. Notas para el Mantenimiento
- Siempre verificar los enlaces web generados para asegurar que redirigen al producto exacto en lugar de a la página de búsqueda general.
- En caso de fallos con las imágenes de LifePlus, el HTML incluye un script `onerror` en las etiquetas `<img>` para cargar un bloque SVG gris como "fallback" visual, impidiendo que el diseño se rompa.
