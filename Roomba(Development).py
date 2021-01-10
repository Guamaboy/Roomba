### 01 / 01 / 2021
### Web scrapper Development
### Author: Guamaboy

# Import Libraries
import time
from requests import get
from os import system as cmd
from datetime import datetime
from bs4 import BeautifulSoup as Soup

cmd('cls')

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
# Paste supported urls in format of: "https://websitename.com/productpath/itempage"
urls = [
    "https://www.newegg.com/p/pl?d=rtx+3080&N=100007709&isdeptsrh=1",
]

# Using requests library to download webpages and bs4 to parse them
# Headers are to diguise the bot as an ordinary browser
def soupify():
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    page = get(url, headers=headers)
    soup = Soup(page.text, 'html.parser')
    return soup

# While loop to initate iteration through urls
while urls != 0:
    for url in urls:
        if url.split('.')[1] == 'newegg':
# Newegg
            soup = soupify()
            products = soup.find_all('div', class_="item-container")
            for product in products:
# If 'COMING SOON'
                if product.find('li', class_='price-current').text == 'COMING SOON':
                    print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["green"] + ' Info ' + color["magenta"] + '|| ' + color["blue"] + url.split('.')[1].capitalize() + color["magenta"] + ' || ' + color['yellow'] + 'COMING SOON ' + color["magenta"] + ' || ' + color["white"] + product.find_all('a',class_="item-title")[0].text[:150])
# If 'OUT OF STOCK'
                elif str(product.find('p',class_="item-promo")) == '<p class="item-promo"><i class="item-promo-icon"></i>OUT OF STOCK</p>':
                    print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["green"] + ' Info ' + color["magenta"] + '|| ' + color["blue"] + url.split('.')[1].capitalize() + color["magenta"] + ' || ' + color['red'] + product.find('p',class_="item-promo").text + color["magenta"] + ' || ' + color["white"] + product.find_all('a',class_="item-title")[0].text[:150])
# If 'IN STOCK'
                elif product.find('button',class_="btn").text == 'View Details' or 'Add to cart':
                    print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["green"] + ' Info ' + color["magenta"] + '|| ' + color["blue"] + url.split('.')[1].capitalize() + color["magenta"] + ' || ' + color['green'] + '  IN STOCK  ' + color["magenta"] + ' || ' + color["white"] + product.find_all('a',class_="item-title")[0].text[:150])

# Set a timeout to avoid spam detection
            print(color["yellow"] + "Pausing to avoid bot detection\nChecking again every 3 seconds...")
            time.sleep(3)
        else:
            print("The url " + url + " is not currently supported!")

print("There are no sites to scrap\nOpen the .py and append the 'urls' list")