import re
import os

# Data updates
pets_data = [
    {"old": "6687", "new": "3534", "name": "Lifeplus Pets™ Calm", "url": "https://ww1.lifeplus.com/SHVCB5/M/es/es/product-details/3534/lifeplus-pets%AE-calm"},
    {"old": "6688", "new": "3535", "name": "Lifeplus Pets™ Move", "url": "https://ww1.lifeplus.com/SHVCB5/M/es/es/product-details/3535/lifeplus-pets%AE-move"},
    {"old": "6689", "new": "3536", "name": "Lifeplus Pets™ Digest", "url": "https://ww1.lifeplus.com/SHVCB5/M/es/es/product-details/3536/lifeplus-pets%AE-digest"},
    {"old": "6697", "new": "3540", "name": "Lifeplus Pets™ Care & Comfort", "url": "https://ww1.lifeplus.com/SHVCB5/M/es/es/product-details/3540/lifeplus-pets%AE-care-%26-comfort"},
    {"old": "6692", "new": "5390", "name": "Lifeplus Pets™ Peanut Butter Biscuits", "url": "https://ww1.lifeplus.com/SHVCB5/M/es/es/product-details/5390/lifeplus-pets%AE-peanut-butter-biscuits"},
    {"old": "6698", "new": "3545", "name": "Lifeplus Pets™ Ahiflower® Oil", "url": "https://ww1.lifeplus.com/SHVCB5/M/es/es/product-details/3545/lifeplus-pets%AE-ahiflower%AE-oil"},
    {"old": "PETS-APP", "new": "4164", "name": "Lifeplus Pets™ Mobile App", "url": "https://ww1.lifeplus.com/SHVCB5/M/es/es/product-details/4164/lifeplus-pets-app"}
]

# 1. Fix products_data.py
if os.path.exists('products_data.py'):
    with open('products_data.py', 'r', encoding='utf-8') as f:
        pd = f.read()
    for item in pets_data:
        pd = pd.replace(f'"{item["old"]}"', f'"{item["new"]}"')
    with open('products_data.py', 'w', encoding='utf-8') as f:
        f.write(pd)
    print("products_data.py updated.")

# 2. Fix crear_buscador_funcional.py
if os.path.exists('crear_buscador_funcional.py'):
    with open('crear_buscador_funcional.py', 'r', encoding='utf-8') as f:
        cb = f.read()
    for item in pets_data:
        cb = cb.replace(f'"code": "{item["old"]}"', f'"code": "{item["new"]}"')
    with open('crear_buscador_funcional.py', 'w', encoding='utf-8') as f:
        f.write(cb)
    print("crear_buscador_funcional.py updated.")

# 3. Fix catalogo_lifeplus_final.html
if os.path.exists('catalogo_lifeplus_final.html'):
    with open('catalogo_lifeplus_final.html', 'r', encoding='utf-8') as f:
        ch = f.read()
    
    for item in pets_data:
        # Update code span
        ch = ch.replace(f'<span class="product-code">{item["old"]}</span>', f'<span class="product-code">{item["new"]}</span>')
        # Update image url
        ch = ch.replace(f'prodpic_{item["old"]}_1@2x.jpg', f'prodpic_{item["new"]}_1@2x.jpg')
        
        # Update link
        # The old links were looking like:
        # href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/{item['old']}/...
        
        # We need a regex or simple replace for the entire link tag. 
        # Since I know exactly what I generated earlier:
        
        # Let's use a regex to replace the a href for this specific product name
        pattern = r'<a href="[^"]+" target="_blank" class="product-link">\s*<i class="fas fa-shopping-cart"></i>\s*<span>(Comprar en Tienda|Ver Aplicación)</span>\s*</a>'
        # Wait, that regex doesn't match by product. I need to replace the specific block.
        # It's easier to just replace the whole pets section or find the specific line.
        
        # Actually, let's just do a regex replace for the hrefs by matching the product ID in the old link.
        # But wait, the previous links were like: <a href="https://ww1.lifeplus.com/SHVCB5/S/es/es/product-details/6687/lifeplus-pets-calm"
        if item["old"] == "PETS-APP":
            ch = re.sub(r'<a href="https://ww1\.lifeplus\.com/SHVCB5/S/es/es/product-details/PETS-APP/[^"]*"', 
                        f'<a href="{item["url"]}"', ch)
        else:
            ch = re.sub(rf'<a href="https://ww1\.lifeplus\.com/SHVCB5/S/es/es/product-details/{item["old"]}/[^"]*"', 
                        f'<a href="{item["url"]}"', ch)

    with open('catalogo_lifeplus_final.html', 'w', encoding='utf-8') as f:
        f.write(ch)
    print("catalogo_lifeplus_final.html updated.")

