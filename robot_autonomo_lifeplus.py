#!/usr/bin/env python3
"""
Robot Autónomo LifePlus — Detección de Novedades

Escanea la tienda LifePlus España, compara con la base de datos local,
y genera un informe de productos nuevos.

Uso:
    python3 robot_autonomo_lifeplus.py              # Detectar novedades
    python3 robot_autonomo_lifeplus.py --packs       # Solo packs
    python3 robot_autonomo_lifeplus.py --precios     # Detectar + obtener precios reales (lento)
"""

import re
import json
import sys
import time
from playwright.sync_api import sync_playwright


# ─── CONFIG ───────────────────────────────────────────────────────────────────
TIENDA_BASE = "https://ww1.lifeplus.com/SHVCB5/M/es/es/web-page/products"
AFILIADO = "SHVCB5"
PAIS = "es/es"
HEADLESS = True

EXCLUIDOS = {"2722", "2465", "2726"}


def obtener_codigos_locales():
    codigos = set()
    try:
        import products_data
        for categoria, productos in products_data.PRODUCT_DATABASE.items():
            for prod in productos:
                codigos.add(str(prod["code"]))
    except Exception:
        pass

    try:
        with open("crear_buscador_funcional.py", "r", encoding="utf-8") as f:
            contenido = f.read()
        matches = re.findall(r'"code":\s*"(\d+)"', contenido)
        codigos.update(matches)
    except Exception:
        pass

    return codigos


def scrapear_tienda(busqueda=None, obtener_precios=False):
    """Scrapea la tienda con paginación. Devuelve lista de productos."""
    productos = {}
    url = f"{TIENDA_BASE}?search={busqueda}" if busqueda else f"{TIENDA_BASE}?tags=view_all"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()

        pagina = 1
        while True:
            page_url = url if pagina == 1 else f"{url}&page={pagina}"
            print(f"  📄 Página {pagina}...", flush=True)

            page.goto(page_url, wait_until="domcontentloaded")
            page.wait_for_timeout(6000)

            enlaces = page.locator("a[href*='/product-details/']").all()
            nuevos_en_pagina = 0

            for enlace in enlaces:
                href = enlace.get_attribute("href") or ""
                match = re.search(r'/product-details/(\w+)/([^"?]+)', href)
                if not match:
                    continue

                codigo = match.group(1)
                slug = match.group(2).rstrip("/")

                if codigo in EXCLUIDOS or codigo in productos:
                    continue

                nombre = ""
                try:
                    nombre = enlace.text_content().strip()
                    if not nombre or len(nombre) < 3:
                        parent = enlace.locator("xpath=..").first
                        nombre = parent.text_content().strip().split("\n")[0]
                except:
                    pass
                if not nombre:
                    nombre = f"Producto {codigo}"

                productos[codigo] = {
                    "code": codigo,
                    "name": nombre,
                    "price": "€0.00",
                    "price_asap": "€0.00",
                    "slug": slug
                }
                nuevos_en_pagina += 1

            print(f"     → {nuevos_en_pagina} productos nuevos", flush=True)

            if nuevos_en_pagina == 0:
                break

            pagina += 1
            if pagina > 20:
                break

        # Fase 2: precios reales (opcional, lento)
        if obtener_precios:
            sin_precio = [p for p in productos.values() if p["price"] == "€0.00"]
            if sin_precio:
                print(f"\n  💰 Obteniendo precios para {len(sin_precio)} productos...", flush=True)
                for i, prod in enumerate(sin_precio):
                    try:
                        detail_url = f"https://ww1.lifeplus.com/{AFILIADO}/M/{PAIS}/product-details/{prod['code']}/{prod['slug']}"
                        page.goto(detail_url, wait_until="domcontentloaded")
                        page.wait_for_timeout(2000)

                        html = page.content()

                        # Nombre
                        h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
                        if h1_match:
                            nombre_real = h1_match.group(1).strip()
                            if len(nombre_real) > 3:
                                prod["name"] = nombre_real

                        # Precios
                        precios = re.findall(r'€([\d]+[,.]?\d*)', html)
                        precios_float = [float(p.replace(',', '.')) for p in precios if float(p.replace(',', '.')) >= 5.0]
                        precios_float = sorted(set(precios_float))

                        if len(precios_float) >= 2:
                            prod["price"] = f"€{precios_float[-2]:.2f}"
                            prod["price_asap"] = f"€{precios_float[-1]:.2f}"
                        elif len(precios_float) == 1:
                            prod["price"] = f"€{precios_float[0]:.2f}"

                        print(f"     [{i+1}/{len(sin_precio)}] {prod['code']}: {prod['name'][:40]} — {prod['price']}", flush=True)
                    except Exception as e:
                        print(f"     ⚠️ Error {prod['code']}: {e}", flush=True)

        browser.close()

    return list(productos.values())


def main():
    modo_packs = "--packs" in sys.argv
    modo_precios = "--precios" in sys.argv

    print("🤖 ROBOT AUTÓNOMO LIFEPLUS", flush=True)
    print("=" * 60, flush=True)

    print("\n📂 Cargando base de datos local...", flush=True)
    codigos_locales = obtener_codigos_locales()
    print(f"  → {len(codigos_locales)} productos locales", flush=True)

    if modo_packs:
        print("\n🔍 Modo PACKS...", flush=True)
        productos_web = scrapear_tienda(busqueda="pack", obtener_precios=modo_precios)
    else:
        print("\n🔍 Modo COMPLETO...", flush=True)
        productos_web = scrapear_tienda(obtener_precios=modo_precios)

    codigos_web = {p["code"] for p in productos_web}
    nuevos = [p for p in productos_web if p["code"] not in codigos_locales]
    existentes = [p for p in productos_web if p["code"] in codigos_locales]

    # Informe
    print("\n" + "=" * 60, flush=True)
    print("  📊 INFORME", flush=True)
    print("=" * 60, flush=True)
    print(f"  Total en tienda: {len(productos_web)}", flush=True)
    print(f"  Ya existentes:   {len(existentes)}", flush=True)
    print(f"  Nuevos:          {len(nuevos)}", flush=True)

    if nuevos:
        print(f"\n  🟢 PRODUCTOS NUEVOS:", flush=True)
        for p in nuevos:
            print(f"  + [{p['code']}] {p['name']}", flush=True)
    else:
        print("\n  ✅ Todo al día. Sin novedades.", flush=True)

    # Guardar JSON
    informe = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_tienda": len(productos_web),
        "nuevos": len(nuevos),
        "productos_nuevos": nuevos,
        "productos_existentes": existentes
    }
    filename = f"informe_robot_{time.strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(informe, f, ensure_ascii=False, indent=2)

    print(f"\n  📁 Informe: {filename}", flush=True)
    print("=" * 60 + "\n", flush=True)

    return nuevos


if __name__ == "__main__":
    main()
