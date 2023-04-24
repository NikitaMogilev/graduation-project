import time
from selenium import webdriver
from data.base_page import BasePage
from data.locators import RegPageLocators
from data.locators import HeadLineLocators
from data.locators import EventsLocators
from data.data import DataUser


class EventPage(BasePage):

    def __init__(self, browser: webdriver.Chrome, login_in):
        super().__init__(browser)

    def open_event_page(self):
        self.click_on_drop_down_list(HeadLineLocators.community, HeadLineLocators.events)
        assert self.check_title() == 'Events in Vietnam'

    def click_post_event(self):
        self.click_element(EventsLocators.post_event_button)
        assert self.check_title() == 'Vietnam events: post your event'

    def fill_data_for_event(self, title: object = DataUser.event_title,
                            description: object = DataUser.event_description,
                            venue: object = DataUser.event_venue) -> object:
        self.selector_by_index(EventsLocators.category_selector, '3')
        self.send_keys(EventsLocators.title_event, title)
        self.send_keys(EventsLocators.description_event, description)
        self.selector_by_value(EventsLocators.event_privacy_selector, '3')
        self.send_keys(EventsLocators.event_venue, venue)
        self.click_element(EventsLocators.calendar_start)
        self.click_element(EventsLocators.date_event_beginning)
        self.click_element(EventsLocators.hour_event_beginning)
        self.click_element(EventsLocators.minute_event_beginning)
        self.click_element(EventsLocators.event_submit_button)
        assert self.get_text_from_element(EventsLocators.title_event_for_assert) == title
        assert self.get_text_from_element(EventsLocators.venue_event_for_assert) == venue + ','

    def enter_in_event(self):
        self.click_element(RegPageLocators.user_logo_button)
        self.click_element(RegPageLocators.user_menu_event)
        self.click_element(EventsLocators.event_in_user_menu_button)

    def update_event(self, title=f'{DataUser.upt_event_title}',
                     description=DataUser.upt_event_description,
                     venue=DataUser.upt_event_venue):
        self.click_element(EventsLocators.edit_button)
        self.fill_data_for_event(title, description, venue)

    def cancel_event(self, cancel_reason=DataUser.cancel_reason):
        self.click_element(EventsLocators.cancel_button)
        self.send_keys(EventsLocators.cancel_reason, cancel_reason)
        self.click_element(EventsLocators.cancel_event_button)
        assert self.get_text_from_element(EventsLocators.cancel_message) == f'Event cancelled: {cancel_reason}'

    def go_to_other_event(self):
        self.click_element(EventsLocators.asia_field)
        name_event = self.find_element(EventsLocators.upcoming_event).text
        self.click_element(EventsLocators.upcoming_event)
        assert name_event == self.get_text_from_element(EventsLocators.title_event_for_assert)

    def maybe_decline_check_button(self):

        if self.is_exist_check(EventsLocators.decline_button):
            self.click_element(EventsLocators.decline_button)
            time.sleep(3)
            maybe_count_before: str = self.get_text_from_element(EventsLocators.maybe_count)
            self.click_element(EventsLocators.maybe_button)
            time.sleep(3)
        else:
            maybe_count_before: str = self.get_text_from_element(EventsLocators.maybe_count)
            self.click_element(EventsLocators.maybe_button)
            time.sleep(3)
        maybe_count_after: str = self.get_text_from_element(EventsLocators.maybe_count)
        assert int(maybe_count_after) == int(maybe_count_before) + 1
        self.click_element(EventsLocators.decline_button)
        time.sleep(3)
        maybe_count_after: str = self.get_text_from_element(EventsLocators.maybe_count)
        assert int(maybe_count_after) == int(maybe_count_before)

    def join_decline_check_button(self):

        if self.is_exist_check(EventsLocators.decline_button):
            self.click_element(EventsLocators.decline_button)
            time.sleep(3)
            join_count_before: str = self.get_text_from_element(EventsLocators.join_count)
            self.click_element(EventsLocators.join_button)
            time.sleep(3)
        else:
            join_count_before: str = self.get_text_from_element(EventsLocators.join_count)
            self.click_element(EventsLocators.join_button)
            time.sleep(3)
        join_count_after: str = self.get_text_from_element(EventsLocators.join_count)
        assert int(join_count_after) == int(join_count_before) + 1
        self.click_element(EventsLocators.decline_button)
        time.sleep(3)
        join_count_after: str = self.get_text_from_element(EventsLocators.join_count)
        assert int(join_count_after) == int(join_count_before)

    def change_join_maybe(self):
        if self.is_exist_check(EventsLocators.decline_button):
            self.click_element(EventsLocators.decline_button)
            time.sleep(3)
            join_count_before: str = self.get_text_from_element(EventsLocators.join_count)
            maybe_count_before: str = self.get_text_from_element(EventsLocators.maybe_count)
            self.click_element(EventsLocators.join_button)
            time.sleep(3)
        else:
            join_count_before: str = self.get_text_from_element(EventsLocators.join_count)
            maybe_count_before: str = self.get_text_from_element(EventsLocators.maybe_count)
            self.click_element(EventsLocators.join_button)
            time.sleep(3)
        self.click_element(EventsLocators.maybe_button)
        time.sleep(3)
        self.click_element(EventsLocators.join_button)
        time.sleep(3)
        join_count_after: str = self.get_text_from_element(EventsLocators.join_count)
        maybe_count_after: str = self.get_text_from_element(EventsLocators.maybe_count)
        assert (int(join_count_after) == int(join_count_before) + 1) and int(maybe_count_before) == int(
            maybe_count_after)
