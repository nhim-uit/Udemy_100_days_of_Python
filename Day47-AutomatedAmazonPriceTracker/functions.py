from email.mime.multipart import MIMEMultipart

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


def get_response(url):
    """
        Fetches the HTML content of the given URL.

        Args:
            url (str): The URL of the webpage to fetch.

        Returns:
            str: The HTML content of the webpage.
    """
    response = requests.get(url)
    return response.text


def get_price(text):
    """
        Extracts the price from the HTML content of a product page.

        Args:
            text (str): The HTML content of the product page.

        Returns:
            float: The price of the product.
    """
    soup = BeautifulSoup(text, 'html.parser')
    price_whole = soup.find(name='span', class_='a-price-whole').getText()
    price_fraction = soup.find(name='span', class_='a-price-fraction').getText()
    price = float(price_whole + price_fraction)

    return price


def get_title(text):
    """
       Extracts the title from the HTML content of a product page.

       Args:
           text (str): The HTML content of the product page.

       Returns:
           str: The title of the product.
    """
    soup = BeautifulSoup(text, 'html.parser')
    return soup.find(id='productTitle').getText().strip()


def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
        Sends an email using the specified SMTP server.

        :param sender_email: (str) The sender's email address.
        :param sender_password: (str) The sender's email password.
        :param recipient_email: (str) The recipient's email address.
        :param subject: (str) The subject of the email.
        :param body: (str) The body of the email.
        :return: void
    """
    # Create the email message
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient_email,
                            msg=f'Subject:{subject}\n\n{body}'.encode('utf-8'))
