import re
import json
from playwright.sync_api import sync_playwright
import products_data

codigos_locales = set()
for categoria, productos in products_data.PRODUCT_DATABASE.items():
    for prod in productos:
        codigos_locales.add(str(prod["code"]))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products?tags=view_all", wait_until="networkidle")
    page.wait_for_timeout(5000)
    
    enlaces = page.locator("a").all()
    productos_web = {}
    
    for enlace in enlaces:
        href = enlace.get_attribute("href")
        if href and "/product-details/" in href:
            match = re.search(r'/product-details/(\w+)/', href)
            if match:
                codigo = match.group(1)
                titulo = enlace.text_content().strip()
                if codigo not in productos_web and titulo:
                    productos_web[codigo] = titulo

    browser.close()
    
    codigos_web = set(productos_web.keys())
    nuevos_productos = codigos_web - codigos_locales
    
    nuevos_list = []
    for cod in nuevos_productos:
        nuevos_list.append({
            "code": cod,
            "name": productos_web[cod],
            "price": "€0.00",
            "price_asap": "€0.00",
            "format": "Novedad",
            "description": "Nuevo producto añadido desde el catálogo general",
            "benefits": ["Nuevo"]
        })
        
    with open('nuevos_productos.json', 'w', encoding='utf-8') as f:
        json.dump(nuevos_list, f, ensure_ascii=False, indent=4)
        
    print(f"Extraídos {len(nuevos_list)} productos nuevos a nuevos_productos.json")
