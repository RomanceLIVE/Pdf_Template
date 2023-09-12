from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
# this is a python object (class type)
#page orientation portrait, milimereters and A4 format

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
# we add each row as a page using for loop instead of manually writing each row page
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
                        #rgb color values for grey
                        # for red its 254, 0, 0
                        # for blue its 0, 0, 254
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        #width, height, ln=breakline
    pdf.line(10, 21, 200, 21)
            #x1,  y1,  x2,  y2 line values, which are 2D line distances of trajectory


# pdf.set_font(family="Times", size=10)
# we removed style="B" due to preference
# pdf.cell(w=0, h=12, txt="Hi There", align="L", ln=1)
# we removed border due to preference

pdf.output("output.pdf")