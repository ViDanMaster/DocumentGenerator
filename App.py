import tkinter as tk
from tkinter import messagebox
from docx.enum.text import WD_ALIGN_PARAGRAPH

from File import File
from Factories.WordFactory import WordFactory
from Factories.PDFFactory import PDFFactory

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Generator")
        
        self.filename_frame = tk.Frame(root, padx=20, pady=20)
        self.filename_frame.pack()

        self.filename_label = tk.Label(self.filename_frame, text="File Name:")
        self.filename_label.grid(row=0, column=0)
        self.filename_entry = tk.Entry(self.filename_frame)
        self.filename_entry.grid(row=0, column=1)
        self.filename_entry.insert(0, "document")

        self.filename_extension_label = tk.Label(self.filename_frame, text="Extension:")
        self.filename_extension_label.grid(row=0, column=2)
        self.filename_extension_var = tk.StringVar(root)
        self.filename_extension_var.set(".docx")
        filename_extensions = [".docx", ".pdf"]
        self.filename_extension_menu = tk.OptionMenu(self.filename_frame, self.filename_extension_var, *filename_extensions)
        self.filename_extension_menu.grid(row=0, column=3)

        self.title_frame = tk.Frame(root, padx=20, pady=20)
        self.title_frame.pack()

        self.title_label = tk.Label(self.title_frame, text="Title:")
        self.title_label.grid(row=0, column=2)
        self.title_entry = tk.Entry(self.title_frame)
        self.title_entry.grid(row=0, column=3)

        self.font_family_label = tk.Label(self.title_frame, text="Font Family:")
        self.font_family_label.grid(row=1, column=0)
        self.font_family_var = tk.StringVar(root)
        self.font_family_var.set("Arial")
        font_families = ["Arial", "Times New Roman", "Verdana", "Helvetica"]
        self.font_family_menu = tk.OptionMenu(self.title_frame, self.font_family_var, *font_families)
        self.font_family_menu.grid(row=1, column=1)

        self.font_size_label = tk.Label(self.title_frame, text="Font Size:")
        self.font_size_label.grid(row=1, column=2)
        self.font_size_var = tk.StringVar(root)
        self.font_size_var.set("24")
        font_sizes = ["10", "12", "14", "16", "18", "20", "24", "28", "32", "36", "40"]
        self.font_size_menu = tk.OptionMenu(self.title_frame, self.font_size_var, *font_sizes)
        self.font_size_menu.grid(row=1, column=3)

        self.alignment_label = tk.Label(self.title_frame, text="Alignment:")
        self.alignment_label.grid(row=1, column=4)
        self.alignment_var = tk.StringVar(root)
        self.alignment_var.set("Center")
        alignments = ["Left", "Center", "Right"]
        self.alignment_menu = tk.OptionMenu(self.title_frame, self.alignment_var, *alignments)
        self.alignment_menu.grid(row=1, column=5)

        self.content_frame = tk.Frame(root, padx=20, pady=20)
        self.content_frame.pack()

        self.content_label = tk.Label(self.content_frame, text="Content:")
        self.content_label.grid(row=0, column=2)
        self.content_entry = tk.Entry(self.content_frame)
        self.content_entry.grid(row=0, column=3)

        self.content_font_family_label = tk.Label(self.content_frame, text="Font Family:")
        self.content_font_family_label.grid(row=1, column=0)
        self.content_font_family_var = tk.StringVar(root)
        self.content_font_family_var.set("Arial")
        self.content_font_family_menu = tk.OptionMenu(self.content_frame, self.content_font_family_var, *font_families)
        self.content_font_family_menu.grid(row=1, column=1)

        self.content_font_size_label = tk.Label(self.content_frame, text="Font Size:")
        self.content_font_size_label.grid(row=1, column=2)
        self.content_font_size_var = tk.StringVar(root)
        self.content_font_size_var.set("14")
        self.content_font_size_menu = tk.OptionMenu(self.content_frame, self.content_font_size_var, *font_sizes)
        self.content_font_size_menu.grid(row=1, column=3)

        self.content_alignment_label = tk.Label(self.content_frame, text="Alignment:")
        self.content_alignment_label.grid(row=1, column=4)
        self.content_alignment_var = tk.StringVar(root)
        self.content_alignment_var.set("Left")
        self.content_alignment_menu = tk.OptionMenu(self.content_frame, self.content_alignment_var, *alignments)
        self.content_alignment_menu.grid(row=1, column=5)

        self.footer_frame = tk.Frame(root, padx=20, pady=20)
        self.footer_frame.pack()

        self.footer_label = tk.Label(self.footer_frame, text="Footer:")
        self.footer_label.grid(row=0, column=2)
        self.footer_entry = tk.Entry(self.footer_frame)
        self.footer_entry.grid(row=0, column=3)

        self.footer_font_family_label = tk.Label(self.footer_frame, text="Font Family:")
        self.footer_font_family_label.grid(row=1, column=0)
        self.footer_font_family_var = tk.StringVar(root)
        self.footer_font_family_var.set("Helvetica")
        self.footer_font_family_menu = tk.OptionMenu(self.footer_frame, self.footer_font_family_var, *font_families)
        self.footer_font_family_menu.grid(row=1, column=1)

        self.footer_font_size_label = tk.Label(self.footer_frame, text="Font Size:")
        self.footer_font_size_label.grid(row=1, column=2)
        self.footer_font_size_var = tk.StringVar(root)
        self.footer_font_size_var.set("10")
        self.footer_font_size_menu = tk.OptionMenu(self.footer_frame, self.footer_font_size_var, *font_sizes)
        self.footer_font_size_menu.grid(row=1, column=3)

        self.footer_alignment_label = tk.Label(self.footer_frame, text="Alignment:")
        self.footer_alignment_label.grid(row=1, column=4)
        self.footer_alignment_var = tk.StringVar(root)
        self.footer_alignment_var.set("Right")
        self.footer_alignment_menu = tk.OptionMenu(self.footer_frame, self.footer_alignment_var, *alignments)
        self.footer_alignment_menu.grid(row=1, column=5)

        self.generate_button = tk.Button(root, text="Generate document", command=self.generate_document)
        self.generate_button.pack()

    def generate_document(self):
        try:
            extension = self.filename_extension_var.get()
            if extension == ".docx":
                factory = WordFactory(f"{self.filename_entry.get()}{extension}")
            elif extension == ".pdf":
                factory = PDFFactory(f"{self.filename_entry.get()}{extension}")

            title_settings = {
                'font_family': self.font_family_var.get(),
                'font_size': int(self.font_size_var.get()),
                'alignment': self.getAlignment(self.alignment_var.get()),
            }

            content_settings = {
                'font_family': self.content_font_family_var.get(),
                'font_size': int(self.content_font_size_var.get()),
                'alignment': self.getAlignment(self.content_alignment_var.get()),
            }

            footer_settings = {
                'font_family': self.footer_font_family_var.get(),
                'font_size': int(self.footer_font_size_var.get()),
                'alignment': self.getAlignment(self.footer_alignment_var.get()),
            }

            file = File(factory, self.title_entry.get(), self.content_entry.get(), self.footer_entry.get(), title_settings, content_settings, footer_settings)
            file.generate()

            messagebox.showinfo("Done generating!", "The document is generated successfully!")
        except Exception as e:
            messagebox.showerror("Something bad happened!", "An error occurred while generating the document: " + str(e))

    def getAlignment(self, alignment_var):
        if self.filename_extension_var.get() == ".docx":
            alignment_value = {
                "left": WD_ALIGN_PARAGRAPH.LEFT,
                "center": WD_ALIGN_PARAGRAPH.CENTER,
                "right": WD_ALIGN_PARAGRAPH.RIGHT,
            }.get(alignment_var.lower())
            return alignment_value
        else:
            return alignment_var