#pyttsx3-library for convert text to speech-pip install pyttsx3 library
#pdf reader -pypdf2-read pdf for conversion-pip install pyPDF2
import pyttsx3
import PyPDF2
file=open("C:/Users/hp/Downloads/python/myprojects/myfile.pdf","rb")
pdf_reader=PyPDF2.PdfFileReader(file)
pages=pdf_reader.numPages
print(pages)
melo=pyttsx3.init()
for i in range(2,pages):
      page=pdf_reader.getPage(6)
      text=page.extract_text()
      melo.say(text)
      melo.runAndWait()
