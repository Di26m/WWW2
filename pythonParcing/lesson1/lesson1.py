d(sys)
import locale
sys.setdefaultencoding(locale.getpreferredencoding())efaultencoding(‘utf-8′)t sys
reload(sys)
# pip install beautifulsoup4 lxml
from bs4 import BeautifulSoup

with open ('blank/index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title)
print(title.text)