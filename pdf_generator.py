from fpdf import FPDF
import pandas as pd


my_pdf = FPDF(orientation='P', unit='mm' , format = 'A4')
my_pdf.set_auto_page_break(False , margin=0)
csvreader = pd.read_csv('topics.csv')

for index, row in csvreader.iterrows():
    for i in range(row["Pages"]):
        my_pdf.add_page()
        my_pdf.set_font('Times','B',size=24)
        my_pdf.set_text_color(100 ,100 , 100)
        my_pdf.cell(txt=row["Topic"] , ln=1 , w=0 , border=0, align='L' , h=12)
        my_pdf.line(x1=10, y1=22, x2=200, y2=22)
        y = 32
        while y < 275:
            my_pdf.line(x1=10, y1=y, x2=200, y2=y)
            y += 8



        my_pdf.set_y(-10)
        my_pdf.set_font('Times','I',size=8)
        my_pdf.set_text_color(100 ,100 , 100)
        my_pdf.cell(align="R" , w=0 , border=0 , h=8 , txt=row["Topic"])




my_pdf.output('output.pdf')


