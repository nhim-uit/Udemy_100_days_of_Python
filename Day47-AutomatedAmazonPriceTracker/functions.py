from email.mime.multipart import MIMEMultipart

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


def get_response(url):
    response = requests.get(url)
    return response.text

