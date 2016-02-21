import urllib.request
import wget
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os



root = "enter url you want to scrape"
response = urllib.request.urlopen(root)
soup = BeautifulSoup(response.read(), "html.parser")

for elem in soup.select("a[href]"):
    if "enter file extension of what you want to download e.g .pdf .doc etc" in elem['href']:
        wget.download(urljoin(root, elem['href']))


