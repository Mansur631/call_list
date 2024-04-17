from selenium.webdriver.common.keys import Keys

from utils.contacts import get_random_address
from utils.contacts import get_random_birtday
from utils.contacts import get_random_names
from utils.contacts import get_random_surname
from utils.page_elements import PageElements


# page_elements = PageElements()


def test_count_contact_before(open_browser):
    page_elements = PageElements(open_browser)
    all_contact = page_elements.by_selector(
        '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div.gwt-HTML'
    )
    return int(all_contact.text.split(':')[-1].strip())


def test_add_first_name(open_browser):
    page_elements = PageElements(open_browser)
    contact_first_name = page_elements.by_selector(
        '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')
    contact_first_name.click()
    contact_first_name.clear()
    contact_first_name.send_keys(get_random_names())


def test_add_last_name(open_browser):
    page_elements = PageElements(open_browser)
    contact_last_name = page_elements.by_selector(
        '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > input')
    contact_last_name.click()
    contact_last_name.clear()
    contact_last_name.send_keys(get_random_surname())


def test_add_category(open_browser):
    page_elements = PageElements(open_browser)
    contact_category = page_elements.by_selector(
        '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > input')
    contact_category.click()
    contact_category_type = page_elements.by_xpath("//option[text()='Friends']")
    contact_category_type.click()


def test_add_birthday(open_browser):
    page_elements = PageElements(open_browser)
    birthday = page_elements.by_selector(
        "#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(5) > td:nth-child(2) > input"
    )
    # birthday.click()
    birthday.clear()
    birthday.send_keys(get_random_birtday())
    birthday.send_keys(Keys.ENTER)


def test_add_address(open_browser):
    page_elements = PageElements(open_browser)
    address = page_elements.by_selector(
        "#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > textarea"
    )
    address.click()
    address.clear()
    address.send_keys(get_random_address())


def test_add_create_contact(open_browser):
    page_elements = PageElements(open_browser)
    create_contact = page_elements.by_selector(
        "#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(7) > td > button:nth-child(2)"
    )
    create_contact.click()


def test_count_contact_after(open_browser):
    page_elements = PageElements(open_browser)
    all_contact = page_elements.by_selector(
        '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div.gwt-HTML'
    )
    return int(all_contact.text.split(':')[-1].strip())

# count_before = count_contact_before()
#
# functions = [test_add_first_name, test_add_last_name, test_add_category, test_add_birthday, test_add_address, test_add_create_contact]
#
# for _ in range(5):
#     for func in functions:
#         func()
#
#
# count_after = count_contact_after()
# print("Число добавленных контактов:", count_after - count_before)
# # time.sleep(5)
