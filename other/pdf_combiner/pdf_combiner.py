import os
import PyPDF2


class PdfCombiner:
    def __init__(self):
        self.pdf_files = []

    def sort_pdfs(self):
        for filename in os.listdir('.'):
            if filename.endswith('.pdf'):
                self.pdf_files.append(filename)

        self.pdf_files.sort(key=lambda x: x.lower())

    def merge_pdfs(self, exclude_first_page=False):
        if exclude_first_page:
            pdf_writer = PyPDF2.PdfFileWriter()

            for pdf_file in self.pdf_files:
                with open(pdf_file, 'rb'), open('merged_result.pdf', 'wb') as merged_result:
                    '''File need to be open when write - see https://stackoverflow.com/questions
                    /49927338/merge-2-pdf-files-giving-me-an-empty-pdf/49927541#49927541'''
                    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                    for page_num in range(1, pdf_reader.numPages):
                        page = pdf_reader.getPage(page_num)
                        pdf_writer.addPage(page)
                    pdf_writer.write(merged_result)

        else:
            pdf_writer = PyPDF2.PdfFileWriter()

            for pdf_file in self.pdf_files:
                with open(pdf_file, 'rb'), open('merged_result.pdf', 'wb') as merged_result:
                    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                    for page_num in range(pdf_reader.numPages):
                        page = pdf_reader.getPage(page_num)
                        pdf_writer.addPage(page)
                    pdf_writer.write(merged_result)
