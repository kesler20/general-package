import pyttsx3
import PyPDF2

book = open('C:\\Users\\Uchek\OneDrive\\Documents\\Projects\\biotechnology\\s41477-019-0475-z.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
speaker = pyttsx3.init()
for item in range(pages + 1):
    page = pdfreader.getPage(item)
    text = ''    
    for i in page:
        text = page.extractText()

speaker.say(text)
speaker.runAndWait()
