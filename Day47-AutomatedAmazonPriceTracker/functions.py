import requests
from bs4 import BeautifulSoup
import smtplib


def get_response(url):
    """
        Fetches the HTML content of the given URL.

        Args:
            url (str): The URL of the webpage to fetch.

        Returns:
            str: The HTML content of the webpage.
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',

    }
    cookies = {
        'csm-hit': 'tb:Q5595GW5G4JK2MKB74EZ+s-EP1K8QT136Z603YTRTT2|1735118057912&t:1735118057912&adb:adblk_yes',
        'session-id': '143-5688308-2285545',
        'session-id-time': '2082787201l',
        'session-token': 'z7AnKSNZIvA7GiZyGKHu8MRr53frq4VN4+FI9ukgB5Ab9HCtoYWm1H90wBMEgZbYu/j1Zs8ZlG3k8bCsXHNturEWBX8K0mKn6JEU6D9JQlkrppbS/N3i+msrCNJDfocDXGKqWf2LdMymPjJUoI1qSNeynv44HB/Qz3ouYgfMZcjDB66gUnY2o4wrryzVNpgtJ4tgIf47hOqKg2t29Ct0xK6Z8ZRVkvrHHUj+SeAE6DeDmv/v3GgTPuJ41GiliiyZbQbLRNvXTvJAMNGm9Pd+erKTTdoQulTJBujY+VRDJBtyU3E8R5hM/0f2D+qa8bn8ytRI8KbcvWOvWbxq7RNNYKFk3fPNEZ7R',
        'ubid-main': '132-1017929-4852164',
        'i18n-prefs': 'USD',
    }
    response = requests.get(url, headers=headers, cookies=cookies)
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
    # print(soup.prettify())
    price = soup.find(name='span', class_='a-offscreen')
    price = float(price[1:])

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
