from find_elements import PageElements

page_elements = PageElements()
contact_first_name = page_elements.by_selector(
    '#gwt-debug-contentPanel > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > table > tbody > tr:nth-child(1) > td.CMWVMEC-p-a > table > tbody > tr.middle > td.middleCenter > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')
contact_first_name.click()
contact_first_name.send_keys('Alex')

