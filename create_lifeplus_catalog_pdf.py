#!/usr/bin/env python3
"""
LifePlus Products Catalog PDF Generator
Create beautiful PDF catalog with product information
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.units import cm, inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

# LifePlus Brand Colors
LIFEPLUS_BLUE = HexColor('#0066CC')
LIFEPLUS_GREEN = HexColor('#00A86B')
LIFEPLUS_ORANGE = HexColor('#FF6B35')
LIFEPLUS_GRAY = HexColor('#F5F5F5')
LIFEPLUS_DARK = HexColor('#333333')

class LifePlusPDFGenerator:
    def __init__(self, output_filename="LifePlus_Catalog.pdf"):
        self.output_filename = output_filename
        self.doc = None
        self.story = []
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()

    def setup_custom_styles(self):
        """Setup custom styles for LifePlus branding"""
        # Title Style
        self.styles.add(ParagraphStyle(
            name='LifePlusTitle',
            parent=self.styles['Title'],
            fontSize=28,
            textColor=LIFEPLUS_BLUE,
            alignment=TA_CENTER,
            spaceAfter=20,
            borderWidth=0,
            borderColor=LIFEPLUS_BLUE
        ))

        # Subtitle Style
        self.styles.add(ParagraphStyle(
            name='LifePlusSubtitle',
            parent=self.styles['Heading1'],
            fontSize=18,
            textColor=LIFEPLUS_GREEN,
            alignment=TA_CENTER,
            spaceAfter=15
        ))

        # Category Header
        self.styles.add(ParagraphStyle(
            name='CategoryHeader',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=white,
            backColor=LIFEPLUS_BLUE,
            alignment=TA_CENTER,
            spaceBefore=20,
            spaceAfter=10,
            borderWidth=1,
            borderColor=LIFEPLUS_BLUE,
            borderPadding=5
        ))

        # Product Name
        self.styles.add(ParagraphStyle(
            name='ProductName',
            parent=self.styles['Heading3'],
            fontSize=14,
            textColor=LIFEPLUS_DARK,
            alignment=TA_LEFT,
            spaceBefore=8,
            spaceAfter=4
        ))

        # Product Description
        self.styles.add(ParagraphStyle(
            name='ProductDescription',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=LIFEPLUS_DARK,
            alignment=TA_LEFT,
            spaceAfter=4,
            leftIndent=10
        ))

        # Product Price
        self.styles.add(ParagraphStyle(
            name='ProductPrice',
            parent=self.styles['Normal'],
            fontSize=12,
            textColor=LIFEPLUS_ORANGE,
            alignment=TA_RIGHT,
            spaceBefore=4,
            fontName='Helvetica-Bold'
        ))

    def create_header_footer(self, canvas, doc):
        """Create header and footer for each page"""
        canvas.saveState()

        # Header
        canvas.setFont('Helvetica-Bold', 12)
        canvas.setFillColor(LIFEPLUS_BLUE)
        canvas.drawString(cm, A4[1] - 1.5*cm, "LIFEPLUS PRODUCT CATALOG")
        canvas.line(cm, A4[1] - 1.7*cm, A4[0] - cm, A4[1] - 1.7*cm)

        # Footer
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(LIFEPLUS_DARK)
        canvas.drawCentredString(A4[0]/2, 1.5*cm, f"Page {doc.page}")
        canvas.line(cm, 2*cm, A4[0] - cm, 2*cm)

        canvas.restoreState()

    def add_cover_page(self):
        """Create attractive cover page"""
        self.story.append(Spacer(1, 3*cm))

        # Main Title
        self.story.append(Paragraph("LIFEPLUS", self.styles['LifePlusTitle']))
        self.story.append(Paragraph("PRODUCT CATALOG", self.styles['LifePlusTitle']))

        self.story.append(Spacer(1, 1*cm))
        self.story.append(Paragraph("Complete Guide to Premium Health & Wellness Products", self.styles['LifePlusSubtitle']))

        self.story.append(Spacer(1, 2*cm))

        # Summary Box
        summary_data = [
            ['Catalog Summary', ''],
            ['Total Products', '118 Premium Items'],
            ['Main Categories', '9 Product Lines'],
            ['Price Range', '€4.00 - €765.25'],
            ['Quality Standards', 'Certified Organic & Professional Grade']
        ]

        summary_table = Table(summary_data, colWidths=[5*cm, 6*cm])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), LIFEPLUS_GRAY),
            ('TEXTCOLOR', (0, 0), (-1, -1), black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [white, LIFEPLUS_GRAY])
        ]))

        self.story.append(summary_table)
        self.story.append(PageBreak())

    def add_table_of_contents(self):
        """Create table of contents"""
        self.story.append(Paragraph("TABLE OF CONTENTS", self.styles['LifePlusTitle']))
        self.story.append(Spacer(1, 0.5*cm))

        categories = [
            ("Nutritional Supplements", 66),
            ("Proteins & Shakes", 10),
            ("Sports Nutrition", 15),
            ("Superfoods SOLIS", 4),
            ("Forever Young Skincare", 7),
            ("Personal Care", 9),
            ("Accessories", 3),
            ("Water Filtration Systems", 6),
            ("Recommendation Packs", 5)
        ]

        toc_data = [["Category", "Number of Products", "Page"]]
        toc_data.extend([
            [cat, f"{count} products", f"Page {i+3}"] for i, (cat, count) in enumerate(categories)
        ])

        toc_table = Table(toc_data, colWidths=[10*cm, 3*cm, 3*cm])
        toc_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), LIFEPLUS_BLUE),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('GRID', (0, 0), (-1, -1), 1, LIFEPLUS_BLUE),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIFEPLUS_GRAY])
        ]))

        self.story.append(toc_table)
        self.story.append(PageBreak())

    def add_product_section(self, title, products):
        """Add a section for a product category"""
        # Category Header
        self.story.append(Paragraph(title.upper(), self.styles['CategoryHeader']))

        for product in products:
            # Product Card
            product_data = []

            # Product Name and Code
            name_text = f"<b>{product['name']}</b><br/>Code: {product['code']}"
            product_data.append([name_text, f"€{product['price']:.2f}"])

            # Product Description
            if 'description' in product:
                desc_text = product['description']
            else:
                desc_text = f"{product['format']}"

            product_data.append([desc_text, ""])

            # Product Table
            product_table = Table(product_data, colWidths=[12*cm, 4*cm])
            product_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, 0), LIFEPLUS_GRAY),
                ('TEXTCOLOR', (0, 0), (-1, -1), black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
                ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (0, 0), 12),
                ('FONTSIZE', (1, 0), (1, -1), 12),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
                ('GRID', (0, 0), (-1, -1), 1, LIFEPLUS_GRAY),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 10),
                ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8)
            ]))

            self.story.append(product_table)
            self.story.append(Spacer(1, 0.3*cm))

        self.story.append(Spacer(1, 0.5*cm))

    def generate_pdf(self):
        """Generate the complete PDF catalog"""
        # Create document with custom template
        doc = SimpleDocTemplate(
            self.output_filename,
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2*cm,
            bottomMargin=3*cm
        )

        # Add cover page
        self.add_cover_page()

        # Add table of contents
        self.add_table_of_contents()

        # Product data from the consolidated list
        nutritional_products = [
            {
                'code': '3401',
                'name': 'Daily BioBasics®',
                'format': '786g',
                'price': 86.00,
                'description': 'Premium nutritional foundation with 115+ ingredients including fruits, vegetables, and herbs'
            },
            {
                'code': '3400',
                'name': 'Proanthenols® 100',
                'format': '60 tablets',
                'price': 75.75,
                'description': 'High-potency antioxidant formula with Real OPC from grape seed and pine bark extract'
            },
            {
                'code': '3402',
                'name': 'OmeGold®',
                'format': '60 capsules',
                'price': 47.75,
                'description': 'Premium omega-3 EPA/DHA formula for cardiovascular and brain health'
            },
            {
                'code': '3405',
                'name': 'TVM-Plus',
                'format': '180 tablets',
                'price': 29.75,
                'description': 'Complete multivitamin and multimineral formula for busy lifestyles'
            },
            {
                'code': '3459',
                'name': 'Xtra Antioxidants',
                'format': '120 tablets',
                'price': 67.75,
                'description': 'Comprehensive antioxidant blend with Vitamins C, E and essential minerals'
            }
        ]

        protein_products = [
            {
                'code': '3530',
                'name': 'Lifeplus Triple Protein Shake - Chocolate',
                'format': '867g',
                'price': 87.75,
                'description': 'Premium triple protein formula with whey, casein, and soy proteins'
            },
            {
                'code': '3531',
                'name': 'Lifeplus Triple Protein Shake - Vanilla',
                'format': '813g',
                'price': 87.75,
                'description': 'Premium triple protein formula with whey, casein, and soy proteins'
            },
            {
                'code': '3442',
                'name': 'Lifeplus Vegan Protein Shake - Chocolate',
                'format': '1235g',
                'price': 93.50,
                'description': 'Complete plant-based protein formula for vegan nutrition'
            }
        ]

        sports_nutrition = [
            {
                'code': '3434',
                'name': 'BE Focused - Berry',
                'format': '384g',
                'price': 82.25,
                'description': 'Pre-workout mental energy formula with 3g creatine for enhanced focus'
            },
            {
                'code': '3421',
                'name': 'BE Focused - Citrus',
                'format': '384g',
                'price': 82.25,
                'description': 'Pre-workout mental energy formula with 3g creatine for enhanced focus'
            },
            {
                'code': '3466',
                'name': 'BE Recharged - Berry',
                'format': '624g',
                'price': 84.75,
                'description': 'Recovery formula with 2:1:1 BCAA ratio for muscle development'
            }
        ]

        solis_products = [
            {
                'code': '3483',
                'name': 'SOLIS Green Medley',
                'format': '171g',
                'price': 69.75,
                'description': '27 superfoods blend with adaptogens for natural vitality'
            },
            {
                'code': '3484',
                'name': 'SOLIS Purple Flash®',
                'format': '183g',
                'price': 79.75,
                'description': 'Antioxidant-rich superfruit formula with premium Aronia berries'
            },
            {
                'code': '3485',
                'name': 'SOLIS Cacao Boost',
                'format': '210g',
                'price': 49.50,
                'description': 'Natural energy blend with Reishi mushroom and maca root'
            },
            {
                'code': '3525',
                'name': 'SOLIS Golden Milk',
                'format': '182g',
                'price': 50.00,
                'description': 'Relaxation formula with premium Ashwagandha KSM-66® for nighttime wellness'
            }
        ]

        forever_young = [
            {
                'code': '4144',
                'name': 'Forever Young Day Crème SPF 25',
                'format': '50 ml',
                'price': 73.25,
                'description': 'Daily moisturizer with SPF 25 protection and alpine rose extract'
            },
            {
                'code': '4131',
                'name': 'Forever Young Radiance Serum',
                'format': '30 ml',
                'price': 71.50,
                'description': 'Intensive treatment serum with lifting effect and antioxidants'
            },
            {
                'code': '4132',
                'name': 'Forever Young Rich Moisturizing Crème',
                'format': '50 ml',
                'price': 64.50,
                'description': 'Deep hydration anti-aging formula with natural ingredients'
            }
        ]

        # Add product sections
        self.add_product_section("Nutritional Supplements", nutritional_products)
        self.add_product_section("Proteins & Shakes", protein_products)
        self.add_product_section("Sports Nutrition", sports_nutrition)
        self.add_product_section("Superfoods SOLIS", solis_products)
        self.add_product_section("Forever Young Skincare", forever_young)

        # Build PDF
        doc.build(self.story, onFirstPage=self.create_header_footer, onLaterPages=self.create_header_footer)

        print(f"PDF Catalog '{self.output_filename}' created successfully!")
        return self.output_filename

def main():
    """Main function to generate the PDF catalog"""
    print("🚀 Creating LifePlus Product Catalog PDF...")

    generator = LifePlusPDFGenerator("LifePlus_Product_Catalog.pdf")
    pdf_file = generator.generate_pdf()

    print(f"✅ PDF generated: {pdf_file}")
    print("📄 Ready for distribution!")

if __name__ == "__main__":
    main()