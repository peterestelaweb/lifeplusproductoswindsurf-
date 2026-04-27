import re
import time
from playwright.sync_api import sync_playwright
import products_data # Tu archivo local

# 1. Obtener los códigos locales
codigos_locales = set()
for categoria, productos in products_data.PRODUCT_DATABASE.items():
    for prod in productos:
        codigos_locales.add(str(prod["code"]))

def run():
    print("🤖 Iniciando Robot de Rastreo LifePlus...")
    print(f"📦 Tienes {len(codigos_locales)} productos registrados localmente.")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        url = "https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products?tags=view_all"
        print(f"🌐 Conectando a {url}...")
        
        # Ir a la página y esperar a que la red esté inactiva (para que React cargue los productos)
        page.goto(url, wait_until="networkidle")
        
        # Esperamos unos segundos extra de cortesía por si hay renders lentos
        time.sleep(5)
        
        print("🔍 Escaneando productos...")
        
        # Buscar todos los enlaces en la página
        enlaces = page.locator("a").all()
        
        productos_web = {}
        
        for enlace in enlaces:
            href = enlace.get_attribute("href")
            # Queremos buscar enlaces que contengan /product-details/CÓDIGO/
            if href and "/product-details/" in href:
                # Extraer el código usando expresiones regulares
                match = re.search(r'/product-details/(\w+)/', href)
                if match:
                    codigo = match.group(1)
                    # Intentar obtener el título del producto
                    # Normalmente está en el texto del enlace o en un elemento hijo
                    titulo = enlace.text_content().strip()
                    # Si el título está vacío, puede que sea un enlace de imagen. Lo guardamos igual.
                    if codigo not in productos_web:
                        productos_web[codigo] = titulo if titulo else f"Producto ID {codigo}"
                        
        browser.close()
        
        # 3. Auditoría Comparativa
        print("\n📊 RESULTADOS DE LA AUDITORÍA:")
        print("="*40)
        
        codigos_web = set(productos_web.keys())
        
        nuevos_productos = codigos_web - codigos_locales
        productos_borrados = codigos_locales - codigos_web
        
        if len(nuevos_productos) == 0 and len(productos_borrados) == 0:
            print("✅ TODO AL DÍA: Tu catálogo está perfectamente sincronizado con LifePlus.")
        else:
            if nuevos_productos:
                print(f"🟢 ¡ATENCIÓN! Se han encontrado {len(nuevos_productos)} PRODUCTOS NUEVOS en la web oficial:")
                for cod in nuevos_productos:
                    print(f"   + [ID: {cod}] {productos_web[cod]}")
                    
            if productos_borrados:
                # Algunas categorías como la App o Packs pueden no salir en la lista principal de productos
                print(f"🔴 AVISO: Tienes {len(productos_borrados)} productos en tu web que NO se han encontrado en la tienda general:")
                for cod in productos_borrados:
                    print(f"   - [ID: {cod}] revisa si está descatalogado o si es un producto especial.")
        
        print("\n🚀 Proceso completado. Revisa OpenSpec_Robot_Scraping_Lifeplus.md para instrucciones.")

if __name__ == "__main__":
    run()
