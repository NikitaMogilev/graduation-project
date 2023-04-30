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



@pytest.fixture()
def login_in(browser):
    user = Authorized_User(browser)
    user.open()
    user.login_in()

