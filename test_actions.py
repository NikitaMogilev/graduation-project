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
import allure


# @allure.feature('Registration')
# @allure.title('Test of creation random user')
# # def test_create_user(browser):
# #     sign_page = Sign_Page(browser)
# #     sign_page.open()
# #     sign_page.click_sign_up()
# #     sign_page.cookie_button_click()
# #     sign_page.new_user_email_input()
# #     sign_page.pseudo_and_password()
# #     sign_page.fill_my_info()
# #     sign_page.look_intro()
# #     sign_page.check_verification()
# #     sign_page.delete_user()

@allure.feature('Registration')
@allure.title('Test which try to registr the same user twice')
def test_twice_create_authorized_user_mail(browser):
    sign_page = Sign_Page(browser)
    with allure.step('Open main page'):
        sign_page.open()
    with allure.step('Open click sign up'):
        sign_page.click_sign_up()
    with allure.step('Try to input email which was registered'):
        sign_page.authorized_email_input_in_reg()


@allure.feature('LOGIN IN')
@allure.title('Test which try to sign in user with email without symbol @')
def test_negative_loginning_without_a(browser):
    login_page = Authorized_User(browser)
    with allure.step('Open main page'):
        login_page.open()
    with allure.step('Input email without @ in login field'):
        login_page.wrong_authorization_without_a()


@allure.feature('LOGIN IN')
@allure.title('Test which try to sign in user with russian symbols and without password')
def test_negative_loginning_rus_symbols(browser):
    login_page = Authorized_User(browser)
    with allure.step('Open main page'):
        login_page.open()
    with allure.step('Input russians symbols in login field'):
        login_page.wrong_authorization_rus_symbols_and_no_psw()


@allure.feature('LOGIN IN')
@allure.title('Test which try to sign in user with wrong password')
def test_negative_logining_with_wrong_pws(browser):
    login_page = Authorized_User(browser)
    with allure.step('Open main page'):
        login_page.open()
    with allure.step('Input wrong password'):
        login_page.wrong_password()


@allure.feature('LOGIN IN')
@allure.title('Test which try to sign in user with right data')
def test_login(browser):
    logined_user = Authorized_User(browser)
    with allure.step('Open main page'):
        logined_user.open()
    with allure.step('Login in with correct data'):
        logined_user.login_in()


@allure.feature('LOGIN IN')
@allure.title('Test exit from authorized user')
def test_exit_from(browser):
    login_page = Authorized_User(browser)
    with allure.step('Open main page'):
        login_page.open()
    with allure.step('Login in with correct data'):
        login_page.login_in()
    with allure.step('Exit from authorized user'):
        login_page.exit_from_account()


@allure.feature('MAIN MENU')
@allure.title('Test which check filters on timeline and correct info in timeline')
def test_filter(browser, login_in):
    with allure.step('Open main page and login in'):
        user = MyTimeline(browser, login_in)
    time.sleep(5)
    with allure.step('Check of work filters in my timeline'):
        user.checkbox_filters_check()


@allure.feature('MAIN MENU')
@allure.title('Test which check redirection after click on avatar')
def test_avatars_links(browser, login_in):
    with allure.step('Open main page and login in'):
        user = MyTimeline(browser, login_in)
    with allure.step('Cancel checkbox with new members, because line members have not avatar image'):
        user.chose_filters_without_members()
    with allure.step('Check that click on avatar redirect to user from timeline'):
        user.check_link_avatars()


@allure.feature('EVENT BLOCK')
@allure.title('Test which check POST new event')
def test_post_event(browser, login_in):
    with allure.step('Open main page and login in'):
        user = EventPage(browser, login_in)
    time.sleep(10)
    with allure.step('Open event page'):
        user.open_event_page()
    with allure.step('Click POST event'):
        user.click_post_event()
    with allure.step('Fill data new event and check data after creation'):
        user.fill_data_for_event()


@allure.feature('EVENT BLOCK')
@allure.title('Test which check update your event')
def test_update_event(browser, login_in):
    with allure.step('Open main page and login in'):
        user = EventPage(browser, login_in)
    with allure.step('Go to event page'):
        user.enter_in_event()
    time.sleep(10)
    with allure.step('update data created event and check data after creation'):
        user.update_event()


