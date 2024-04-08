import time
from selenium.webdriver.common.keys import Keys

from find_elements import PageElements
from contacts import get_random_names
from contacts import get_random_surname
from contacts import get_random_birtday
from contacts import get_random_address

page_elements = PageElements()


def add_first_name():
    contact_first_name = page_elements.by_selector(
        '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')
    contact_first_name.click()
    contact_first_name.send_keys(get_random_names())


def add_last_name():
    contact_last_name = page_elements.by_selector(
        '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > input')
    contact_last_name.click()
    contact_last_name.send_keys(get_random_surname())


def add_category():
    contact_category = page_elements.by_selector(
        '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > input')
    contact_category.click()
    contact_category_type = page_elements.by_xpath("//option[text()='Friends']")
    contact_category_type.click()


def add_birthday():
    birthday = page_elements.by_selector(
        "#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(5) > td:nth-child(2) > input"
    )
    # birthday.click()
    birthday.send_keys(get_random_birtday())
    birthday.send_keys(Keys.ENTER)


def add_address():
    address = page_elements.by_selector(
        "#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > textarea"
    )
    address.click()
    address.send_keys(get_random_address())


add_first_name()
add_last_name()
add_category()
add_birthday()
add_address()
time.sleep(5)