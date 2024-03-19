import time

from selenium import webdriver


def install_driver():
    """Установка драйвера для хром"""
    driver = webdriver.Chrome()
    return driver


def open_browser(install_driver):
    """Открытие старницы"""
    install_driver.get('https://samples.gwtproject.org/samples/Showcase/Showcase.html#!CwCellList')
    time.sleep(5)
