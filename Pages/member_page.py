import time
from selenium import webdriver
from data.base_page import BasePage
from data.locators import HeadLineLocators
from data.locators import MembersLocator
from data.data import DataUser
from data.custom_exeptions import UserInfoError


class MemberPage(BasePage):

    def __init__(self, browser: webdriver.Chrome, login_in):
        super().__init__(browser)

    def open_member_page(self):
        self.click_on_drop_down_list(HeadLineLocators.community, HeadLineLocators.members)

    def wrong_data(self):
        self.click_element(MembersLocator.destination_click)
        self.send_keys(MembersLocator.destination_input, DataUser.wrong_country)
        error = self.get_text_from_element(MembersLocator.wrong_destination_message)
        assert error == 'No results found'
        self.click_element(MembersLocator.nationality_click)
        self.send_keys(MembersLocator.destination_input, DataUser.wrong_nationality)
        error = self.get_text_from_element(MembersLocator.wrong_nationality_message)
        assert error == 'No results found'

    def fill_select_data(self):
        self.selector_by_text(MembersLocator.destination, DataUser.country_for_members)
        self.selector_by_text(MembersLocator.nationality, DataUser.nationality)
        self.selector_by_index(MembersLocator.age, '3')
        self.selector_by_index(MembersLocator.status, '1')
        self.selector_by_index(MembersLocator.gender, '1')
        self.selector_by_index(MembersLocator.professional_status, '3')
        self.selector_by_text(MembersLocator.language, 'English')
        self.selector_by_index(MembersLocator.online, '1')
        self.click_element(MembersLocator.search_button)
        time.sleep(5)

    def check_filter_users(self):
        self.click_element(MembersLocator.user_inside_button)
        time.sleep(10)
        actual_nationality = self.get_text_from_element(MembersLocator.user_nationality)
        assert DataUser.nationality in actual_nationality

    def user_info_in_user_list(self):
        list_of_info = self.get_text_from_elements(MembersLocator.list_users)
        for el in list_of_info:
            if el == '':
                raise UserInfoError("No USER Info under avatar")
            else:
                pass

    def search_by_nick_name(self):
        return print('No Search Field By NickName')
