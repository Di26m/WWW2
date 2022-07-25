import json
import ebooklib
import pypandoc
import catpandoc
from ebooklib import epub
from pathlib import Path
from ebooklib.utils import parse_string, parse_html_string, guess_type, get_pages_for_items

# def epub_to_txt(file_path='test.txt', language='en'):

    # if Path(file_path).is_file() and Path(file_path).suffix == '.txt':
        # return "File norm"
def epub_to_txt(file_path='Charlz.epub', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.epub':
        # return "File norm"
        with epub(open(file = file_path, mode='rb')).read as epub:
            pages = [page.extract_text() for page in epub.pages]

        text = ''.join(pages)

        with open('text1.txt', 'w') as file:
            file.write(text)
        text = text.replace('\n', '')
        with open('text2.txt', 'w') as file:
            file.write(text)
    else:
        return "File bad"
def main():
    # print(epub_to_txt(file_path='test.txt'))
    print(epub_to_txt(file_path='Charlz.epub'))
if __name__ == "__main__":
    main()

# book = epub.read_epub('Charlz.epub')
#
# for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
#     print(doc)
py