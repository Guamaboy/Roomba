### 01 / 01 / 2021
### Web scrapper Development
### Author: Guamaboy

# Import Libraries
import os
import time
import webbrowser
from requests import get
from datetime import datetime
from twilio.rest import Client
from bs4 import BeautifulSoup as Soup

os.system('cls')

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
    # Playstation 5
    "https://www.newegg.com/p/pl?d=ps5&N=101696840&isdeptsrh=1",
    # Intel 10900k
    #"https://www.newegg.com/p/pl?d=intel+10900k&N=100007671&isdeptsrh=1",
    # RTX 3080
    "https://www.newegg.com/p/pl?d=rtx+3080&N=100007709&isdeptsrh=1",
    
]

# Using requests library to download webpages and bs4 to parse them
# Headers are to diguise the bot as an ordinary browser
def soupify():
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    page = get(url, headers=headers)
    soup = Soup(page.text, 'html.parser')
    return soup

# Twilio SMS API variables
try:
    account_sid = os.environ['TwilioSid']
    auth_token = os.environ['TwilioAuth']
    client = Client(account_sid, auth_token)
except:
    print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["yellow"] + '  Warn  ' + color["magenta"] + '|| ' + color["cyan"] + 'Twilio' + color['white'] + '  ---------------->  ' + color["yellow"] + 'Failed setting variables for SMS API. Visit "' + color["cyan"] + 'https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python' + color["yellow"] + '" for more info.')
sentProducts = []

def sendsms():
    message = client.messages \
                .create(
                     body = ('In Stock \n' + product.find('li', class_='price-current').text[:-1] + '\n' + product.find('a',class_="item-title")['href']),
                     from_ = os.environ['TwilioPhone'],
                     to = os.environ['MyPhone']
                 )
    print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["green"] + '  Info  ' + color["magenta"] + '|| ' + color["cyan"] + 'Twilio' + color['white'] + '  ---------------->  ' + color["cyan"] + 'Successfully sent product link via SMS to your phone.')

# Open the default browser to the product page
def openLink():
    webbrowser.open(product.find('a',class_="item-title")['href'])
    print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["green"] + '  Info  ' + color["magenta"] + '|| ' + color["white"] + 'System' + color['white'] + '  ---------------->  ' + color["cyan"] + 'Successfully opened browser with link to product page.')


# While loop to initate iteration through urls
while urls != 0:
    for url in urls:

### Newegg ###
        if url.split('.')[1] == 'newegg':
            soup = soupify()
            products = soup.find_all('div', class_="item-container")
            for product in products:
                try:
# If 'COMING SOON'
                    if product.find('li', class_='price-current').text == 'COMING SOON':
                        print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["green"] + '  Info  ' + color["magenta"] + '|| ' + color["blue"] + url.split('.')[1].capitalize() + color["magenta"] + ' || ' + color['yellow'] + 'COMING SOON ' + color["magenta"] + ' || ' + color["white"] + product.find('a',class_="item-title").text[:150])
# If 'OUT OF STOCK'
                    elif product.find('p',class_="item-promo").text == 'OUT OF STOCK':
                        print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["green"] + '  Info  ' + color["magenta"] + '|| ' + color["blue"] + url.split('.')[1].capitalize() + color["magenta"] + ' || ' + color['red'] + product.find('p',class_="item-promo").text + color["magenta"] + ' || ' + color["white"] + product.find('a',class_="item-title").text[:150])
# If 'IN STOCK'
                    elif product.find('button',class_="btn").text == 'View Details' or 'Add to cart':
                        print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["green"] + '  Info  ' + color["magenta"] + '|| ' + color["blue"] + url.split('.')[1].capitalize() + color["magenta"] + ' || ' + color['green'] + '  IN STOCK  ' + color["magenta"] + ' || ' + color["white"] + product.find('a',class_="item-title").text[:150])

# Send an SMS once eveytime an item comes into stock.(Part of the 'IN STOCK' if statement)
                        try:
                            if product.find('a',class_="item-title").text not in sentProducts:
                                sentProducts.append(product.find('a',class_="item-title").text)
                                openLink()
                                sendsms()
                        except:
                            print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["red"] + '  Error ' + color["magenta"] + '|| ' + color["cyan"] + 'Twilio' + color['white'] + '  ---------------->  ' + color["red"] + 'Error sending SMS with product link to phone.')
                except:
                    print(color["white"] + datetime.now().strftime("[%I:%M:%S %p]") + color["yellow"] + '  Warn  ' + color["magenta"] + '|| ' + color["blue"] + url.split('.')[1].capitalize() + color["magenta"] + ' || ' + color['yellow'] + 'Item Except ' + color["magenta"] + ' || ' + color["white"] + product.find('a',class_="item-title").text[:150])

                time.sleep(.25)
            
        else:
            print("The url " + url + " is not currently supported!")

# Set a timeout to avoid spam/bot detection
    print(color["yellow"] + "Pausing to avoid bot detection\nChecking again every 3 seconds...")
    time.sleep(3)

print("There are no sites to scrap\nOpen the .py and append the 'urls' list")