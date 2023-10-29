from model.atrasos import atrasos
from fpdf import FPDF
import requests
from PIL import Image
from io import BytesIO
from os.path import join, abspath
import os
from datetime import datetime


class handleAtrasos:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def buscarAtrasos():
        datos = atrasos.buscarAtrasos()
        Atrasos = []
        for atraso in datos:
            _atraso = {
                "nombres": atraso[0],
                "apellido_p": atraso[1],
                "apellido_m": atraso[2],
                "nivel": atraso[3],
                "letra": atraso[4],
                "rut": atraso[5],
                "avatar":atraso[6],
                "fecha": atraso[7],
                "hora": atraso[8],
                "idatraso": atraso[9],
                "idestudiante": atraso[10],
            }
            Atrasos.append(_atraso)
        return Atrasos
    
    def buscarAtraso(termino):
        datos = atrasos.buscarAtraso(termino)
        Atrasos = []
        for atraso in datos:
            _atraso = {
                "nombres": atraso[0],
                "apellido_p": atraso[1],
                "apellido_m": atraso[2],
                "nivel": atraso[3],
                "letra": atraso[4],
                "rut": atraso[5],
                "avatar":atraso[6],
                "fecha": atraso[7],
                "hora": atraso[8],
                "idatraso": atraso[9],
                "idestudiante": atraso[10],
            }
            Atrasos.append(_atraso)
        return Atrasos
    
    def buscarAtrasoId(id):
        datos = atrasos.buscarAtrasoId(id)
        Atrasos = []
        for atraso in datos:
            _atraso = {
                "nombres": atraso[0],
                "apellido_p": atraso[1],
                "apellido_m": atraso[2],
                "nivel": atraso[3],
                "letra": atraso[4],
                "rut": atraso[5],
                "avatar":atraso[6],
                "fecha": atraso[7],
                "hora": atraso[8],
                "idatraso": atraso[9],
                "idestudiante": atraso[10],
            }
            Atrasos.append(_atraso)
        return Atrasos

    def generarPDF(url):
        class PDF(FPDF):
            def header(self):
                self.set_font('Arial', 'B', 15)
            def footer(self):
                self.set_y(-15)

        pdf = PDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(0, 10, txt="Atraso de Damián Panes", ln=True, align='C')
        pdf.ln(10)

        pdf.set_x(40)

        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        temp_image_path = 'temp_avatar.jpg'
        img.save(temp_image_path)

        pdf.image(temp_image_path, x=40, y=30, w=40, h=50, type='', link=url)
        pdf.cell(40, 50, "", 1)
        pdf.cell(90, 10, "Damián Alberto Panes Lobos", 1)
        pdf.set_y(pdf.get_y() + 10)
        pdf.set_x(80)
        
        pdf.cell(25, 10, "Curso: 4F", 1)
        pdf.cell(65, 10, "RUT: 123456789", 1)

        pdf.set_y(pdf.get_y() + 10)
        pdf.set_x(80)

        pdf.cell(40, 10, "Fecha: 2023-10-13", 1)
        pdf.cell(50, 10, "Hora Entrada: 16:51 ", 1)

        pdf.set_y(pdf.get_y() + 10)
        pdf.set_x(80)

        pdf.cell(90, 10, "Fecha Impresión: 2023-10-13", 1)

        pdf.set_y(pdf.get_y() + 10)
        pdf.set_x(80)
        
        pdf.cell(90, 10, "Número de atraso: 1", 1)

        carpeta_reportes = join(abspath("."), "atrasos")
        if not os.path.exists(carpeta_reportes):
            os.makedirs(carpeta_reportes)
        pdf_file = join(carpeta_reportes, "atraso.pdf")
        pdf.output(pdf_file)

        return pdf_file