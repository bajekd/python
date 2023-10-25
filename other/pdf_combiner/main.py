import sys

from pdf_combiner import PdfCombiner
from email_sender import Message


if len(sys.argv) == 4 and sys.argv[3] == 'exclude_first_page':
    receivers = sys.argv[1]
    subject = sys.argv[2]

    pdf_combiner = PdfCombiner()
    pdf_combiner.sort_pdfs()
    pdf_combiner.merge_pdfs(exclude_first_page=True)

    email_sender = Message(receivers, subject)
    email_sender.send_mail()

elif len(sys.argv) == 3:
    receivers = sys.argv[1]
    subject = sys.argv[2]

    pdf_combiner = PdfCombiner()
    pdf_combiner.sort_pdfs()
    pdf_combiner.merge_pdfs()

    email_sender = Message(receivers, subject)
    email_sender.send_mail()

elif len(sys.argv) == 2 and sys.argv[1] == 'exclude_first_page':
    pdf_combiner = PdfCombiner()
    pdf_combiner.sort_pdfs()
    pdf_combiner.merge_pdfs(exclude_first_page=True)

elif len(sys.argv) == 1:
    pdf_combiner = PdfCombiner()
    pdf_combiner.sort_pdfs()
    pdf_combiner.merge_pdfs()

else:
    raise TypeError('Something wrong with arguments - check readme.md and try again!')



