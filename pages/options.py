from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.config import BASE_URL


def install_driver():
    """Установка драйвера для хром"""
    driver = webdriver.Chrome()
    return driver


def open_browser(install_driver) -> WebDriver:
    """Открытие старницы"""
    install_driver.get(BASE_URL)
    return install_driver
