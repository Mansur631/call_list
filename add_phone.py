import time

import find_elements
from find_elements import PageElements
from options import install_driver
from options import open_browser
from selenium.webdriver.support.ui import WebDriverWait



contact_first_name = page_elements.by_xpath("//div/div/table/tbody/tr[2]/td[2]/input").click()
contact_first_name.send_keys('Alex')


