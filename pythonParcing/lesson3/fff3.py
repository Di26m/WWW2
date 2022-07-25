import os
import pypandoc
from bs4 import BeautifulSoup
import lxml
import re

# result = pypandoc.convert_file('Ataman.fb2', 'context', outputfile="Ataman.txt")
# result = pypandoc.convert_file('Ataman.html', 'context', outputfile="Ataman2.txt")
# result = pypandoc.convert_file('Ataman.fb2', 'html', outputfile="Ataman.html")
# with open('Ataman.html', encoding='utf-8') as file:
#     src = file.read()
# with open('Ataman.txt', 'r+', encoding='utf-8') as f:
text =  open('Ataman.txt', 'r+', encoding='utf-8')
f = text.read(str)
    # text = ''.join([line.replace("\\", "") for line in f.readlines()])
    # f.seek(0)
    # f.write(text)

    # text = re.sub(r"[a-z]", "", f)
    # f.write(text)

    # text = re.sub("[$|@|&]", "", f)
    # f.write(text)
    text = f.strip("{}[]=+-`~")
    f.write(text)
# soup = BeautifulSoup(src, "lxml")
#
# all_text = soup.find_all("h1").find_all("h2")
# print(all_text)