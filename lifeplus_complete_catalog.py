#!/usr/bin/env python3
"""
LifePlus Complete Catalog Generator
Full catalog with all 118 products from the master file
"""

import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white, gray
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

# LifePlus Brand Colors
LIFEPLUS_BLUE = HexColor('#0066CC')
LIFEPLUS_GREEN = HexColor('#00A86B')
LIFEPLUS_ORANGE = HexColor('#FF6B35')
LIFEPLUS_GRAY = HexColor('#F5F5F5')
LIFEPLUS_DARK = HexColor('#333333')
LIFEPLUS_LIGHT_BLUE = HexColor('#E6F2FF')

class LifePlusCompleteCatalogGenerator:
    def __init__(self):
        self.base_url = "https://ww1.lifeplus.com/SHVCB5/M/es/es"
        self.styles = self.setup_styles()

    def setup_styles(self):
        """Setup beautiful styles for the catalog"""
        styles = getSampleStyleSheet()

        # Title Styles
        styles.add(ParagraphStyle(
            name='CatalogTitle',
            parent=styles['Title'],
            fontSize=28,
            textColor=LIFEPLUS_BLUE,
            alignment=TA_CENTER,
            spaceAfter=20,
            fontName='Helvetica-Bold'
        ))

        styles.add(ParagraphStyle(
            name='CatalogSubtitle',
            parent=styles['Heading1'],
            fontSize=16,
            textColor=LIFEPLUS_GREEN,
            alignment=TA_CENTER,
            spaceAfter=15,
            fontName='Helvetica'
        ))

        # Category Header
        styles.add(ParagraphStyle(
            name='CategoryHeader',
            parent=styles['Heading2'],
            fontSize=18,
            textColor=white,
            backColor=LIFEPLUS_BLUE,
            alignment=TA_CENTER,
            spaceBefore=25,
            spaceAfter=15,
            borderWidth=2,
            borderColor=LIFEPLUS_BLUE,
            borderPadding=8,
            fontName='Helvetica-Bold'
        ))

        # Product Styles
        styles.add(ParagraphStyle(
            name='ProductName',
            parent=styles['Heading3'],
            fontSize=14,
            textColor=LIFEPLUS_DARK,
            alignment=TA_LEFT,
            spaceBefore=8,
            spaceAfter=4,
            fontName='Helvetica-Bold'
        ))

        styles.add(ParagraphStyle(
            name='ProductInfo',
            parent=styles['Normal'],
            fontSize=11,
            textColor=LIFEPLUS_DARK,
            alignment=TA_LEFT,
            spaceAfter=2
        ))

        styles.add(ParagraphStyle(
            name='ProductPrice',
            parent=styles['Normal'],
            fontSize=14,
            textColor=LIFEPLUS_ORANGE,
            alignment=TA_RIGHT,
            fontName='Helvetica-Bold'
        ))

        return styles

    def create_header_footer(self, canvas, doc):
        """Create beautiful header and footer"""
        canvas.saveState()

        # Header
        canvas.setFont('Helvetica-Bold', 14)
        canvas.setFillColor(LIFEPLUS_BLUE)
        canvas.drawString(cm, A4[1] - 2*cm, "LIFEPLUS CATÁLOGO COMPLETO")
        canvas.setFont('Helvetica', 10)
        canvas.drawString(cm, A4[1] - 2.4*cm, "118 Productos Premium de Bienestar")

        canvas.setStrokeColor(LIFEPLUS_BLUE)
        canvas.setLineWidth(2)
        canvas.line(cm, A4[1] - 2.6*cm, A4[0] - cm, A4[1] - 2.6*cm)

        # Footer
        canvas.setFont('Helvetica-Bold', 12)
        canvas.setFillColor(LIFEPLUS_ORANGE)
        canvas.drawCentredString(A4[0]/2, 2*cm, f"Página {doc.page}")

        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(LIFEPLUS_DARK)
        canvas.drawCentredString(A4[0]/2, 1.2*cm, f"© 2025 LifePlus - Tu Tienda: {self.base_url}")

        canvas.setStrokeColor(LIFEPLUS_GRAY)
        canvas.setLineWidth(1)
        canvas.line(cm, 2.5*cm, A4[0] - cm, 2.5*cm)

        canvas.restoreState()

    def parse_product_list(self, markdown_text):
        """Parse product list from markdown file"""
        products = []
        current_category = None

        lines = markdown_text.split('\n')

        for line in lines:
            line = line.strip()

            # Detect category headers
            if line.startswith('### ') and ('PRODUCTOS' in line or 'PROTEÍNAS' in line or 'NUTRICIÓN' in line or 'SUPERFOODS' in line or 'CUIDADO' in line or 'ACCESORIOS' in line or 'SISTEMAS' in line or 'PACKS' in line):
                current_category = line.replace('### ', '').replace('(', '').replace(')', '')
                continue

            # Parse product lines
            match = re.match(r'(\d+)\.\s*\*\*(\d+)\*\*\s*(.*?)\s*-\s*(.*?)\s*-\s*€([\d,\.]+)', line)
            if match:
                num, code, name, format_part, price = match.groups()
                price = price.replace(',', '.')

                products.append({
                    'number': int(num),
                    'code': code,
                    'name': name.strip(),
                    'format': format_part.strip(),
                    'price': float(price),
                    'category': current_category or 'Sin Categoría'
                })

        return products

    def create_spectacular_cover(self):
        """Create an amazing cover page"""
        story = []

        story.append(Spacer(1, 2*cm))
        story.append(Paragraph("LIFEPLUS", self.styles['CatalogTitle']))
        story.append(Paragraph("CATÁLOGO COMPLETO", self.styles['CatalogTitle']))

        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph("🌟 La Colección Completa de Productos Premium 🌟", self.styles['CatalogSubtitle']))
        story.append(Paragraph("118 Productos de Bienestar de Alta Calidad", self.styles['CatalogSubtitle']))

        story.append(Spacer(1, 2*cm))

        # Summary table
        summary_data = [
            ['📊 ESTADÍSTICAS COMPLETAS', ''],
            ['Total de Productos', '118 Productos Premium'],
            ['Categorías', '9 Líneas Especializadas'],
            ['Rango de Precios', '€4.00 - €765.25'],
            ['Calidad', '✅ Certificada Internacional'],
            ['Disponibilidad', '🚀 Inmediata'],
            ['Tu Tienda Personal', '🛍️ Enlace Directo']
        ]

        summary_table = Table(summary_data, colWidths=[6*cm, 6*cm])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), LIFEPLUS_BLUE),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 2, LIFEPLUS_BLUE),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIFEPLUS_LIGHT_BLUE])
        ]))

        story.append(summary_table)
        story.append(PageBreak())

        return story

    def create_table_of_contents(self, products):
        """Create comprehensive table of contents"""
        story = []
        story.append(Paragraph("ÍNDICE COMPLETO", self.styles['CatalogTitle']))
        story.append(Spacer(1, 1*cm))

        # Count products by category
        category_counts = {}
        for product in products:
            cat = product['category']
            category_counts[cat] = category_counts.get(cat, 0) + 1

        # TOC table
        toc_data = [["CATEGORÍA", "PRODUCTOS", "CÓDIGO"]]

        # Add categories
        sorted_categories = sorted(category_counts.items())
        for i, (category, count) in enumerate(sorted_categories):
            toc_data.append([
                category,
                f"{count} productos",
                f"Ver página {i + 4}"
            ])

        toc_table = Table(toc_data, colWidths=[10*cm, 3*cm, 3*cm])
        toc_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), LIFEPLUS_BLUE),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('GRID', (0, 0), (-1, -1), 2, LIFEPLUS_BLUE),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIFEPLUS_LIGHT_BLUE])
        ]))

        story.append(toc_table)
        story.append(PageBreak())

        return story

    def create_product_list_by_category(self, products):
        """Create beautiful product listings by category"""
        story = []

        # Group products by category
        category_groups = {}
        for product in products:
            cat = product['category']
            if cat not in category_groups:
                category_groups[cat] = []
            category_groups[cat].append(product)

        # Sort categories alphabetically
        sorted_categories = sorted(category_groups.items())

        for category, category_products in sorted_categories:
            # Category header
            story.append(Paragraph(f"🌟 {category} 🌟", self.styles['CategoryHeader']))
            story.append(Paragraph(f"<center><i>{len(category_products)} productos disponibles</i></center>", self.styles['CatalogSubtitle']))

            # Products table for this category
            product_data = [["#", "CÓDIGO", "PRODUCTO", "FORMATO", "PRECIO"]]

            for product in category_products:
                product_url = f"{self.base_url}/product-details/{product['code']}"
                product_link = f'<a href="{product_url}" color="blue">{product["name"]}</a>'

                product_data.append([
                    str(product['number']),
                    product['code'],
                    product['name'],
                    product['format'],
                    f"€{product['price']:.2f}"
                ])

            product_table = Table(product_data, colWidths=[1*cm, 2*cm, 7*cm, 4*cm, 3*cm])
            product_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), LIFEPLUS_GREEN),
                ('TEXTCOLOR', (0, 0), (-1, 0), white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('ALIGN', (2, 0), (2, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('GRID', (0, 0), (-1, -1), 1, LIFEPLUS_GRAY),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIFEPLUS_LIGHT_BLUE])
            ]))

            story.append(product_table)
            story.append(Spacer(1, 1*cm))

            # Add category summary
            category_value = sum(p['price'] for p in category_products)
            avg_price = category_value / len(category_products)

            summary_text = f"""
            <center>
            <font size="10" color="#666">
            Valor total de la categoría: €{category_value:.2f} |
            Precio promedio: €{avg_price:.2f} |
            <a href="{self.base_url}" color="blue">Ver todos en tienda →</a>
            </font>
            </center>
            """
            story.append(Paragraph(summary_text, self.styles['ProductInfo']))
            story.append(PageBreak())

        return story

    def generate_complete_catalog(self, markdown_file="Lifeplus productos Final final final.md",
                                 output_file="LifePlus_Catalogo_Completo.pdf"):
        """Generate the complete catalog"""
        print("🚀 Generando Catálogo Completo LifePlus...")

        # Read and parse the markdown file
        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()

            products = self.parse_product_list(markdown_content)
            print(f"✅ Parseados {len(products)} productos del archivo")

        except Exception as e:
            print(f"❌ Error leyendo archivo: {e}")
            return None

        # Create document
        doc = SimpleDocTemplate(
            output_file,
            pagesize=A4,
            rightMargin=1.5*cm,
            leftMargin=1.5*cm,
            topMargin=2.5*cm,
            bottomMargin=3*cm
        )

        # Build story
        story = []

        # Add cover
        story.extend(self.create_spectacular_cover())

        # Add table of contents
        story.extend(self.create_table_of_contents(products))

        # Add product listings
        story.extend(self.create_product_list_by_category(products))

        # Build PDF
        doc.build(story, onFirstPage=self.create_header_footer, onLaterPages=self.create_header_footer)

        print(f"✅ Catálogo completo creado: {output_file}")
        print(f"📊 {len(products)} productos procesados")
        print("🎨 Diseño premium completado!")
        print("📄 Listo para compartir!")

        return output_file

def main():
    """Main function"""
    generator = LifePlusCompleteCatalogGenerator()
    return generator.generate_complete_catalog()

if __name__ == "__main__":
    main()