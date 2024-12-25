from email.mime.multipart import MIMEMultipart

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


def get_response(url):
    response = requests.get(url)
    return response.text


def get_price(text):
    soup = BeautifulSoup(text, 'html.parser')
    price_whole = soup.find(name='span', class_='a-price-whole').getText()
    price_fraction = soup.find(name='span', class_='a-price-fraction').getText()
    price = float(price_whole + price_fraction)

    return price


