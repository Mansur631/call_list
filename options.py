from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def install_driver():
    """Установка драйвера для хром"""
    driver = webdriver.Chrome()
    return driver


def open_browser(install_driver) -> WebDriver:
    """Открытие старницы"""
    install_driver.get('https://samples.gwtproject.org/samples/Showcase/Showcase.html#!CwCellList')
    return install_driver
