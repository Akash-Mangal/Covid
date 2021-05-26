from fpdf import FPDF
import base64
import streamlit as st

title='Covid-19 Detection'

class PDF(FPDF):
    def header(self):
        
        # Times bold 45
        self.set_font('Times', 'B', 45) 
        self.set_text_color(220, 82, 82)
        # Title
        self.cell(0, 30, title, 0, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 3.5, 'Page ' + str(self.page_no()), 0, 0, 'C',fill=True)

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

def crt_pdf(profile):  

    
    # Instantiation of inherited class
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    
    #Setting patient id and date of issue
    pdf.ln(8)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(21.1624,10,'Patient ID: ', 0,0, 'L')
    pdf.set_font('Times', '', 12)
    pdf.cell(0,10, str(profile.id) , 0,0, 'L')
    pdf.set_font('Times', '', 12)
    pdf.cell(0,10, 'Issued on: '+ profile.uploaded_on , 0,1, 'R')
    
    
    #Printing patient details
    pdf.ln(15)
    pdf.set_draw_color(230,232, 236)
    pdf.set_fill_color(240, 242, 246)
    pdf.set_text_color(246, 51, 102)
    # Thickness of frame (.7 mm)
    pdf.set_line_width(.7)
    pdf.set_font('Arial', '', 15)
    pdf.cell(0, 10, ' Name:', 1, 0,fill=True)
    pdf.set_x(107)
    pdf.cell(0,  10, profile.name, 1, 1,fill=True)
    pdf.cell(0, 10, ' Age:', 1, 0,fill=True)
    pdf.set_x(107)
    pdf.cell(0,  10, str(profile.age), 1, 1,fill=True)
    pdf.cell(0,  10, ' Gender:', 1, 0,fill=True)
    pdf.set_x(107)
    pdf.cell(0,  10, profile.gender, 1, 1,fill=True)
    pdf.cell(0,  10, ' Contact:', 1, 0,fill=True)
    pdf.set_x(107)
    pdf.cell(0,  10, str(profile.contact), 1, 1,fill=True)
    pdf.cell(0,  10, ' Status:', 1, 0,fill=True)
    pdf.set_x(107)
    pdf.cell(0,  10, profile.result, 1, 1, fill=True)
    pdf.ln(12)

    #About Project
    pdf.set_font('Times','', 14)
    pdf.set_text_color(10, 10, 10)
    pdf.multi_cell(0,8,'''Covid-19 pneumonia causes the density of the lungs to increase. This may be seen as whiteness in the lungs on radiography which, depending on the severity of the pneumonia, obscures the lung markings that are normally seen. However, this may be delayed in appearing or absent. When interpreting the x-ray, the AI will look for white spots in the lungs (called infiltrates) that identify an infection. This exam will also help determine if you have any complications related to pneumonia such as abscesses or pleural effusions (fluid surrounding the lungs).''',0,'J')
    pdf.ln(10)

    #About Status
    
    
    pdf.set_font('Times', 'I', 13)
    pdf.set_text_color(10, 100, 10)
    pdf.cell(0,8,'''Normal: Covid-19 pneumonia or any other pneumonia has not been detected.''',0,1) 
    pdf.set_text_color(10, 10, 100)
    pdf.cell(0,8,'''Pneumonia: Pneumonia other than Covid-19 has been detected.''',0,1)
    pdf.set_text_color(100, 10, 10)
    pdf.cell(0,8,'''Covid-19: Covid-19 has been detected.''',0,1)
    pdf.ln(35)

    #authorisation
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(5, 5, 150)
    pdf.cell(0,6,'''(Authority Name)\t\t''',0,2,'R')
    pdf.set_font('Arial', 'I', 12)
    pdf.cell(0,8,'''(Authority Designation)\t''',0,1,'R')

    #Declaration
    pdf.set_line_width(.5)
    pdf.line(15,264,195,264)
    pdf.set_font('Times', '',12)
    pdf.set_text_color(150, 150, 150)
    pdf.set_y(267)
    pdf.multi_cell(0,4.5,'''Declaration: This software is designed for educational purpose. This software based medical report do not have any medical certification or verfication. This report can not be used for any medical treatment.''',0,1
    
    
    
    
    )
    pdf.line(15,279,195,279)

    pdf.output('tuto2.pdf', 'F')
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")
    st.markdown(html, unsafe_allow_html=True)
    