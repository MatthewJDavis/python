""" Checks a couple of sites for the current cost of Wahoo direct trainers."""
import os
import bs4
import requests
from requests import HTTPError

chat_id = os.getenv('CHAT_ID')
token = os.getenv('TOKEN')


CORE_CURRENT_PRICE = 1300
V5_CURRENT_PRICE = 1800
CORE_ID = "product-price-241"
V5_ID = "product-price-363"
BIKE_SHOP_ID = "RegularPrice"
WAHOO_CORE_URL = "https://ca.wahoofitness.com/devices/bike-trainers/kickr-core-indoor-smart-trainer"
WAHOO_V5_URL = "https://ca.wahoofitness.com/devices/bike-trainers/kickr/buy"
BIKE_SHOP_CORE_URL = "https://www.thebikeshop.com/product/wahoo-kickr-core-smart-trainer-365266-1.htm"  # pylint: disable=line-too-long
BIKE_SHOP_V5_URL = "https://www.thebikeshop.com/product/wahoo-kickr-smart-trainer-381240-1.htm"


def process_price(url, site_id, soup_data):
    """ Locate the price with bs4 find and return a price string."""
    if "wahoofitness" in url:
        price = soup_data.find(id=site_id)
        price_string = str(price()[0])
        price_string = price_string.split('CA$')[1]
        price_string = price_string.split('</')[0]
        price_string = price_string.replace(',', '')
    elif "thebikeshop" in url:
        price = soup_data.find(id=site_id)
        price_string = str(price).split('>$')[1]
        price_string = price_string.split("</")[0]
        price_string = price_string.replace(',', '')

    return price_string


def get_price(url, site_id):
    """ Get the webpage and return the section containing the price of the trainer. """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(http_err)

    wahoo_soup = bs4.BeautifulSoup(response.content, "html.parser")
    price = process_price(url, site_id, wahoo_soup)
    return price


def send_telegram(telegram_chat_id, telegram_token, text):
    """ Send message to telegram via the API """
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={telegram_chat_id}&text={text}'  # pylint: disable=line-too-long
    requests.post(url)


def main():
    """ Main entry point."""
    wh_core_price = get_price(WAHOO_CORE_URL, CORE_ID)
    wh_v5_price = get_price(WAHOO_V5_URL, V5_ID)
    bs_core_price = get_price(BIKE_SHOP_CORE_URL, BIKE_SHOP_ID)
    bs_v5_price = get_price(BIKE_SHOP_V5_URL, BIKE_SHOP_ID)

    if float(wh_core_price) < CORE_CURRENT_PRICE:
        pay_load = f"Wahoo price core: {wh_core_price} {WAHOO_CORE_URL}"
        print(pay_load)
        send_telegram(chat_id, token, pay_load)

    if float(wh_v5_price) < V5_CURRENT_PRICE:
        pay_load = f"Wahoo price V5: {wh_v5_price} {WAHOO_V5_URL}"
        print(pay_load)
        send_telegram(chat_id, token, pay_load)

    if float(bs_core_price) < CORE_CURRENT_PRICE:
        pay_load = f"Bike shop price core: {bs_core_price} {BIKE_SHOP_CORE_URL}"
        print(pay_load)
        send_telegram(chat_id, token, pay_load)

    if float(bs_v5_price) < V5_CURRENT_PRICE:
        pay_load = f"Bike shop price V5: {bs_v5_price} {BIKE_SHOP_V5_URL}"
        print(pay_load)
        send_telegram(chat_id, token, pay_load)


if __name__ == "__main__":
    main()
