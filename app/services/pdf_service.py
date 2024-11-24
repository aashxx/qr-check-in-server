from fpdf import FPDF

def generate_pdf(name, qr_code_path, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Crescent Innovation & Incubation Council", ln=True, align="C")
    pdf.cell(200, 10, txt="Demo Day Pass", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True, align="C")
    pdf.image(qr_code_path, x=80, y=50, w=50)
    pdf.cell(200, 10, txt="Powered by Schedrix", ln=True, align="C")

    pdf.output(pdf_path)
