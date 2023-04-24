import time
from selenium import webdriver
from data.base_page import BasePage
from data.locators import HeadLineLocators
from data.locators import PictureLocator
from data.locators import BlogLocators
from data.data import DataUser


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

    def check_blogs_about_choosen_country(self):
        list_blogs = self.get_list_atr(BlogLocators.list_blogs, 'class')
        for blog in list_blogs:
            if DataUser.country_for_blog.lower() in blog:
                self.result = 1
            else:
                self.result = 0
        assert self.result == 1

    def send_wrong_keys_in_country(self):
        self.click_element(BlogLocators.drop_country_box)
        self.send_keys(BlogLocators.input_country_choice, '54')
        self.click_element(BlogLocators.ok_button)
        alert = self.get_text_from_element(BlogLocators.alert_message)
        assert alert == "Please select at least one criteria for your search"

    def choose_blog(self):
        return self.click_element(BlogLocators.any_blog)

    def make_comment_under_blog_story(self):
        self.send_keys(BlogLocators.comment_filed, DataUser.comment_for_blog)
        self.click_element(BlogLocators.comment_submit_button)
        time.sleep(5)
        my_comment = self.get_text_from_element(BlogLocators.my_comment)
        assert my_comment == DataUser.comment_for_blog

    def commentator_name(self):
        nick = self.get_text_from_element(BlogLocators.commentator_nick)
        assert nick in DataUser.right_login

    def upt_comment_under_blog_story(self):
        self.click_element(BlogLocators.options_list)
        self.click_element(BlogLocators.edit_button)
        self.send_keys(BlogLocators.edit_comment_field, DataUser.upt_comment_for_blog)
        self.click_element(BlogLocators.comment_submit_button)
        new_comment = self.get_text_from_element(BlogLocators.my_comment)
        assert new_comment == DataUser.upt_comment_for_blog

    def del_comment(self):
        self.click_element(BlogLocators.options_list)
        self.click_element(BlogLocators.delete_button)

