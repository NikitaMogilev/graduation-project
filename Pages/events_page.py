import time
from selenium import webdriver
from data.base_page import BasePage
from data.locators import RegPageLocators
from data.locators import HeadLineLocators
from data.locators import EventsLocators
from data.data import DataUser
import allure


class EventPage(BasePage):

    def __init__(self, browser: webdriver.Chrome, login_in):
        super().__init__(browser)

    def open_event_page(self):
        self.click_on_drop_down_list(HeadLineLocators.community, HeadLineLocators.events)
        assert self.check_title() == 'Events in Vietnam'

    def click_post_event(self):
        self.click_element(EventsLocators.post_event_button)
        assert self.check_title() == 'Vietnam events: post your event'

    @allure.step('Fill data of event')
    def fill_data_for_event(self, title=DataUser.event_title,
                            description=DataUser.event_description,
                            venue=DataUser.event_venue):
        with allure.step('Chose event category'):
            self.selector_by_index(EventsLocators.category_selector, '3')
        with allure.step('Chose event title'):
            self.send_keys(EventsLocators.title_event, title)
        with allure.step('Make some description'):
            self.send_keys(EventsLocators.description_event, description)
        with allure.step('Chose privacy politic of event'):
            self.selector_by_value(EventsLocators.event_privacy_selector, '3')
        with allure.step('Chose event venue/adress'):
            self.send_keys(EventsLocators.event_venue, venue)
        with allure.step('Chose event date and time of beginning'):
            self.click_element(EventsLocators.calendar_start)
            self.click_element(EventsLocators.date_event_beginning)
            self.click_element(EventsLocators.hour_event_beginning)
            self.click_element(EventsLocators.minute_event_beginning)
        with allure.step('Click submit button'):
            self.click_element(EventsLocators.event_submit_button)
        with allure.step('Check that title and venue which you write is like in event page'):
            assert self.get_text_from_element(EventsLocators.title_event_for_assert) == title
            assert self.get_text_from_element(EventsLocators.venue_event_for_assert) == venue + ','

    @allure.step('Enter in even which you create from main menu')
    def enter_in_event(self):
        with allure.step('Click logo button'):
            self.click_element(RegPageLocators.user_logo_button)
        with allure.step('Click event button in main menu'):
            self.click_element(RegPageLocators.user_menu_event)
        with allure.step('Click last event which you create or update or |WARNING| TRY TO GO'):
            self.click_element(EventsLocators.event_in_user_menu_button)

    @allure.step('UPDATE event data')
    def update_event(self, title=f'{DataUser.upt_event_title}',
                     description=DataUser.upt_event_description,
                     venue=DataUser.upt_event_venue):
        self.click_element(EventsLocators.edit_button)
        self.fill_data_for_event(title, description, venue)

    @allure.step('Cancel event')
    def cancel_event(self, cancel_reason=DataUser.cancel_reason):
        with allure.step('Click cancel event button'):
            self.click_element(EventsLocators.cancel_button)
        with allure.step('Write some reason why you cancel the event'):
            self.send_keys(EventsLocators.cancel_reason, cancel_reason)
        with allure.step('Click submit cancel button'):
            self.click_element(EventsLocators.cancel_event_button)
        with allure.step('Check event cancel message'):
            assert self.get_text_from_element(EventsLocators.cancel_message) == f'Event cancelled: {cancel_reason}'

    @allure.step('Go to any event')
    def go_to_other_event(self):
        with allure.step('Choose all events from Asia'):
            self.click_element(EventsLocators.asia_field)
            name_event = self.find_element(EventsLocators.upcoming_event).text
            allure.attach(name_event, name='name of any chosen event')
        with allure.step('Click upcoming event and redirect to new page'):
            self.click_element(EventsLocators.upcoming_event)
        with allure.step('Check that chosen event name the same in redirect page'):
            assert name_event == self.get_text_from_element(EventsLocators.title_event_for_assert)

    @allure.step('Click on MAYBE button and check counter')
    def maybe_decline_check_button(self):
        with allure.step('Check if DECLINE button is exist click it if not exist click MAYBE button'):
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
        with allure.step('Check and Count MAYBE button after click it and after decline'):
            maybe_count_after: str = self.get_text_from_element(EventsLocators.maybe_count)
            assert int(maybe_count_after) == int(maybe_count_before) + 1
            self.click_element(EventsLocators.decline_button)
            time.sleep(3)
            maybe_count_after: str = self.get_text_from_element(EventsLocators.maybe_count)
            assert int(maybe_count_after) == int(maybe_count_before)

    @allure.step('Click on JOIN button and check counter')
    def join_decline_check_button(self):
        with allure.step('Check if DECLINE button is exist click it if not exist click JOIN button'):
            if self.is_exist_check(EventsLocators.decline_button):
                self.click_element(EventsLocators.decline_button)
                time.sleep(5)
                join_count_before: str = self.get_text_from_element(EventsLocators.join_count)
                self.click_element(EventsLocators.join_button)
                time.sleep(5)
            else:
                join_count_before: str = self.get_text_from_element(EventsLocators.join_count)
                self.click_element(EventsLocators.join_button)
                time.sleep(5)
        with allure.step('Check and Count JOIN button after click it and after decline'):
            join_count_after: str = self.get_text_from_element(EventsLocators.join_count)
            assert int(join_count_after) == int(join_count_before) + 1
            self.click_element(EventsLocators.decline_button)
            time.sleep(5)
            join_count_after: str = self.get_text_from_element(EventsLocators.join_count)
            assert int(join_count_after) == int(join_count_before)

    @allure.step('Click on MAYBE and JOIN button and check counter')
    def change_join_maybe(self):
        with allure.step('Check if DECLINE button is exist click it if not exist click JOIN button'):
            if self.is_exist_check(EventsLocators.decline_button):
                self.click_element(EventsLocators.decline_button)
                time.sleep(5)
                join_count_before: str = self.get_text_from_element(EventsLocators.join_count)
                maybe_count_before: str = self.get_text_from_element(EventsLocators.maybe_count)
                self.click_element(EventsLocators.join_button)
                time.sleep(5)
            else:
                join_count_before: str = self.get_text_from_element(EventsLocators.join_count)
                maybe_count_before: str = self.get_text_from_element(EventsLocators.maybe_count)
                self.click_element(EventsLocators.join_button)
                time.sleep(5)
            with allure.step('Click maybe button then JOIN '):
                self.click_element(EventsLocators.maybe_button)
                time.sleep(5)
                self.click_element(EventsLocators.join_button)
                time.sleep(5)
                join_count_after: str = self.get_text_from_element(EventsLocators.join_count)
                maybe_count_after: str = self.get_text_from_element(EventsLocators.maybe_count)
            with allure.step('Check that counter of KOIN and MAYBE buttons is correct'):
                assert (int(join_count_after) == int(join_count_before) + 1) and int(maybe_count_before) == int(
                    maybe_count_after)
