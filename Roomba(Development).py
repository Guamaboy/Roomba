### 01 / 01 / 2021
### Web scrapper Development
### Author: Edwin Guama

# Import Libraries
from requests import get
from os import system as cmd
from bs4 import BeautifulSoup as Soup

# Color Dictionary
color = {
    "white": "\u001b[37m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "yellow": "\u001b[33m",
    "cyan": "\u001b[36m",
    "black": "\u001b[30m"
}

# Website urls
# Paste supported urls in format of: "https://websitename.com/productpage"
urls = [
    "https://www.newegg.com/p/pl?d=3080&N=100007709&isdeptsrh=1",
]

# Using requests library to download webpages and bs4 to parse them
# Headers are to diguise the bot as an ordinary browser
def soupify():
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    page = get(url, headers=headers)
    soup = Soup(page.content, 'html.parser')

# While loop to initate iteration through urls
while True:
    for url in urls:
        soupify()
