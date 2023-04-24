import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.sign_page import Authorized_User




@pytest.fixture()
def browser():
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome.maximize_window()
    chrome.refresh()
    chrome.maximize_window()
    yield chrome
    chrome.close()


# @pytest.fixture()
# def chromedriver_headless():
#     chromeopt = Options()
#     chromeopt.add_argument("--headless")
#     chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chromeopt)
#     yield chrome
#     chrome.close()


# @pytest.fixture()
# def chromedriver_docker() -> Options:
#     """Sets chrome options for Selenium.
#     Chrome options for headless browser is enabled.
#     """
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=chrome_options)
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()


@pytest.fixture()
def login_in(browser):
    user = Authorized_User(browser)
    user.open()
    user.login_in()

