from selenium.webdriver.common.by import By

import options
from options import install_driver


class PageElements:
    def __init__(self):
        self.driver = install_driver()

    def by_id(self, element_id):
        return self.driver.find_element(By.ID, element_id)

    def by_class_name(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def by_name(self, name):
        return self.driver.find_element(By.NAME, name)


# page_elements = PageElements()
# contact_first_name = page_elements.by_xpath("//div/div/table/tbody/tr[2]/td[2]/input")
# contact_first_name.click()
# contact_first_name.send_keys('Alex')