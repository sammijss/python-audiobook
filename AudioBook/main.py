# PDF Reader
import pyttsx3  # pip install pyttsx3
import PyPDF2   # pip install PyPDF2

book = open('pdfbook.pdf', 'rb')
pdffilereader = PyPDF2.PdfFileReader(book)
pages = pdffilereader.numPages  # Total number of pages in the pdf book
speaker = pyttsx3.init()
for num in range(11, pages):  # 11 is the index of page, not the actual page number
    page = pdffilereader.getPage(num)
    text = page.extractText()
    speaker.say(text)
speaker.runAndWait()