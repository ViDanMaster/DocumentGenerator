import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from Factories.AbstractFactory import AbstractFactory

class PDFFactory(AbstractFactory):
    def __init__(self, name):
        self.folder_path = 'Results/'
        self.filename = name
        self.canvas = canvas.Canvas(self.getSavePath(), pagesize=(800, 1000))
        pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Times New Roman', 'Times New Roman.ttf'))
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))        

    def createTitle(self, title_text, font_size, font_family, alignment) -> None:
        self.canvas.setFont(font_family, font_size)
        y = 950
        self.getAlignment(alignment, y, title_text)

    def createContent(self, content_text, font_size, font_family, alignment) -> None:
        self.canvas.setFont(font_family, font_size)
        y = 900
        self.getAlignment(alignment, y, content_text)

    def createFooter(self, footer_text, font_size, font_family, alignment) -> None:
        self.canvas.setFont(font_family, font_size)
        y = 50
        self.getAlignment(alignment, y, footer_text)

    def save(self):
        self.canvas.save()

    def getAlignment(self, alignment, y, text):
        if alignment.lower() == "left":
            self.canvas.drawString(100, y, text)
        elif alignment.lower() == "center":
            self.canvas.drawCentredString(400, y, text)
        elif alignment.lower() == "right":
            self.canvas.drawRightString(700, y, text)
    
    def getSavePath(self):
        return os.path.join(self.folder_path, self.filename)