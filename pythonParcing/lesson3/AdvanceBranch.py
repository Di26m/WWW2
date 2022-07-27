import os
import pypandoc
from pathlib import Path

from gtts import gTTS
import re
def Fb2_to_mp3(file_path="test.fb2"):
    if Path(file_path).is_file() and Path(file_path).suffix == '.fb2':
        # return "Good"
        file_name = Path(file_path).stem


        # with pypandoc.convert_file(open(file=f'{file_path}', mode="r+"), 'context', outputfile=f'{file_name}.txt') as fb2:
            content = fb2.read()

            file_content = re.sub(r"[\/|,|\[|\],\\,\{,\},\-,\~,\=,A-z,]", "", content).replace("\n", " ")
            fb2.write(file_content)


# result = pypandoc.convert_file('Ataman.fb2', 'context', outputfile="Ataman.txt")

# result = pypandoc.convert_file('Ataman.html', 'context', outputfile="Ataman2.txt")
# result = pypandoc.convert_file('Ataman.fb2', 'html', outputfile="Ataman.html")


# with open('Ataman.txt', 'r+', encoding='utf-8') as f:
#
#     # ----------создал пер F, потом прочитал ее переменной content, записал в file_content переменную content без лишних символов)
#     content = f.read()
#     # file_content =re.sub(r"[\/|,|\[|\], \\,\{,\},\-,\~]", "", content)
#     file_content = re.sub(r"[\/|,|\[|\],\\,\{,\},\-,\~,\=,A-z,]", "", content).replace("\n"," ")
#
#     print(file_content)
#
# with open('Ataman2.txt', 'w', encoding='utf-8') as f:
#     f.write(file_content)

    else:
        return "File is not FB2"

def main():
    print(Fb2_to_mp3(file_path='Ataman.fb2'))

if __name__ == '__main__':
    main()