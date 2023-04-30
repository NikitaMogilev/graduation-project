import time
from selenium import webdriver
import random
from data.base_page import BasePage
from data.locators import RegPageLocators
from data.data import DataUser
import allure


class Sign_Page(BasePage):

    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.user_email = DataUser.random_mail(self)
        self.pseudo = f'tester{random.randrange(1, 100, 1)}'

    def wrong_email_input(self):
        self.send_keys(locator=RegPageLocators.reg_email, content=DataUser.login_without_a)
        self.click_element(RegPageLocators.create_account_button)
        assert RegPageLocators.message_error_reg.text == 'This email address is not valid.'
        self.send_keys(locator=RegPageLocators.reg_email, content=DataUser.login_rus_symbols)
        self.click_element(RegPageLocators.create_account_button)
        assert RegPageLocators.message_error_reg.text == 'This email address is not valid.'

    def check_login_page(self):
        title = self.check_title()
        assert title == 'Expat.com, the expatriate community'

    def click_sign_up(self):
        self.click_element(RegPageLocators.sign_up)

    def new_user_email_input(self):
        self.send_keys(locator=RegPageLocators.reg_email, content=self.user_email)
        self.click_element(RegPageLocators.create_account_button)

    @allure.step('Input login which was registered')
    def authorized_email_input_in_reg(self):
        self.send_keys(locator=RegPageLocators.reg_email, content=DataUser.right_login)
        self.click_element(RegPageLocators.create_account_button)
        with allure.step('Check impossibility same login register'):
            assert self.is_exist_check(RegPageLocators.twice_reg_message)

    def pseudo_and_password(self):
        self.send_keys(RegPageLocators.pseudo_field, self.pseudo)
        self.send_keys(RegPageLocators.password_field, DataUser.password)
        self.click_element(RegPageLocators.pseudo_submit_but)
        error_message = self.find_element(RegPageLocators.error_without_checkbox)
        assert error_message.is_displayed()
        self.click_element(RegPageLocators.conditions_checkbox_expat)
        self.click_element(RegPageLocators.pseudo_submit_but)

    def cookie_button_click(self):
        if self.is_exist_check(RegPageLocators.cookie_button):
            self.click_element(RegPageLocators.cookie_button)
        else:
            pass

    def fill_my_info(self):
        self.send_keys(RegPageLocators.interested_destination_field, DataUser.logined_user_country)
        time.sleep(5)
        self.click_element(RegPageLocators.click_interest)
        self.click_element(RegPageLocators.expat_selector)
        self.click_element(RegPageLocators.expat_status)
        self.click_element(RegPageLocators.nationality_selector)
        self.click_element(RegPageLocators.nationality)
        self.click_element(RegPageLocators.confirm_button)
        time.sleep(10)

    def look_intro(self):
        self.click_element(RegPageLocators.start_tour_button)
        assert self.find_element(RegPageLocators.title2).text == 'Filters'
        self.click_element(RegPageLocators.next_button)
        assert self.find_element(RegPageLocators.title3).text == 'Type of post'
        self.click_element(RegPageLocators.next_button)
        assert self.find_element(RegPageLocators.title4).text == 'Save'
        self.click_element(RegPageLocators.next_button)
        assert self.find_element(RegPageLocators.title5).text == 'More options'
        self.click_element(RegPageLocators.next_button)
        assert self.find_element(RegPageLocators.title6).text == 'Hide a post'
        self.click_element(RegPageLocators.prev_button)
        assert self.find_element(RegPageLocators.title5).text == 'More options'
        self.click_element(RegPageLocators.prev_button)
        assert self.find_element(RegPageLocators.title4).text == 'Save'
        self.click_element(RegPageLocators.prev_button)
        assert self.find_element(RegPageLocators.title3).text == 'Type of post'
        self.click_element(RegPageLocators.prev_button)
        assert self.find_element(RegPageLocators.title2).text == 'Filters'
        self.click_element(RegPageLocators.prev_button)
        assert self.find_element(RegPageLocators.title1).text == 'Browse your timeline'
        self.click_element(RegPageLocators.start_tour_button)
        self.click_element(RegPageLocators.next_button)
        self.click_element(RegPageLocators.next_button)
        self.click_element(RegPageLocators.next_button)
        self.click_element(RegPageLocators.next_button)
        self.click_element(RegPageLocators.i_got_it_button)

    def check_verification(self):
        avatar_name = self.get_atr(RegPageLocators.avatar_img_button, 'alt')
        assert avatar_name == self.pseudo

    def delete_user(self):
        self.click_element(RegPageLocators.user_logo_button)
        self.click_element(RegPageLocators.user_settings)
        self.click_element(RegPageLocators.del_account_button)
        self.click_element(RegPageLocators.del_account_button_V)
        deleting_progress = self.find_element(RegPageLocators.info_del_message)
        assert deleting_progress == 'Account deletion pending'