@allure.feature('EVENT BLOCK')
@allure.title('Test which check cancel of your event')
def test_cancel_event(browser, login_in):
    with allure.step('Open main page and login in'):
        user = EventPage(browser, login_in)
    with allure.step('Go to event page'):
        user.enter_in_event()
    time.sleep(5)
    with allure.step('cancel created event and check by cancel message'):
        user.cancel_event()


@allure.feature('EVENT BLOCK')
@allure.title('Test which check work and right count of buttons join and maybe in another event')
def test_check_other_event(browser, login_in):
    with allure.step('Open main page and login in'):
        user = EventPage(browser, login_in)
    time.sleep(10)
    with allure.step('Go to event page'):
        user.open_event_page()
    with allure.step('Go to Random event'):
        user.go_to_other_event()
    with allure.step('Check buttons maybe and decline in event and check counter'):
        user.maybe_decline_check_button()
    with allure.step('Check buttons join and decline in event and check counter'):
        user.join_decline_check_button()
    with allure.step('Check clicking buttons maybe and decline and join in event and check counter'):
        user.change_join_maybe()


@allure.feature('PICTURES BLOCK')
@allure.title('Test which check choice of country and shown pictures')
def test_picture_menu(browser, login_in):
    with allure.step('Open main page and login in'):
        user = PicturePage(browser, login_in)
    time.sleep(10)
    with allure.step('Open picture page'):
        user.open_picture_page()
    with allure.step('Click choice whole world to be able choose any country'):
        user.world_around_click()
    with allure.step('Choose any country'):
        user.chose_country()
    with allure.step('Check that chosen country assert in title'):
        user.name_chosen_country()


@allure.feature('PICTURE BLOCK')
@allure.title('Test which check incorrect choice from list of countries and do alert message')
def test_wrong_data_country_in_picture(browser, login_in):
    with allure.step('Open main page and login in'):
        user = PicturePage(browser, login_in)
    time.sleep(10)
    with allure.step('Open picture page'):
        user.open_picture_page()
    with allure.step('Click choice whole world to be able choose any country'):
        user.world_around_click()
    with allure.step('Try to send instead country name some numbers'):
        user.send_wrong_keys_in_country()


@allure.feature('BLOGS BLOCK')
@allure.title('Test which sort blogs by country')
def test_open_and_sort_blogs(browser, login_in):
    with allure.step('Open main page and login in'):
        user = BlogsPage(browser, login_in)
    time.sleep(10)
    with allure.step('Open blog page'):
        user.open_blogs_page()
    with allure.step('Click choice whole world to be able choose any country'):
        user.world_around_click()
    with allure.step('Choose any country'):
        user.chose_country()
    time.sleep(10)
    with allure.step('Check that blogs respond chosen country'):
        user.check_blogs_about_choosen_country()


@allure.feature('BLOGS BLOCK')
@allure.title('Test which check incorrect choice from list of countries and do alert message')
def test_wrong_data_country_in_blogs(browser, login_in):
    with allure.step('Open main page and login in'):
        user = BlogsPage(browser, login_in)
    time.sleep(10)
    with allure.step('Open blog page'):
        user.open_blogs_page()
    with allure.step('Click choice whole world to be able choose any country'):
        user.world_around_click()
    with allure.step('Try to send instead country name some numbers'):
        user.send_wrong_keys_in_country()


@allure.feature('BLOGS BLOCK')
@allure.title('Test which CREATE, UPDATE and DELETE comments under blogs')
def test_CRUD_comments(browser, login_in):
    with allure.step('Open main page and login in'):
        user = BlogsPage(browser, login_in)
    time.sleep(10)
    with allure.step('Open blog page'):
        user.open_blogs_page()
    with allure.step('Click choice whole world to be able choose any country'):
        user.world_around_click()
    with allure.step('Choose any country'):
        user.chose_country()
    with allure.step('Choose any blog'):
        user.choose_blog()
    time.sleep(5)
    with allure.step('Make comment under chosen blog'):
        user.make_comment_under_blog_story()
    with allure.step('Check that up to you comment is your name'):
        user.commentator_name()
    with allure.step('Update your comment under chosen blog'):
        user.upt_comment_under_blog_story()
    with allure.step('Delete comment under chosen blog'):
        user.del_comment()


