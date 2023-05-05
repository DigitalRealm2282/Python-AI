import PyPDF2
import pyttsx3
from googletrans import Translator

translator = Translator()

book = open ('C:\Artificial Intelligence for.NET.pdf', 'rb')

P = 1 ####if page 1 write 0 no. of page -1####

Total = 264

pdfReader = PyPDF2.PdfFileReader(book)

page = pdfReader.numPages

print(page)

speak = pyttsx3.init()

voices = speak.getProperty('voices') 
speak.setProperty('voice', voices[0].id)

for i in range (Total):
 from_page = pdfReader.getPage(P)
 text = from_page.extractText()
 trans_text = translator.translate(text, dest='ar')

 P = P + 1

 speak.say(trans_text)
 speak.runAndWait()
 if P == Total :
     break




 







