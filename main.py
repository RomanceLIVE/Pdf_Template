from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
# this is a python object (class type)
#page orientation portrait, milimereters and A4 format

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There", align="L", ln=1)
        #width, height, ln=breakline
pdf.set_font(family="Times", size=10)
# we removed style="B" due to preference
pdf.cell(w=0, h=12, txt="Hi There", align="L", ln=1)
# we removed border due to preference

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There", align="L", ln=1)
        #width, height, ln=breakline
pdf.set_font(family="Times", size=10)
# we removed style="B" due to preference
pdf.cell(w=0, h=12, txt="Hi There", align="L", ln=1)
# we removed border due to preference

pdf.output("output.pdf")