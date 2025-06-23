import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from pages.login_page import LoginPage

logger = logging.getLogger("qa")


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://berpress.github.io/selenium-login-demo/",
                     help="url")
    parser.addoption("--headless", action="store_true",
                     help="url")


@pytest.fixture(scope="session") # scope="session" позволяет ускорить выполнение тестов
def login_page(request):
    url = request.config.getoption('--url')
    is_headless = request.config.getoption('--headless')
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    if is_headless:
        chrome_options.add_argument("--headless=new")
    logger.info(f'Start app on url {url}, headless is {is_headless}')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    login_page = LoginPage(driver)
    yield login_page
    logger.info(f'Stop tests')
    driver.quit()




