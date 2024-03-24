from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from options import install_driver
from options import open_browser


class PageElements:
    def __init__(self):
        self.driver = open_browser(install_driver())

    def by_id(self, element_id):
        return self.driver.find_element(By.ID, element_id)

    def by_class_name(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def by_xpath(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        self.driver.refresh()
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element

    def by_name(self, name):
        return self.driver.find_element(By.NAME, name)

    def by_text(self, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def by_selector(self, selector):
        wait = WebDriverWait(self.driver, 10)
        self.driver.refresh()
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        return element