class Authorized_User(BasePage):
    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)

    @allure.step('Login with right data')
    def login_in(self):
        with allure.step(' Click LOGIN button'):
            self.click_element(RegPageLocators.login_button)
        with allure.step('Input right login and password'):
            self.send_keys(RegPageLocators.username_field, DataUser.right_login)
            self.send_keys(RegPageLocators.authorized_password_field, DataUser.password)
        with allure.step(' Click submit button'):
            self.click_element(RegPageLocators.login_button1)

    @allure.step('Input login without @')
    def wrong_authorization_without_a(self):
        with allure.step(' Click LOGIN button'):
            self.click_element(RegPageLocators.login_button)
        with allure.step('Input email without @'):
            self.send_keys(locator=RegPageLocators.username_field, content=DataUser.login_without_a)
        with allure.step('Input password'):
            self.send_keys(RegPageLocators.authorized_password_field, DataUser.password)
        with allure.step('Click Submit button'):
            self.click_element(RegPageLocators.login_button1)
        with allure.step('Check error message'):
            assert self.get_text_from_element(RegPageLocators.login_error) == 'Wrong username and/or password.' \
                   or 'No user with specified username / email has been found'

    @allure.step('Input login in russian and not input password')
    def wrong_authorization_rus_symbols_and_no_psw(self):
        with allure.step(' Click LOGIN button'):
            self.click_element(RegPageLocators.login_button)
        with allure.step('Input email in russian'):
            self.send_keys(locator=RegPageLocators.username_field, content=DataUser.login_rus_symbols)
        with allure.step('Click Submit button'):
            self.click_element(RegPageLocators.login_button1)
        with allure.step('Check error message'):
            assert self.get_text_from_element(RegPageLocators.login_error) == 'Wrong username and/or password.' \
                   or 'No user with specified username / email has been found'

    @allure.step('Input login in russian and not input password')
    def wrong_password(self):
        with allure.step(' Click LOGIN button'):
            self.click_element(RegPageLocators.login_button)
        with allure.step('Input right email'):
            self.send_keys(locator=RegPageLocators.username_field, content=DataUser.right_login)
        with allure.step('Input wrong password'):
            self.send_keys(RegPageLocators.authorized_password_field, DataUser.wrong_psw)
        with allure.step('Click submit button'):
            self.click_element(RegPageLocators.login_button1)
        with allure.step('Check error message'):
            assert self.get_text_from_element(RegPageLocators.login_error) == 'Wrong username and/or password.' \
                   or 'No user with specified username / email has been found'

    @allure.step('Exit from authorized user')
    def exit_from_account(self):
        with allure.step('Click on logo button and click logout'):
            self.click_element(RegPageLocators.user_logo_button)
            self.click_element(RegPageLocators.logout_button)
        with allure.step('Check page by displaying again SIGN UP '):
            assert self.is_exist_check(RegPageLocators.sign_up)
