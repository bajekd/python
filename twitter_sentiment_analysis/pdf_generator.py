import datetime

from fpdf import FPDF

WIDTH = 210
HEIGHT = 297


class PDFGenerator:
    def __init__(self, tweets_num, tweeter_username):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.tweets_num = tweets_num
        self.tweeter_username = tweeter_username
        self._create_title()

    def _create_title(self):
        self.pdf.set_font("Arial", "B", 36)
        self.pdf.ln(2)
        self.pdf.write(10, f"User: {self.tweeter_username} / Tweets: {self.tweets_num}")
        self.pdf.ln(10)
        self.pdf.set_font("Arial", "", 18)
        subtitle = f"{datetime.date.today()}"
        self.pdf.write(10, f"{subtitle:>75}")

    def save(self, path_to_word_chart, path_to_scatter_chart, path_to_pie_chart):
        self.pdf.image(path_to_scatter_chart, 0, 40, WIDTH / 2)
        self.pdf.image(path_to_pie_chart, WIDTH / 2, 40, WIDTH / 2)
        self.pdf.image(path_to_word_chart, 0, 115, WIDTH)

        self.pdf.output(f"pdfs/{self.tweeter_username}_{self.tweets_num}_{datetime.date.today()}.pdf")
