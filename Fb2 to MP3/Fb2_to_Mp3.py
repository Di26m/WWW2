import os
import pypandoc
from pathlib import Path
import pathlib
import glob
from gtts import gTTS
import re


def fb2_to_mp3(file_path=input("ВВедите путь"), language='ru'):
    os.chdir(file_path)
    for file_path in glob.glob("*.fb2"):

        if Path(file_path).is_file() and Path(file_path).suffix == '.fb2':
            pypandoc.convert_file(f'{file_path}', 'context', outputfile=f"{file_path}.txt")

        with open(f'{file_path}.txt', mode='r+', encoding='utf-8') as f:
            content = f.read()

            file_content = re.sub(r"[\/|,|\[|\],\\,\{,\},\-,\~,\=,A-z,]", "", content).replace("\n", " ")
            # print(file_content)

        with open(f'{file_path}.txt', 'w', encoding='utf-8') as f:
            f.write(file_content)

        my_audio = gTTS(text=file_content, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 создан успешно!'


    else:
        return "bad"


def main():
    print(fb2_to_mp3())


if __name__ == '__main__':
    main()
