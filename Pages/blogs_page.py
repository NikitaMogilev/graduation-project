import time
from selenium import webdriver
from data.base_page import BasePage
from data.locators import HeadLineLocators
from data.locators import PictureLocator
from data.locators import BlogLocators
from data.data import DataUser
import allure


class BlogsPage(BasePage):

    def __init__(self, browser: webdriver.Chrome, login_in):
        super().__init__(browser)

    def open_blogs_page(self):
        self.click_on_drop_down_list(HeadLineLocators.community, HeadLineLocators.blogs)

    def world_around_click(self):
        if self.is_exist_check(BlogLocators.world_field):
            self.click_element(BlogLocators.world_field)
        else:
            pass

    def chose_country(self):
        self.selector_by_text(PictureLocator.country_selector, f'{DataUser.country_for_blog}')
        self.click_element(PictureLocator.ok_button)

    @allure.step('Test which sort blogs by country')
    def check_blogs_about_choosen_country(self):
        with allure.step('Formed list of all blogs on page'):
            list_blogs = self.get_list_atr(BlogLocators.list_blogs, 'class')
            with allure.step('Iterate all values and check if chosen country in all list of blogs,test passed'):
                for blog in list_blogs:
                    if DataUser.country_for_blog.lower() in blog:
                        result = 1
                    else:
                        result = 0
                assert result == 1

    @allure.step('Send in country field some numbers')
    def send_wrong_keys_in_country(self):
        with allure.step('Click on drop box to chose country'):
            self.click_element(BlogLocators.drop_country_box)
        with allure.step('Write in find field number'):
            self.send_keys(BlogLocators.input_country_choice, '54')
        with allure.step('Click OK with numbers instead right country name'):
            self.click_element(BlogLocators.ok_button)
        alert = self.get_text_from_element(BlogLocators.alert_message)
        allure.attach(alert, name='Text of alert which will shown after incorrect country name')
        with allure.step('Check alert message'):
            assert alert == "Please select at least one criteria for your search"

    def choose_blog(self):
        return self.click_element(BlogLocators.any_blog)

    @allure.step('Make comment under some blog')
    def make_comment_under_blog_story(self):
        with allure.step('Write comment and click post'):
            self.send_keys(BlogLocators.comment_filed, DataUser.comment_for_blog)
            self.click_element(BlogLocators.comment_submit_button)
        time.sleep(5)
        with allure.step('Check that posted comment is displayed'):
            my_comment = self.get_text_from_element(BlogLocators.my_comment)
            allure.attach(my_comment, name='My Comment')
            assert my_comment == DataUser.comment_for_blog

    @allure.step('Check the commentator name')
    def commentator_name(self):
        nick = self.get_text_from_element(BlogLocators.commentator_nick)
        allure.attach(nick, name='Commentator Name')
        assert nick in DataUser.right_login

    @allure.step('Update comment')
    def upt_comment_under_blog_story(self):
        with allure.step('Click edit comment'):
            self.click_element(BlogLocators.options_list)
            self.click_element(BlogLocators.edit_button)
        with allure.step('Write new comment and submit'):
            self.send_keys(BlogLocators.edit_comment_field, DataUser.upt_comment_for_blog)
            self.click_element(BlogLocators.comment_submit_button)
        with allure.step('Check that updated comment is displayed'):
            new_comment = self.get_text_from_element(BlogLocators.my_comment)
            allure.attach(new_comment, name='Updated comment')
            assert new_comment == DataUser.upt_comment_for_blog

    @allure.step('Remove comment')
    def del_comment(self):
        self.click_element(BlogLocators.options_list)
        self.click_element(BlogLocators.delete_button)
