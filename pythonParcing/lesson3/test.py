import os
import pypandoc
from pathlib import Path
import  pathlib
import glob
from gtts import gTTS
import re



# for root, dirs, files in os.walk(input("ВВедите путь")):
#     for file in files:
#         if file.endswith(".fb2"):
#             file_path = os.path.join(root, file)
#             print(os.path.join(root, file))
def Fb2_to_mp3(file_path = input("ВВедите путь")):
    os.chdir(file_path)
    for file_path in glob.glob("*.fb2"):

         if Path(file_path).is_file() and Path(file_path).suffix == '.fb2':
             return "good"




