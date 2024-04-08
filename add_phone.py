from find_elements import PageElements
from contacts import get_random_names
from contacts import get_random_surname
from contacts import get_random_birtday
page_elements = PageElements()


# def add_first_name():
contact_first_name = page_elements.by_selector(
    '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')
contact_first_name.click()
contact_first_name.send_keys(get_random_names())

contact_last_name = page_elements.by_selector(
    '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > input')
contact_last_name.click()
contact_last_name.send_keys(get_random_surname())
#
# contact_category = page_elements.by_selector(
#     '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > input')
# contact_category.click()
# contact_category_type = page_elements.by_xpath("//option[text()='Friends']")
# contact_category_type.click()