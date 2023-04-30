import time
from selenium import webdriver
from data.base_page import BasePage
from data.locators import HeadLineLocators
from data.locators import MembersLocator
from data.data import DataUser
from data.custom_exeptions import UserInfoError
import allure


class MemberPage(BasePage):

    def __init__(self, browser: webdriver.Chrome, login_in):
        super().__init__(browser)

    def open_member_page(self):
        self.click_on_drop_down_list(HeadLineLocators.community, HeadLineLocators.members)

    @allure.step('Write in country and nationality some number and check error message')
    def wrong_data(self):
        self.click_element(MembersLocator.destination_click)
        self.send_keys(MembersLocator.destination_input, DataUser.wrong_country)
        error = self.get_text_from_element(MembersLocator.wrong_destination_message)
        assert error == 'No results found'
        self.click_element(MembersLocator.nationality_click)
        self.send_keys(MembersLocator.destination_input, DataUser.wrong_nationality)
        error = self.get_text_from_element(MembersLocator.wrong_nationality_message)
        assert error == 'No results found'

    @allure.step('Fill correct data in search fields')
    def fill_select_data(self):
        with allure.step('Choose country'):
            self.selector_by_text(MembersLocator.destination, DataUser.country_for_members)
        with allure.step('Choose nationality'):
            self.selector_by_text(MembersLocator.nationality, DataUser.nationality)
        with allure.step('Choose age interval'):
            self.selector_by_index(MembersLocator.age, '3')
        with allure.step('Choose expat status'):
            self.selector_by_index(MembersLocator.status, '1')
        with allure.step('Choose ex[at gender'):
            self.selector_by_index(MembersLocator.gender, '1')
        with allure.step('Choose expat professional status'):
            self.selector_by_index(MembersLocator.professional_status, '3')
        with allure.step('Choose expat language'):
            self.selector_by_text(MembersLocator.language, 'English')
        with allure.step('Choose status on site online/offline'):
            self.selector_by_index(MembersLocator.online, '1')
        with allure.step('Click search button'):
            self.click_element(MembersLocator.search_button)
            time.sleep(5)

    @allure.step('Check search filter by nationality')
    def check_filter_users(self):
        with allure.step('Click and redirect to page of any user'):
            self.click_element(MembersLocator.user_inside_button)
        time.sleep(10)
        with allure.step('Check that chosen nationality matches with nationality in user page '):
            actual_nationality = self.get_text_from_element(MembersLocator.user_nationality)
            allure.attach(actual_nationality, name='Actual User nationality')
            assert DataUser.nationality in actual_nationality

    @allure.step('Check info under user avatar')
    def user_info_in_user_list(self):
        list_of_info = self.get_text_from_elements(MembersLocator.list_users)
        for el in list_of_info:
            if el == '':
                raise UserInfoError("No USER Info under avatar")
            else:
                pass

    @allure.step('NO POSSIBILITY TO REALIZE THIS FUNCTION')
    def search_by_nick_name(self):
        return print('No Search Field By NickName')
