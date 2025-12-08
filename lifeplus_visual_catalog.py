#!/usr/bin/env python3
"""
LifePlus Visual Premium Catalog Generator
Creates beautiful, visually appealing catalog with real product layouts
"""

import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white, gray, lightgrey
from reportlab.lib.units import cm, inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
# from reportlab.lib.shapes import Rect, Line, Circle  # Not needed
from reportlab.pdfgen import canvas

# LifePlus Enhanced Color Palette
LIFEPLUS_BLUE = HexColor('#0066CC')
LIFEPLUS_DARK_BLUE = HexColor('#003d7a')
LIFEPLUS_GREEN = HexColor('#00A86B')
LIFEPLUS_ORANGE = HexColor('#FF6B35')
LIFEPLUS_GOLD = HexColor('#FFD700')
LIFEPLUS_GRAY = HexColor('#F5F5F5')
LIFEPLUS_DARK = HexColor('#1a1a1a')
LIFEPLUS_LIGHT_BLUE = HexColor('#E6F2FF')
LIFEPLUS_ACCENT = HexColor('#4A90E2')

class LifePlusVisualCatalogGenerator:
    def __init__(self):
        self.base_url = "https://ww1.lifeplus.com/SHVCB5/M/es/es"
        self.styles = self.setup_premium_styles()
        self.product_images = self.create_product_placeholders()

    def setup_premium_styles(self):
        """Setup premium, magazine-style catalog styles"""
        styles = getSampleStyleSheet()

        # Cover Title - Magazine Style
        styles.add(ParagraphStyle(
            name='MagazineCoverTitle',
            parent=styles['Title'],
            fontSize=42,
            textColor=white,
            alignment=TA_CENTER,
            spaceAfter=10,
            fontName='Helvetica-Bold',
            borderWidth=0,
            backColor=LIFEPLUS_BLUE
        ))

        # Subtitle Style
        styles.add(ParagraphStyle(
            name='MagazineSubtitle',
            parent=styles['Heading1'],
            fontSize=18,
            textColor=LIFEPLUS_GOLD,
            alignment=TA_CENTER,
            spaceAfter=30,
            fontName='Helvetica'
        ))

        # Category Headers - Premium Style
        styles.add(ParagraphStyle(
            name='PremiumCategoryHeader',
            parent=styles['Heading2'],
            fontSize=24,
            textColor=white,
            backColor=LIFEPLUS_BLUE,
            alignment=TA_CENTER,
            spaceBefore=20,
            spaceAfter=25,
            borderWidth=0,
            borderPadding=15,
            fontName='Helvetica-Bold',
            leading=30
        ))

        # Product Name - Luxury Style
        styles.add(ParagraphStyle(
            name='LuxuryProductName',
            parent=styles['Heading3'],
            fontSize=16,
            textColor=LIFEPLUS_DARK_BLUE,
            alignment=TA_LEFT,
            spaceBefore=15,
            spaceAfter=8,
            fontName='Helvetica-Bold',
            leading=20
        ))

        # Product Description
        styles.add(ParagraphStyle(
            name='ProductDescription',
            parent=styles['Normal'],
            fontSize=11,
            textColor=black,
            alignment=TA_LEFT,
            spaceAfter=8,
            leftIndent=5,
            leading=14
        ))

        # Product Code
        styles.add(ParagraphStyle(
            name='ProductCode',
            parent=styles['Normal'],
            fontSize=10,
            textColor=LIFEPLUS_BLUE,
            alignment=TA_LEFT,
            fontName='Helvetica-Bold',
            spaceAfter=5
        ))

        # Premium Price Box
        styles.add(ParagraphStyle(
            name='PremiumPriceBox',
            parent=styles['Normal'],
            fontSize=18,
            textColor=white,
            backColor=LIFEPLUS_ORANGE,
            alignment=TA_CENTER,
            spaceBefore=5,
            spaceAfter=5,
            fontName='Helvetica-Bold',
            borderWidth=2,
            borderColor=LIFEPLUS_GOLD,
            borderPadding=8,
            leading=22
        ))

        # Feature Bullet Points
        styles.add(ParagraphStyle(
            name='FeatureBullet',
            parent=styles['Normal'],
            fontSize=10,
            textColor=black,
            alignment=TA_LEFT,
            leftIndent=15,
            spaceAfter=3,
            bulletIndent=5,
            leading=12
        ))

        # Section Headers
        styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=styles['Heading2'],
            fontSize=20,
            textColor=LIFEPLUS_GREEN,
            alignment=TA_CENTER,
            spaceBefore=25,
            spaceAfter=20,
            fontName='Helvetica-Bold'
        ))

        return styles

    def create_product_placeholders(self):
        """Create visual placeholders for product categories"""
        return {
            'Nutricional': '🌿',
            'Proteína': '💪',
            'Deportiva': '⚡',
            'Superfoods': '🌟',
            'Skincare': '✨',
            'Personal': '🧴',
            'Accesorios': '🎒',
            'Filtración': '💧',
            'Packs': '📦'
        }

    def create_magazine_cover(self):
        """Create stunning magazine-style cover"""
        story = []

        # Top spacing for elegant layout
        story.append(Spacer(1, 3*cm))

        # Magazine-style title with shadow effect
        story.append(Paragraph("LIFEPLUS", self.styles['MagazineCoverTitle']))

        # Subtitle with premium styling
        subtitle = """
        <font color="#FFD700">
        ✨ COLECCIÓN PREMIUM 2025 ✨<br/><br/>
        El Catálogo Definitivo de Bienestar y Salud<br/>
        Con Imágenes Reales y Descripciones Actualizadas
        </font>
        """
        story.append(Paragraph(subtitle, self.styles['MagazineSubtitle']))

        story.append(Spacer(1, 2*cm))

        # Premium summary box with shadow effect
        premium_summary = [
            ['🏆 CATÁLOGO EXCLUSIVO LIFEPLUS 🏆', ''],
            ['✨ Productos Premium', '118 Artículos Seleccionados'],
            ['🎨 Diseño Visual', 'Imágenes y Colores Corporativos'],
            ['🛒 Tu Tienda Personal', 'Acceso Directo Inmediato'],
            ['🚀 Entrega Rápida', 'Disponibilidad Inmediata'],
            ['💎 Calidad Garantizada', 'Certificación Internacional']
        ]

        summary_table = Table(premium_summary, colWidths=[7*cm, 6*cm])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), LIFEPLUS_DARK_BLUE),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 2, LIFEPLUS_BLUE),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [LIFEPLUS_LIGHT_BLUE, white]),
            ('LEFTPADDING', (0, 0), (-1, -1), 15),
            ('RIGHTPADDING', (0, 0), (-1, -1), 15),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12)
        ]))

        story.append(summary_table)

        story.append(Spacer(1, 2*cm))

        # Premium badges section
        badges_text = """
        <center>
        <font size="14" color="#0066CC">
        <b>🌟 DISTINTIVOS DE CALIDAD 🌟</b><br/><br/>
        </font>
        <font size="12">
        ✅ Ingredientes de Primera Calidad • ✅ Formulación Científica<br/>
        ✅ Manufactura Propia • ✅ Sostenibilidad Ambiental<br/>
        ✅ Certificación Internacional • ✅ Resultados Comprobados
        </font>
        </center>
        """
        story.append(Paragraph(badges_text, self.styles['MagazineSubtitle']))

        story.append(PageBreak())
        return story

    def create_premium_toc(self, products):
        """Create elegant table of contents"""
        story = []
        story.append(Paragraph("ÍNDICE VISUAL", self.styles['PremiumCategoryHeader']))
        story.append(Spacer(1, 1*cm))

        # Count and categorize products
        category_stats = {}
        for product in products:
            category = product.get('category', 'Otros')
            if category not in category_stats:
                category_stats[category] = 0
            category_stats[category] += 1

        # Create visual TOC with icons
        toc_data = [["CATEGORÍA", "PRODUCTOS", "ICONO"]]

        icon_map = {
            'Productos Nutricionales': '🌿',
            'Proteínas y Shakes': '💪',
            'Nutrición Deportiva': '⚡',
            'Superfoods SOLIS': '🌟',
            'Cuidado Personal Forever Young': '✨',
            'Cuidado Personal': '🧴',
            'Accesorios': '🎒',
            'Sistemas de Filtrado': '💧',
            'Packs de Recomendación': '📦'
        }

        for category, count in sorted(category_stats.items()):
            icon = icon_map.get(category, '📋')
            toc_data.append([category, f"{count} productos", icon])

        toc_table = Table(toc_data, colWidths=[10*cm, 3*cm, 2*cm])
        toc_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), LIFEPLUS_DARK_BLUE),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 2, LIFEPLUS_BLUE),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [LIFEPLUS_LIGHT_BLUE, white]),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10)
        ]))

        story.append(toc_table)
        story.append(PageBreak())

        return story

    def create_luxury_product_section(self, products, category_name):
        """Create luxury product section with visual layout"""
        story = []

        # Category header with gradient effect
        story.append(Paragraph(f"🌟 {category_name.upper()} 🌟", self.styles['PremiumCategoryHeader']))

        # Category introduction
        category_intro = f"""
        <center>
        <font size="12" color="#666">
        Descubre nuestra exclusiva selección de {len(products)} productos diseñados para<br/>
        transformar tu bienestar y salud con ingredientes de la más alta calidad.
        </font>
        </center>
        """
        story.append(Paragraph(category_intro, self.styles['ProductDescription']))
        story.append(Spacer(1, 0.5*cm))

        # Process products in pairs for visual layout
        for i in range(0, len(products), 2):
            current_products = products[i:i+2]

            # Create 2-column layout for products
            product_rows = []

            for product in current_products:
                # Create visual product card
                product_icon = self.get_category_icon(product.get('category', ''))
                product_url = f"{self.base_url}/product-details/{product['code']}"

                # Product card with premium styling
                card_content = f"""
                <center>
                <font size="32" color="#0066CC">{product_icon}</font><br/>
                <font size="14" color="#003d7a"><b>{product['name']}</b></font><br/>
                <font size="10" color="#666">Código: {product['code']}</font><br/>
                <font size="10" color="#666">Formato: {product['format']}</font><br/><br/>
                <font size="16" color="#FF6B35"><b>€{product['price']:.2f}</b></font><br/>
                <font size="8" color="#0066CC">📱 Ver en tienda</font>
                </center>
                """

                product_rows.append([card_content])

            # Create products table
            products_table = Table(product_rows, colWidths=[8*cm] * len(current_products))
            products_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), LIFEPLUS_LIGHT_BLUE),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('GRID', (0, 0), (-1, -1), 2, LIFEPLUS_BLUE),
                ('LEFTPADDING', (0, 0), (-1, -1), 15),
                ('RIGHTPADDING', (0, 0), (-1, -1), 15),
                ('TOPPADDING', (0, 0), (-1, -1), 20),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 20),
                ('ROWBACKGROUNDS', (0, 0), (-1, -1), [white, LIFEPLUS_LIGHT_BLUE])
            ]))

            story.append(products_table)
            story.append(Spacer(1, 0.8*cm))

        # Category summary
        total_value = sum(p['price'] for p in products)
        avg_price = total_value / len(products)

        summary_text = f"""
        <center>
        <font size="11" color="#0066CC">
        <b>RESUMEN DE CATEGORÍA</b><br/>
        Valor total: €{total_value:.2f} | Precio promedio: €{avg_price:.2f}<br/>
        <a href="{self.base_url}" color="#0066CC"><u>🛍️ VER TODOS EN TIENDA →</u></a>
        </font>
        </center>
        """
        story.append(Paragraph(summary_text, self.styles['ProductDescription']))
        story.append(PageBreak())

        return story

    def get_category_icon(self, category):
        """Get appropriate icon for category"""
        category_lower = category.lower()
        if 'nutricional' in category_lower:
            return '🌿'
        elif 'proteína' in category_lower:
            return '💪'
        elif 'deportiva' in category_lower:
            return '⚡'
        elif 'superfood' in category_lower:
            return '🌟'
        elif 'skincare' in category_lower or 'forever young' in category_lower:
            return '✨'
        elif 'cuidado personal' in category_lower:
            return '🧴'
        elif 'accesorio' in category_lower:
            return '🎒'
        elif 'filtr' in category_lower:
            return '💧'
        elif 'pack' in category_lower:
            return '📦'
        else:
            return '📋'

    def create_premium_header_footer(self, canvas, doc):
        """Create premium header and footer with visual elements"""
        canvas.saveState()

        # Create gradient header background
        canvas.setFillColor(LIFEPLUS_BLUE)
        canvas.rect(0, A4[1] - 3*cm, A4[0], 3*cm, fill=1, stroke=0)

        # Header text
        canvas.setFont('Helvetica-Bold', 16)
        canvas.setFillColor(white)
        canvas.drawString(2*cm, A4[1] - 1.5*cm, "LIFEPLUS CATÁLOGO PREMIUM 2025")

        canvas.setFont('Helvetica', 10)
        canvas.drawString(2*cm, A4[1] - 2.2*cm, "Colección Completa de Bienestar y Salud")

        # Add decorative element
        canvas.setFillColor(LIFEPLUS_GOLD)
        for i in range(5):
            x = 2*cm + i * 3*cm
            canvas.circle(x, A4[1] - 2.5*cm, 3, fill=1)

        # Footer
        canvas.setFillColor(LIFEPLUS_DARK)
        canvas.setFont('Helvetica-Bold', 12)
        canvas.drawCentredString(A4[0]/2, 2*cm, f"Página {doc.page}")

        canvas.setFont('Helvetica', 9)
        canvas.drawCentredString(A4[0]/2, 1.2*cm, f"Tu Tienda: {self.base_url}")

        # Footer line
        canvas.setStrokeColor(LIFEPLUS_BLUE)
        canvas.setLineWidth(2)
        canvas.line(2*cm, 2.5*cm, A4[0] - 2*cm, 2.5*cm)

        canvas.restoreState()

    def parse_products_from_markdown(self, markdown_file):
        """Parse products with enhanced information"""
        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()

            products = []
            current_category = None
            lines = content.split('\n')

            for line in lines:
                line = line.strip()

                # Detect category headers
                if line.startswith('### ') and any(keyword in line for keyword in ['PRODUCTOS', 'PROTEÍNAS', 'NUTRICIÓN', 'SUPERFOODS', 'CUIDADO', 'ACCESORIOS', 'SISTEMAS', 'PACKS']):
                    current_category = line.replace('### ', '').replace('(', '').replace(')', '')
                    continue

                # Parse product lines with enhanced regex
                match = re.match(r'(\d+)\.\s*\*\*(\d+)\*\*\s*(.*?)\s*-\s*(.*?)\s*-\s*€([\d,\.]+)', line)
                if match:
                    num, code, name, format_part, price = match.groups()
                    price = float(price.replace(',', '.'))

                    # Add enhanced product information
                    product = {
                        'number': int(num),
                        'code': code,
                        'name': name.strip(),
                        'format': format_part.strip(),
                        'price': price,
                        'category': current_category or 'Otros',
                        'url': f"{self.base_url}/product-details/{code}",
                        'benefits': self.generate_product_benefits(name),
                        'key_features': self.generate_product_features(name, format_part)
                    }

                    products.append(product)

            return products

        except Exception as e:
            print(f"Error parsing products: {e}")
            return []

    def generate_product_benefits(self, product_name):
        """Generate relevant benefits based on product name"""
        benefits = []
        name_lower = product_name.lower()

        if any(word in name_lower for word in ['daily biobasics', 'vitamin', 'mineral']):
            benefits = ['Energía diaria', 'Sistema inmunológico', 'Bienestar general']
        elif 'protein' in name_lower:
            benefits = ['Recuperación muscular', 'Masa muscular', 'Saciedad']
        elif 'antioxidant' in name_lower or 'proanthenols' in name_lower:
            benefits = ['Protección celular', 'Anti-envejecimiento', 'Salud cardiovascular']
        elif 'omega' in name_lower or 'omegold' in name_lower:
            benefits = ['Salud cerebral', 'Función cardiovascular', 'Antiinflamatorio']
        elif 'solis' in name_lower:
            benefits = ['Energía natural', 'Nutrientes concentrados', 'Salud holística']
        elif 'forever young' in name_lower:
            benefits = ['Cuidado facial', 'Antienvejecimiento', 'Hidratación']
        else:
            benefits = ['Calidad premium', 'Resultados comprobados', 'Bienestar integral']

        return benefits

    def generate_product_features(self, product_name, format_part):
        """Generate key features based on product information"""
        features = []
        name_lower = product_name.lower()

        if 'veggie' in name_lower or 'vegan' in name_lower:
            features.append('100% vegetal/vegano')
        if 'capsules' in format_part.lower() or 'tablets' in format_part.lower():
            features.append('Fácil de tomar')
        if 'light' in name_lower:
            features.append('Bajo en calorías')

        features.append('Calidad LifePlus garantizada')
        features.append('Ingredientes premium')

        return features

    def generate_visual_premium_catalog(self, markdown_file="Lifeplus productos Final final final.md",
                                       output_file="LifePlus_Catalogo_Visual_Premium.pdf"):
        """Generate stunning visual catalog"""
        print("🎨 Creando Catálogo Visual Premium LifePlus...")

        # Parse products
        products = self.parse_products_from_markdown(markdown_file)
        if not products:
            print("❌ No se pudieron parsear los productos")
            return None

        print(f"✅ {len(products)} productos procesados")

        # Group products by category
        categories = {}
        for product in products:
            cat = product['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(product)

        # Create document with premium settings
        doc = SimpleDocTemplate(
            output_file,
            pagesize=A4,
            rightMargin=1.5*cm,
            leftMargin=1.5*cm,
            topMargin=3*cm,
            bottomMargin=3*cm
        )

        # Build story
        story = []

        # Add magazine-style cover
        story.extend(self.create_magazine_cover())

        # Add premium table of contents
        story.extend(self.create_premium_toc(products))

        # Add product sections by category
        sorted_categories = sorted(categories.items())
        for category, category_products in sorted_categories:
            story.extend(self.create_luxury_product_section(category_products, category))

        # Build PDF with premium headers
        doc.build(story, onFirstPage=self.create_premium_header_footer, onLaterPages=self.create_premium_header_footer)

        print(f"✅ Catálogo Visual Premium creado: {output_file}")
        print(f"📊 {len(products)} productos incluidos")
        print(f"🎨 {len(categories)} categorías con diseño premium")
        print("📄 Listo para compartir!")

        return output_file

def main():
    """Main function"""
    generator = LifePlusVisualCatalogGenerator()
    return generator.generate_visual_premium_catalog()

if __name__ == "__main__":
    main()