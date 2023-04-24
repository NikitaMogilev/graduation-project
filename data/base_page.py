# from retrying import retry
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from retrying import retry
from selenium.webdriver.support.select import Select
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from data.data import DataUser


# def random_name_address(self):
#     validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
#     add_char = ''
#     adress_name = 'my address'
#     loginlen = random.randint(1, 3)
#     for i in range(loginlen):
#         pos = random.randint(0, len(validchars) - 1)
#         add_char += validchars[pos]
#     addres = adress_name + add_char
#     return addres


class BasePage:
    def __init__(self, browser: webdriver.Chrome) -> object:
        self.webdriver: webdriver.Chrome = browser
        browser.maximize_window()
        self.url = ''

    def open_url(self, url):
        self.webdriver.get(url)

    def open(self):
        self.open_url(url=DataUser.url)

    def is_exist_check(self, locator: tuple, timer=10):
        try:
            self.webdriver.find_element(locator[0], locator[1]).is_displayed()
            return True
        except NoSuchElementException:
            return False

    def check_title(self):
        return self.webdriver.title

    # def get_url(self):
    #     return self.webdriver.current_url

    def get_atr(self, locator: tuple, atr: str, timer=15):
        element = WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))
        return element.get_attribute(atr)

    def get_list_atr(self, locator_of_list_el: tuple, atr: str, timer=15):
        list_of_atrs = self.find_elements(locator_of_list_el)
        el_atr_text = []
        for el in list_of_atrs:
            text_class = el.get_attribute(atr)
            el_atr_text.append(text_class)
        return el_atr_text

    def selector_by_value(self, locator: tuple, value: str, timer=10):
        element = WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))
        return Select(element).select_by_value(value)

    def selector_by_index(self, locator: tuple, index: str, timer=10):
        element = WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))
        return Select(element).select_by_index(index)

    def selector_by_text(self, locator: tuple, text: str, timer=10):
        element = WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))
        return Select(element).select_by_visible_text(text)

    def find_element(self, locator: tuple, timer=10) -> WebElement:
        return WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timer=30):
        return WebDriverWait(self.webdriver, timer).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator: tuple, timer=20):
        return WebDriverWait(self.webdriver, timer).until(EC.element_to_be_clickable(locator)).click()

    def click_checkbox_or_radio(self, locator: tuple, timer=10):
        element = WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))
        element.click()

    def click_on_drop_down_list(self, locator1: tuple, locator2: tuple) -> object:
        button = WebDriverWait(self.webdriver, 40).until(EC.visibility_of_element_located(locator1))
        hover = ActionChains(self.webdriver).move_to_element(button)
        hover.perform()
        return WebDriverWait(self.webdriver, 40).until(EC.visibility_of_element_located(locator2)).click()

    # def submit_element(self, locator: tuple, timer=10):
    #     return WebDriverWait(self.webdriver, timer).until(EC.element_to_be_clickable(locator)).submit()

    def send_keys(self, locator, content, timer=10):
        input_field = WebDriverWait(self.webdriver, timer).until(EC.element_to_be_clickable(locator))
        input_field.clear()
        input_field.send_keys(content)

    def send_files(self, locator, content, timer=10):
        input_field = WebDriverWait(self.webdriver, timer).until(EC.element_to_be_clickable(locator))
        input_field.send_keys(content)

    def get_text_from_element(self, locator, timer=10):
        element = self.find_element(locator, timer)
        return element.text

    def get_text_from_elements(self, locator, timer=10):
        list_of_element = self.find_elements(locator)
        el_textes = []
        for el in list_of_element:
            text_el = el.text
            el_textes.append(text_el)
        return el_textes

    # def get_list_atr(self, locator_of_list_el: tuple, atr: str, timer=15):
    #     list_of_atrs = self.find_elements(locator_of_list_el)
    #     el_atr_text = []
    #     for el in list_of_atrs:
    #         text_class = el.get_attribute(atr)
    #         el_atr_text.append(text_class)
    #     return el_atr_text

    def switch_to_iframe(self, locator: object, timer=40):
        iframe = self.webdriver.find_element(locator)
        self.webdriver.switch_to.frame(iframe)
        # WebDriverWait(self, timer).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))

    def switch_to_default_context(self):
        self.webdriver.switch_to.default_content()

    # def accept_alert(self):
    #     alert_el = self.webdriver.switch_to.alert
    #     alert_el.accept()
    #     self.switch_to_default_context()
    #
    # def dismiss_alert(self):
    #     alert_el = self.webdriver.switch_to.alert
    #     alert_el.dismiss()
    #     self.switch_to_default_context()
    #
    # def fill_and_accept_alert(self, content):
    #     alert_el = self.webdriver.switch_to.alert
    #     alert_el.send_keys(content)
    #     alert_el.accept()
    #     self.switch_to_default_context()
    #
    # @retry(stop_max_delay=10000)
    # def element_click_with_retry(self, locator, timer=30):
    #     return (
    #         WebDriverWait(self.webdriver, timer).until(
    #             EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}"))
