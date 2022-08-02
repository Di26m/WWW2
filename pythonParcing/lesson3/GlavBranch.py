import os
import pypandoc
from bs4 import BeautifulSoup
import lxml
from gtts import gTTS
import re

result = pypandoc.convert_file('Ataman.fb2', 'context', outputfile="Ataman.txt")

# result = pypandoc.convert_file('Ataman.html', 'context', outputfile="Ataman2.txt")
# result = pypandoc.convert_file('Ataman.fb2', 'html', outputfile="Ataman.html")


with open('Ataman.txt', 'r+', encoding='utf-8') as f:

    # ----------создал пер F, потом прочитал ее переменной content, записал в file_content переменную content без лишних символов)
    content = f.read()
    # file_content =re.sub(r"[\/|,|\[|\], \\,\{,\},\-,\~]", "", content)
    file_content = re.sub(r"[\/|,|\[|\],\\,\{,\},\-,\~,\=,A-z,]", "", content).replace("\n"," ")

    print(file_content)

with open('Ataman2.txt', 'w', encoding='utf-8') as f:
    f.write(file_content)

