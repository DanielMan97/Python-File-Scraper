import urllib.request
import wget
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os



root = "http://rpi.edu/dept/arc/training/latex/resumes/"
response = urllib.request.urlopen(root)
soup = BeautifulSoup(response.read(), "html.parser")

for elem in soup.select("a[href]"):
    if ".tex" in elem['href']:
        wget.download(urljoin(root, elem['href']))


