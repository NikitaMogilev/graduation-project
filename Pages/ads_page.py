import time
from selenium import webdriver
from data.base_page import BasePage
from data.locators import HeadLineLocators
from data.locators import AdsLocators
from data.data import DataUser
import os
import allure


class Ads(BasePage):

    def __init__(self, browser: webdriver.Chrome, login_in):
        super().__init__(browser)

    def open_ads_page(self):
        self.click_element(HeadLineLocators.classifieds)

    def post_your_ads(self):
        return self.click_element(AdsLocators.post_add)

    @allure.step('Check categories and subcategories')
    def check_categories(self):
        for key in AdsLocators.categories:
            self.click_element(AdsLocators.categories[key])
            parent_category_expect = self.get_atr(AdsLocators.categories[key], 'data-parent-category')
            allure.attach(f'{(key, parent_category_expect)}', name='Name of category and its data number')
            parent_category_actual = self.get_atr(AdsLocators.list_subcategory, 'data-parent-category')
            allure.attach(parent_category_actual, name='Data number of the list subcategory')
            assert parent_category_actual == parent_category_expect

    def fill_category(self):
        self.click_element(AdsLocators.categories['activities'])
        self.click_element(AdsLocators.sport_partner)

    @allure.step('Fill basic info in ADs')
    def basic_info(self):
        time.sleep(5)
        with allure.step('Click type of Ads Offer or Search'):
            self.click_checkbox_or_radio(AdsLocators.type_of_ad)
        with allure.step('Click your status'):
            self.click_checkbox_or_radio(AdsLocators.your_status)
        with allure.step('Chose currency'):
            self.selector_by_text(AdsLocators.currency_selector, '(USD) United States dollar $')
        with allure.step('Choose price'):
            self.send_keys(AdsLocators.price_value, f'{DataUser.price_for_ads}')
        with allure.step('Are ypu ready to negotiate'):
            self.click_checkbox_or_radio(AdsLocators.negotiable_no)
        with allure.step('Chose date till which your Ads is valid '):
            self.click_element(AdsLocators.calendar)
            self.click_element(AdsLocators.valid_for_today)
        with allure.step('Put title of your Ads'):
            self.send_keys(AdsLocators.title_ad, DataUser.title_ad)
        with allure.step('Switch to iframe of Description and make it'):
            frame = self.find_element(AdsLocators.description_frame)
            self.webdriver.switch_to.frame(frame)
            self.send_keys(AdsLocators.description, DataUser.ads_description)
        with allure.step('Switch to default context'):
            self.switch_to_default_context()
        with allure.step('Chose auto-translation option to Spanish'):
            self.click_checkbox_or_radio(AdsLocators.autotranslation_button_yes)
            self.click_checkbox_or_radio(AdsLocators.spanish_lang)

    def chose_location(self):
        self.selector_by_text(AdsLocators.ads_country_selector, 'Vietnam')
        self.send_keys(AdsLocators.city_sellector, f'{DataUser.ad_city}')
        time.sleep(5)
        self.click_element(AdsLocators.click_city)

    def chose_wrong_location(self):
        self.selector_by_text(AdsLocators.ads_country_selector, 'Vietnam')
        self.send_keys(AdsLocators.city_sellector, f'{DataUser.ad_incorrect_city}')

    def upload_foto(self):
        absolute_path = os.path.abspath('foto_for_upload.jpg')
        self.send_files(AdsLocators.upload_field, absolute_path)

    @allure.step('Put User name, Phone and email')
    def right_contacts(self):
        self.send_keys(AdsLocators.contact_name, DataUser.name_for_ad)
        self.send_keys(AdsLocators.phone_number, DataUser.phone_number)
        self.send_keys(AdsLocators.email, DataUser.right_login)

    def add_my_classified(self):
        self.click_element(AdsLocators.add_button)

    def success_check(self):
        success_message = self.is_exist_check(AdsLocators.success_message)
        allure.attach(success_message, name="Success message")
        assert success_message

    def error_check_message(self):
        error_message = self.get_text_from_element(AdsLocators.error_message)
        assert self.is_exist_check(AdsLocators.error_message)
        print(error_message)
