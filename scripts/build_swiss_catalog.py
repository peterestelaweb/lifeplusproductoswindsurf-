#!/usr/bin/env python3
"""Build the curated Swiss catalogue from Lifeplus' current CH product feed."""

from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://www.lifeplus.com/SHX4C7/ch/de/web-page/products?tags=view_all"

CONFIRMED_CODES = """
5044 5403 5404 4145 4146 5401 5402 4149 4150 4158 5405 5406 4148 4147
5521 5522 5011 5006 5010 5591 4443 4008 5003 5792 5028 5004 5008 5032
5047 5500 5096 5509 4463 5000 5388 5872 5012 5009 5495 5496 1601 4098
1021 2747 2748 5038 5534 5708 5789 5822 5281 5282 5283 5284 5285 5286
5287 5288 5289 5290 4669 4851 5036 4634 4133 4132 4131 4134 5823 4130
4129 4144 4173 4174 5707 5345 5829 5830 5828
5894 5895 5390 5887 5888 5889
""".split()

# The approved plan explicitly classifies these as telephone orders, even if a
# product can occur in the visible product payload during a catalogue refresh.
PHONE_OVERRIDES = {"5828", "5830"}

PENDING_WITHOUT_CODE = [
    "ParaCleanse",
    "Phase‘olean Forte",
    "Proanthenols 200 SV",
    "Prostate Formula",
    "SlenderLean",
    "Smart Bar Chocolate Supreme",
    "Triple Protein Shake Chocolate sin edulcorante",
    "Triple Protein Shake Vainilla sin edulcorante",
]

ALIASES = {"5504": "5823"}

LOCAL_IMAGE_ALIASES = {
    "5011":"6104", "5006":"9600", "5028":"6193", "5003":"6132", "5004":"6122",
    "5008":"6111", "5012":"6141", "5009":"3428", "5036":"6124",
}

REMOTE_IMAGE_ALIASES = {"5281":"5283", "5289":"5290", "5282":"5284", "5285":"5287", "5286":"5288"}


def extract_array(source: str, variable: str) -> list[dict]:
    marker = f"var {variable} = "
    start = source.index(marker) + len(marker)
    return json.JSONDecoder().raw_decode(source[start:])[0]


def category(name: str) -> str:
    value = name.lower()
    if "lifeplus pets" in value:
        return "Lifeplus Pets"
    if "forever young" in value:
        return "Forever Young"
    if value.startswith("be "):
        return "Be"
    if value.startswith("mr ") or "pack" in value:
        return "Packs"
    if "solis" in value:
        return "Solis"
    if any(word in value for word in ("lotion", "vitaminbox", "crème", "cream", "shampoo", "conditioner", "serum")):
        return "Cuidado y accesorios"
    return "Nutrición y bienestar"


def clean_name(row: dict) -> str:
    return (row.get("translated_product_name") or row.get("description") or "Producto Lifeplus").strip()


def money(value: str) -> str:
    return f"{float(value):.2f}"


def main() -> None:
    request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "Mozilla/5.0"})
    source = urllib.request.urlopen(request, timeout=45).read().decode("utf-8")
    direct_rows = extract_array(source, "productSet")
    phone_rows = extract_array(source, "nmp")
    direct = {str(row.get("item_id")): row for row in direct_rows if row.get("item_id")}
    phone = {str(row.get("ShortProductID")): row for row in phone_rows if row.get("ShortProductID")}

    products = []
    missing = []
    for code in CONFIRMED_CODES:
        row = direct.get(code) or phone.get(code)
        if not row:
            missing.append(code)
            continue
        is_direct = code in direct and code not in PHONE_OVERRIDES
        name = clean_name(row)
        image_code = REMOTE_IMAGE_ALIASES.get(code, code)
        image = (f"assets/products/prodpic_{code}_1.jpg" if code in LOCAL_IMAGE_ALIASES
                 else f"https://www.lifeplus.com/images/products/prodpic_{image_code}_1.jpg")
        products.append({
            "article": code,
            "name": name,
            "category": category(name),
            "price_chf": money(row.get("price") or row.get("Price")),
            "ip": money(row.get("ip") or row.get("IP")),
            "purchase": "direct" if is_direct else "phone",
            "url": f"https://www.lifeplus.com/SHX4C7/ch/de/product-details/{code}" if is_direct else None,
            "image": image,
            "image_fallback": "https://www.lifeplus.com/images/product_placeholder.png",
        })

    products.sort(key=lambda item: (item["category"], item["name"].casefold()))
    payload = {
        "shop_id": "SHX4C7",
        "phone_display": "0800 321 026",
        "phone_href": "tel:0800321026",
        "source": SOURCE_URL,
        "products": products,
        "aliases": ALIASES,
        "pending_without_code": PENDING_WITHOUT_CODE,
        "missing_confirmed_codes": missing,
    }
    data_dir = ROOT / "data"
    data_dir.mkdir(exist_ok=True)
    rendered = json.dumps(payload, ensure_ascii=False, indent=2)
    (data_dir / "catalogo-suiza.json").write_text(rendered + "\n", encoding="utf-8")
    (data_dir / "catalogo-suiza.js").write_text(f"window.SWISS_CATALOG = {rendered};\n", encoding="utf-8")
    print(f"Generated {len(products)} products; missing confirmed codes: {missing}")


if __name__ == "__main__":
    main()
