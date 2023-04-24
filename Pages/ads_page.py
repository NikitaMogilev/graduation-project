import time
from selenium import webdriver
from data.base_page import BasePage
from data.locators import HeadLineLocators
from data.locators import AdsLocators
from data.data import DataUser
import os


class Ads(BasePage):

    def __init__(self, browser: webdriver.Chrome, login_in):
        super().__init__(browser)

    def open_ads_page(self):
        self.click_element(HeadLineLocators.classifieds)

    def post_your_ads(self):
        return self.click_element(AdsLocators.post_add)

    def check_categories(self):
        for key in AdsLocators.categories:
            self.click_element(AdsLocators.categories[key])
            parent_category_expect = self.get_atr(AdsLocators.categories[key], 'data-parent-category')
            parent_category_actual = self.get_atr(AdsLocators.list_subcategory, 'data-parent-category')
            assert parent_category_actual == parent_category_expect

    def fill_category(self):
        self.click_element(AdsLocators.categories['activities'])
        self.click_element(AdsLocators.sport_partner)

    def basic_info(self):
        time.sleep(5)
        self.click_checkbox_or_radio(AdsLocators.type_of_ad)
        self.click_checkbox_or_radio(AdsLocators.your_status)
        self.selector_by_text(AdsLocators.currency_selector, '(USD) United States dollar $')
        self.send_keys(AdsLocators.price_value, f'{DataUser.price_for_ads}')
        self.click_checkbox_or_radio(AdsLocators.negotiable_no)
        self.click_element(AdsLocators.calendar)
        self.click_element(AdsLocators.valid_for_today)
        self.send_keys(AdsLocators.title_ad, DataUser.title_ad)
        fr = self.find_element(AdsLocators.description_frame)
        self.webdriver.switch_to.frame(fr)
        self.send_keys(AdsLocators.description, DataUser.ads_description)
        self.switch_to_default_context()
        self.click_checkbox_or_radio(AdsLocators.autotranslation_button_yes)
        self.click_checkbox_or_radio(AdsLocators.spanish_lang)

    def chose_location(self):
        self.selector_by_text(AdsLocators.ads_country_selector, 'Vietnam')
        self.send_keys(AdsLocators.city_sellector, f'{DataUser.ad_city}')
        time.sleep(5)
        self.click_element(AdsLocators.click_city)
        # auto_chose = self.find_element(AdsLocators.click_city)
        # auto_chose.click()

    def chose_wrong_location(self):
        self.selector_by_text(AdsLocators.ads_country_selector, 'Vietnam')
        self.send_keys(AdsLocators.city_sellector, f'{DataUser.ad_incorrect_city}')

    def upload_foto(self):
        absolute_path = os.path.abspath('foto_for_upload.jpg')
        self.send_files(AdsLocators.upload_field, absolute_path)

    def right_contacts(self):
        self.send_keys(AdsLocators.contact_name, DataUser.name_for_ad)
        self.send_keys(AdsLocators.phone_number, DataUser.phone_number)
        self.send_keys(AdsLocators.email, DataUser.right_login)

    def add_my_classified(self):
        self.click_element(AdsLocators.add_button)

    def success_check(self):
        success_message = self.is_exist_check(AdsLocators.success_message)
        assert success_message, 'ADD CLASSIFIED CANNT COMPLETE, last button is not working'
        # success_message = self.get_text_from_element(AdsLocators.success_message)
        # assert 'We have received your ad' in success_message, 'ADD CLASSIFIED CANNT COMPLETE'

    def error_check_message(self):
        error_message = self.get_text_from_element(AdsLocators.error_message)
        assert self.is_exist_check(AdsLocators.error_message)
        print(error_message)
