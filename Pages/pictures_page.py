from selenium import webdriver
from data.base_page import BasePage
from data.locators import HeadLineLocators
from data.locators import PictureLocator
from data.data import DataUser


class PicturePage(BasePage):

    def __init__(self, browser: webdriver.Chrome, login_in):
        super().__init__(browser)

    def open_picture_page(self):
        self.click_on_drop_down_list(HeadLineLocators.community, HeadLineLocators.pictures)

    def world_around_click(self):
        if self.is_exist_check(PictureLocator.world_but):
            self.click_element(PictureLocator.world_but)
        else:
            pass

    def chose_country(self):
        self.selector_by_text(PictureLocator.country_selector, f'{DataUser.country_for_picture}')
        self.click_element(PictureLocator.ok_button)

    def name_chosen_country(self):
        country_name = self.get_text_from_element(PictureLocator.title_country)
        if country_name == 'Expat life in pictures':
            print('BAG, when user log, should shown country which user choose when do registration')
        else:
            assert country_name == f'Pictures of {DataUser.country_for_picture}'

    def send_wrong_keys_in_country(self):
        self.click_element(PictureLocator.drop_country_box)
        self.send_keys(PictureLocator.input_country_choice, '54')
        self.click_element(PictureLocator.ok_button)
        alert = self.get_text_from_element(PictureLocator.alert_message)
        assert alert == "Please select at least one criteria for your search"




