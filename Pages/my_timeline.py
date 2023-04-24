import time
from selenium import webdriver
from data.base_page import BasePage
from data.locators import MyTimelineLocator


class MyTimeline(BasePage):

    def __init__(self, browser: webdriver.Chrome, login_in):
        super().__init__(browser)

    def open_close_filters(self):
        time.sleep(10)
        self.click_element(MyTimelineLocator.filter_button)

    def remove_filters(self):
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['forum'])
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['events'])
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['business'])
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['new_members'])
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['classifieds'])
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['jobs'])
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['blogs'])
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['housing'])
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['pictures'])
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['guides'])

    def check_impossible_remove_all_filters(self):
        self.click_element(MyTimelineLocator.filter_save_button)
        warning_text = self.find_element(MyTimelineLocator.warning_filter_message).text
        assert warning_text == "Please select at least one item to display before saving your filters."

    def select_all_filters(self):
        self.click_element(MyTimelineLocator.select_all)
        el_class_text = self.get_list_atr(MyTimelineLocator.all_checkboxes, "class")
        for text in el_class_text:
            assert text == "icheckbox_flat-green checked"

    def checkbox_filters_check(self):
        self.open_close_filters()
        self.click_element(MyTimelineLocator.select_all)
        self.remove_filters()
        for key in MyTimelineLocator.dict_checkboxes:
            self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes[key])
            self.click_element(MyTimelineLocator.filter_save_button)
            time.sleep(10)
            if self.find_element(MyTimelineLocator.first_article).is_displayed():
                data_type_articles = self.get_list_atr(MyTimelineLocator.timeline_list, 'data-type')
                el = None
                while el in data_type_articles:
                    data_type_articles.remove(el)
                assert all(x == data_type_articles[0] or None for x in data_type_articles)
                time.sleep(8)
                self.open_close_filters()
                self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes[key])
            else:
                print(f"No such articles{key}")
                self.open_close_filters()
                self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes[key])
                continue

    def chose_filters_without_members(self):
        self.open_close_filters()
        self.select_all_filters()
        self.click_checkbox_or_radio(MyTimelineLocator.dict_checkboxes['new_members'])
        self.click_element(MyTimelineLocator.filter_save_button)
        time.sleep(5)

    def check_link_avatars(self):
        redirect_list = self.get_list_atr(MyTimelineLocator.list_avatars, 'href')
        redirection_link = 'https://www.expat.com/' \
                           'redirect.php?href=https%3A%2F%2Fwww.expat.com%2Fforum%2Fprofile.php%3Fid%'
        quantity = len(redirection_link)
        for el in redirect_list:
            assert el[0:quantity] == redirection_link
