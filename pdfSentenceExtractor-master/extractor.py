import pdfplumber
import re

fileurl1 = '.\\pdfs\\asamblea.pdf' 
fileurl2 = '.\\pdfs\\utp.pdf' 


def extractor(fileurl): 
    pdf = pdfplumber.open(fileurl)
    content = ''
    for page in pdf.pages:
        content = content + page.extract_text()
    pdf.close()
    return content

def sentenceExtractor(content):
    oraciones = re.findall(r'\—[A-Z\sÑ\.\,ÁÉÍÓÚ]*([A-Z\sÑ\.\,ÁÉÍÓÚ][a-zA-Z\s\.áéíóúÁÉÍÓÚ\,\¿\?ñÑ0-9\'\"\“\”\:\-]*)', content)
    
    #Sentece cleaning: Eliminar el footer del pdf
    for idx,oracion in enumerate(oraciones):
        if 'Acta de la sesión ordinaria' in oracion:
            oraciones[idx] = oracion[:oracion.index('Acta de la sesión ordinaria')]

    file1 = open("Separated.txt","a") 
    for oracion in oraciones:
        file1.write("-----")
        file1.write(oracion)
    file1.close() 

    return oraciones


def pdfSentenceExtractor(file):
    return sentenceExtractor(extractor(file))

if __name__ == "__main__":
    res = pdfSentenceExtractor(fileurl1)
    print(res)