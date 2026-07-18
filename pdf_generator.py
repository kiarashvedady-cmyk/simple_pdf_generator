import csv
from pydoc_data.topics import topics

from fpdf import FPDF
import pandas as pd

my_pdf = FPDF(orientation='P', unit='mm' , format = 'A4')

csvreader = pd.read_csv('topics.csv')

for index, row in csvreader.iterrows():
    my_pdf.add_page()
    my_pdf.set_font('Times','B',size=24)
    my_pdf.set_text_color(100 ,100 , 100)
    my_pdf.cell(txt=row["Topic"] , ln=1 , w=0 , border=0, align='L' , h=12)
    my_pdf.line(x1=10 , y1=22 , x2=200 , y2=22)


my_pdf.output('output.pdf', 'F')