@allure.feature('MEMBERS BLOCK')
@allure.title('Test check that we could not write values not from the list in search lists')
def test_open_members_and_try_fill_wrong_data(browser, login_in):
    with allure.step('Open main page and login in'):
        user = MemberPage(browser, login_in)
    time.sleep(5)
    with allure.step('Open member page'):
        user.open_member_page()
    with allure.step('Input some number in country and nationality fields and assert error message'):
        user.wrong_data()


@allure.feature('MEMBERS BLOCK')
@allure.title('Test check find of the users by given parameters')
def test_open_member_and_fill_correct_data(browser, login_in):
    with allure.step('Open main page and login in'):
        user = MemberPage(browser, login_in)
    time.sleep(10)
    with allure.step('Open member page'):
        user.open_member_page()
    with allure.step('Fill correct data in find selectors'):
        user.fill_select_data()
    with allure.step('Check correct filters work'):
        user.check_filter_users()


@allure.feature('MEMBERS BLOCK')
@allure.title('Test check info under avatar in user list')
@pytest.mark.xfail
def test_user_info(browser, login_in):
    with allure.step('Open main page and login in'):
        user = MemberPage(browser, login_in)
    time.sleep(5)
    with allure.step('Open member page'):
        user.open_member_page()
    with allure.step('Check user info under avatar'):
        user.user_info_in_user_list()


@allure.feature('MEMBERS BLOCK')
@allure.title('Test which should find user by username')
@pytest.mark.xfail
def test_search_by_nick_name(browser, login_in):
    with allure.step('Open main page and login in'):
        user = MemberPage(browser, login_in)
    with allure.step('Try to find user by Username'):
        user.search_by_nick_name()


@allure.feature('ADS BLOCK')
@allure.title('Test which check subcategories when you post ads')
def test_check_categories_classified(browser, login_in):
    with allure.step('Open main page and login in'):
        user = Ads(browser, login_in)
    time.sleep(5)
    with allure.step('Open Ads page'):
        user.open_ads_page()
    with allure.step('Click Post our Ads'):
        user.post_your_ads()
    with allure.step('Check correct categories when check ads'):
        user.check_categories()


@allure.feature('ADS BLOCK')
@allure.title('Test which check impossibility of post ads with wrong data')
def test_wrong_data_post_ads(browser, login_in):
    with allure.step('Open main page and login in'):
        user = Ads(browser, login_in)
    time.sleep(5)
    with allure.step('Open Ads page'):
        user.open_ads_page()
    with allure.step('Click Post our Ads'):
        user.post_your_ads()
    with allure.step('Fill category our Ads'):
        user.fill_category()
    with allure.step('Fill basic info our Ads'):
        user.basic_info()
    with allure.step('Fill wrong location our Ads'):
        user.chose_wrong_location()
    with allure.step('Fill right contacts our Ads'):
        user.right_contacts()
    with allure.step('Click add Ads'):
        user.add_my_classified()
    time.sleep(15)
    with allure.step('Assert error message'):
        user.error_check_message()


@allure.feature('ADS BLOCK')
@allure.title('Test which check post ads with right data')
def test_right_post_ads(browser, login_in):
    with allure.step('Open main page and login in'):
        user = Ads(browser, login_in)
    time.sleep(5)
    with allure.step('Open Ads page'):
        user.open_ads_page()
    with allure.step('Click Post our Ads'):
        user.post_your_ads()
    with allure.step('Fill category our Ads'):
        user.fill_category()
    with allure.step('Fill basic info our Ads'):
        user.basic_info()
    with allure.step('Fill right location our Ads'):
        user.chose_location()
    with allure.step('Upload foto'):
        user.upload_foto()
    with allure.step('Fill right contacts our Ads'):
        user.right_contacts()
    with allure.step('Click add my Ads after fill correct data'):
        user.add_my_classified()
    time.sleep(15)
    with allure.step('Assert success message'):
        user.success_check()
