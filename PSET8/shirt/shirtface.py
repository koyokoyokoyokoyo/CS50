from fpdf import FPDF, Align

class PDF(FPDF):

    def header(self):
        self.image("shirtificate.png", x=Align.C, y=60, w=0, h=190)
        self.set_font("Times", style="BI", size=45,)
        self.multi_cell(text="CS50 Shirtification", w=0, h=30, border=0, align="C", fill=False)
        self.ln(10)

    def footer(self):
        name = input("Name: ")
        self.set_font("helvetica", style="I", size=25)
        self.set_text_color(255)
        self.multi_cell(text=f"{name} completed CS50", w=0, h=150, border=0, align="C", fill=False)


def main():
    pdf = PDF(orientation='portrait', unit='mm', format='A4')
    pdf.output("new.pdf")

if __name__ == "__main__":
    main()