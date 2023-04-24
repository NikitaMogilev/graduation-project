import time
import pytest
from Pages.sign_page import Sign_Page
from Pages.sign_page import Authorized_User
from Pages.my_timeline import MyTimeline
from Pages.events_page import EventPage
from Pages.pictures_page import PicturePage
from Pages.blogs_page import BlogsPage
from Pages.member_page import MemberPage
from Pages.ads_page import Ads
from retrying import retry


def test_create_user(browser):
    sign_page = Sign_Page(browser)
    sign_page.open()
    sign_page.click_sign_up()
    sign_page.new_user_email_input()
    sign_page.pseudo_and_password()
    sign_page.fill_my_info()
    sign_page.look_intro()
    sign_page.check_verification()
    sign_page.delete_user()


def test_twice_create_authorized_user_mail(browser):
    sign_page = Sign_Page(browser)
    sign_page.open()
    sign_page.click_sign_up()
    sign_page.authorized_email_input_in_reg()


def test_negative_loginning_without_a(browser):
    login_page = Authorized_User(browser)
    login_page.open()
    login_page.wrong_authorization_without_a()


def test_negative_loginning_rus_sumbols(browser):
    login_page = Authorized_User(browser)
    login_page.open()
    login_page.wrong_authorization_rus_symbols_and_no_psw()


def test_negative_logining_without_pws(browser):
    login_page = Authorized_User(browser)
    login_page.open()
    login_page.wrong_password()


def test_login(browser):
    logined_user = Authorized_User(browser)
    logined_user.open()
    logined_user.login_in()


@retry(stop_max_delay=10000)
def test_filter(browser, login_in):
    user = MyTimeline(browser, login_in)
    time.sleep(5)
    user.checkbox_filters_check()


def test_avatars_links(browser, login_in):
    user = MyTimeline(browser, login_in)
    user.chose_filters_without_members()
    user.check_link_avatars()


def test_post_event(browser, login_in):
    user = EventPage(browser, login_in)
    time.sleep(10)
    user.open_event_page()
    user.click_post_event()
    user.fill_data_for_event()


@retry(stop_max_delay=10000)
def test_update_event(browser, login_in):
    user = EventPage(browser, login_in)
    user.enter_in_event()
    time.sleep(10)
    user.update_event()


@retry(stop_max_delay=10000)
def test_cancel_event(browser, login_in):
    user = EventPage(browser, login_in)
    user.enter_in_event()
    time.sleep(5)
    user.cancel_event()


def test_check_other_event(browser, login_in):
    user = EventPage(browser, login_in)
    time.sleep(15)
    user.open_event_page()
    user.go_to_other_event()
    user.maybe_decline_check_button()
    user.join_decline_check_button()
    user.change_join_maybe()


def test_picture_menu(browser, login_in):
    user = PicturePage(browser, login_in)
    time.sleep(10)
    user.open_picture_page()
    user.world_around_click()
    user.chose_country()
    user.name_chosen_country()


def test_wrong_data_country_in_picture(browser, login_in):
    user = PicturePage(browser, login_in)
    time.sleep(10)
    user.open_picture_page()
    user.world_around_click()
    user.send_wrong_keys_in_country()


def test_open_and_sort_blogs(browser, login_in):
    user = BlogsPage(browser, login_in)
    time.sleep(10)
    user.open_blogs_page()
    user.world_around_click()
    user.chose_country()
    time.sleep(10)
    user.check_blogs_about_choosen_country()


def test_wrong_data_country_in_blogs(browser, login_in):
    user = BlogsPage(browser, login_in)
    time.sleep(10)
    user.open_blogs_page()
    user.world_around_click()
    user.send_wrong_keys_in_country()


def test_CRUD_comments(browser, login_in):
    user = BlogsPage(browser, login_in)
    time.sleep(10)
    user.open_blogs_page()
    user.world_around_click()
    user.chose_country()
    user.choose_blog()
    time.sleep(5)
    user.make_comment_under_blog_story()
    user.commentator_name()
    user.upt_comment_under_blog_story()
    user.del_comment()


def test_open_members_and_try_fill_wrong_data(browser, login_in):
    user = MemberPage(browser, login_in)
    time.sleep(5)
    user.open_member_page()
    user.wrong_data()


def test_open_member_and_fill_correct_data(browser, login_in):
    user = MemberPage(browser, login_in)
    time.sleep(10)
    user.open_member_page()
    user.fill_select_data()
    user.check_filter_users()


@pytest.mark.xfail
def test_user_info(browser, login_in):
    user = MemberPage(browser, login_in)
    time.sleep(5)
    user.open_member_page()
    user.user_info_in_user_list()


@pytest.mark.xfail
def test_search_by_nick_name(browser, login_in):
    user = MemberPage(browser, login_in)
    user.search_by_nick_name()


def test_check_categories_classified(browser, login_in):
    user = Ads(browser, login_in)
    time.sleep(5)
    user.open_ads_page()
    user.post_your_ads()
    user.check_categories()


def test_wrong_data_post_ads(browser, login_in):
    user = Ads(browser, login_in)
    time.sleep(5)
    user.open_ads_page()
    user.post_your_ads()
    user.fill_category()
    user.basic_info()
    user.chose_wrong_location()
    user.right_contacts()
    user.add_my_classified()
    time.sleep(15)
    user.error_check_message()


def test_right_post_ads(browser, login_in):
    user = Ads(browser, login_in)
    time.sleep(5)
    user.open_ads_page()
    user.post_your_ads()
    user.fill_category()
    user.basic_info()
    user.chose_location()
    user.upload_foto()
    user.right_contacts()
    user.add_my_classified()
    time.sleep(15)
    user.success_check()
