### 01 / 01 / 2021
### Web scrapper Development
### Author: Edwin Guama

from os import system as cmd
from bs4 import BeautifulSoup as Soup


cmd('color a')
color = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "reset": "\u001b[0m"
}
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')