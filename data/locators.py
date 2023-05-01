from selenium.webdriver.common.by import By
from data.data import DataUser


class RegPageLocators:
    sign_up = (By.XPATH, '//li[@class="register"]/a[contains( text(),"Sign up")]')
    reg_email = (By.XPATH, '//input[@id="email"]')
    create_account_button = (By.XPATH, '//button[@id="submitStep1"]')
    message_error_reg = (By.XPATH, '//div[@data-error-list]//li')
    twice_reg_message = (By.XPATH, '//button[@id="submitStep1"]/..'
                                   '//div[@class="fancy-form-message__text js-fancy-form-text"]')
    pseudo_field = (By.XPATH, '//input[@name="username"]')
    password_field = (By.XPATH, '//input[@id="password"]')
    conditions_checkbox_expat = (By.CSS_SELECTOR, '.checkbox-label')
    error_without_checkbox = (By.XPATH, '//div[@class="error-list"]//li[contains(text(), "You must")]')
    pseudo_submit_but = (By.XPATH, '//button[@id="submitStep2"]')

    user_settings = (By.XPATH, '//ul[@class="user-navigation-fullmenu"]/li[12]/a')
    del_account_button = (By.XPATH, '//button[@id="request-acc-del"]')
    del_account_button_V = (By.XPATH, '//button[@class="btn btn-primary btn-yes"]')
    info_del_message = (By.XPATH, '//p[@class="status"]/span')

    interested_destination_field = (By.XPATH, '//input[@name="destination_of_interest"]')
    click_interest = (By.XPATH, '//li[text()="Vietnam"]')
    cookie_button = (By.CSS_SELECTOR, 'axeptio_btn_acceptAll')

    expat_selector = (By.XPATH, '//span[@id="select2-expat-status-container"]')
    expat_status = (By.XPATH, '//ul[@class="select2-results__options"]/li[2]')
    nationality_selector = (By.XPATH, '//span[@id="select2-nationality-container"]')
    nationality = (By.XPATH, '//ul[@id="select2-nationality-results"]/li[contains(text(), "Russian")]')
    confirm_button = (By.XPATH, '//button[@id="submitStep3"]')
    close_button = (By.XPATH, '//div[@class="auth-container-modal__'
                              'close js-close-register auth-container-modal__close--final"]')

    title1 = (By.XPATH, '//div[@class="tour-intro-title"]')
    start_tour_button = (By.XPATH, '//button[@class="tour-start"]')
    title2 = (By.XPATH, '//h3[@class="popover-title"]')
    next_button = (By.XPATH, '//button[@data-role="next"]')
    title3 = (By.XPATH, '//h3[@class="popover-title"]')
    title4 = (By.XPATH, '//h3[@class="popover-title"]')
    title5 = (By.XPATH, '//h3[@class="popover-title"]')
    title6 = (By.XPATH, '//h3[@class="popover-title"]')
    prev_button = (By.XPATH, '//button[@data-role="prev"]')
    i_got_it_button = (By.XPATH, '//button[@class="end-btn finish-tour"]')

    avatar_img_button = (By.XPATH, '//li[1]//div[@data-id="1"]//img[@alt]')

    user_logo_button = (By.XPATH, '//a[@id="user-navigation__toggler"]//img[@alt]')
    user_menu_event = (By.XPATH, '//i[@class="nc-icon-outline ui-1_calendar-grid-58"]')
    user_menu_ads = (By.XPATH, '//i[@class="nc-icon-outline ui-1_notification-70"]/..')

    logout_button = (By.XPATH, '//a[@class="js-logout"]//span')

    login_button = (By.XPATH, '//li[@class="login"]/a[contains(text(), "Login")]')
    username_field = (By.XPATH, '//input[@id="loginUsername"]')
    authorized_password_field = (By.XPATH, '//input[@id="loginPassword"]')
    login_button1 = (By.XPATH, '//button[@id="loginButton"]')
    login_error = (By.XPATH, '//button[@id="loginButton"]/..'
                             '//div[@class="fancy-form-message__text js-fancy-form-text"]')


class MyTimelineLocator:
    filter_button = (By.XPATH, '//div[@class="header-line"]//span')

    dict_checkboxes = {'forum': (By.XPATH, '//input[@data-type="1"]/../ins'),
                       'events': (By.XPATH, '//input[@data-type="9"]/../ins'),
                       'business': (By.XPATH, '//input[@data-type="10"]/../ins'),
                       'new_members': (By.XPATH, '//input[@data-type="6"]/../ins'),
                       'classifieds': (By.XPATH, '//input[@data-type="2"]/../ins'),
                       'jobs': (By.XPATH, '//input[@data-type="4"]/../ins'),
                       'housing': (By.XPATH, '//input[@data-type="3"]/../ins'),
                       'pictures': (By.XPATH, '//input[@data-type="8"]/../ins'),
                       'blogs': (By.XPATH, '//input[@data-type="11"]/../ins'),
                       'guides': (By.XPATH, '//input[@data-type="5"]/../ins')
                       }

    warning_filter_message = (By.XPATH, '//div[@class="filters-overlay-desktop active"]//div[@class="text"]')
    select_all = (By.XPATH, '//div[@class="select-all-checkboxes"]')
    all_checkboxes = (By.XPATH, '//div[@style="position: relative;"]')
    filter_save_button = (By.XPATH, '//div[@class="filters-save"]')
    timeline_list = (By.XPATH, '//div[@class="loaded-items aos-init aos-animate"]/li')
    first_article = (By.XPATH, '//li[@data-type]')
    empty_message = (By.XPATH, '//div[@class="timeline-empty-message"]')
    list_avatars = (By.XPATH, '//ul[@id="timeline-content"]//li[@class="timeline-item"]/a')


class HeadLineLocators:
    community = (By.CSS_SELECTOR, '#main-nav-ul li:nth-child(3)  span.toggler')
    events = (By.XPATH, '//ul[@class="main-nav__level2"]//a[contains(text(),"Events")]')
    members = (By.XPATH, '//ul[@class="main-nav__level2"]//a[contains(text(),"Members")]')
    pictures = (By.CSS_SELECTOR, '#main-nav-ul > li:nth-child(3) > div > ul > li:nth-child(3) > a')
    blogs = (By.XPATH, '//ul[@class="main-nav__level2"]//a[contains(text(),"Blogs")]')
    classifieds = (By.XPATH, '//a[contains(text(),"Classifieds")]')


class EventsLocators:
    post_event_button = (By.XPATH, '//a[@data-scenario="15"]')

    # Data for filling event
    category_selector = (By.XPATH, '//select[@id="category"]')
    title_event = (By.XPATH, '//input[@name="title0"]')
    description_event = (By.XPATH, '//textarea[@name="description0"]')
    event_privacy_selector = (By.XPATH, '//select[@id="privacy"]')
    country = (By.XPATH, '//span[@title="Vietnam"]')
    event_venue = (By.XPATH, '//textarea[@id="eventlocation"]')
    calendar_start = (By.XPATH, '//input[@id="event_start"]')
    date_event_beginning = (By.XPATH, '//td[@class="day active"]//following-sibling::td')
    hour_event_beginning = (By.XPATH, '//div[contains(@style, "z-index: 100009")]//span[@class="hour"][5]')
    minute_event_beginning = (By.XPATH, '//div[contains(@style, "z-index: 100009")]//span[@class="minute"][5]')
    advanced_options = (By.XPATH, '//a[@class="show-advanced-options"]')
    fields_advanced_options = (By.XPATH, '//div[@class ="advanced-block margin-bottom-10"]')
    event_submit_button = (By.XPATH, '//button[@id="event_submit"]')
    title_event_for_assert = (By.XPATH, '//h1[@itemprop="name"]')
    venue_event_for_assert = (By.XPATH, '//div[@itemprop="location"]/span')

    # locators for edit and cancel event
    edit_button = (By.XPATH, '//div[@class="event-admin-bar"]//a[@class=" btn edit"]')
    event_in_user_menu_button = (By.XPATH, f'//span[contains(text(),"{DataUser.event_title}")]')
    title_event_upt = (By.XPATH, '//input[@name="title0"]')
    event_venue_upt = (By.XPATH, '//textarea[@id="eventlocation"]')
    cancel_button = (By.XPATH, '//div[@class="event-admin-bar"]//a[@class="btn cancel"]')
    cancel_reason = (By.XPATH, '//textarea[@id="reasonen"]')
    cancel_event_button = (By.XPATH, '//button[@id="cancel-event-submit"]')
    cancel_message = (By.XPATH, '//span[@class="eventExpiredTxt"]')

    # locators for check buttons join_maybe_cancel
    asia_field = (By.XPATH, '//li[@class="showIt"][2]//span')
    upcoming_event = (By.XPATH, '//div[@id="list-events-upcoming"]/div[1]//a/span')
    maybe_button = (By.XPATH, '//div[@id="section-event-header"]//a[@class=" fuddleAll btn maybe"]')
    join_button = (By.XPATH, '//div[@id="section-event-header"]//a[@class=" fuddleAll btn accept"]')
    join_count = (By.XPATH, '//div[@id="section-event-header"]//div[@class="block-participants"]'
                            '//div[contains(@class, "going")]/strong')
    maybe_count = (By.XPATH, '//div[@id="section-event-header"]//div[@class="block-participants"]'
                             '//div[contains(@class, "maybe")]/strong')
    decline_button = (By.XPATH, '//div[@id="section-event-header"]//a[@class=" fuddleAll btn decline"]')


class PictureLocator:
    world_but = (By.XPATH, '//li[@class="showIt"][1]//span')

    # Locators for country selection
    country_selector = (By.XPATH, '//select[@id="select-destination"]')
    drop_country_box = (By.XPATH, '//span[@id="select2-select-destination-container"]')
    input_country_choice = (By.XPATH, '//span[@class="select2-search select2-search--dropdown"]/input')
    ok_button = (By.XPATH, '//button[@id="btn-search"]')

    # Locators for check
    alert_message = (By.XPATH, '//td[contains(text(), "Please select at least one criteria for your search")]')
    title_country = (By.XPATH, '//div[@id="section-annonce"]/h1')
    picture_of_chosen_place = (By.XPATH, '//div[@id="section-annonce"]')
    country_region_selector = (By.XPATH, '//input[@class="select2-search__field"]')
    region_choice = (By.XPATH, '//ul[@id="select2-select-destination-results"]/li[5]')


class BlogLocators:
    # Locators for add blog
    add_blog_button = (By.XPATH, '//a[@class=" btn fuddleAll"]')
    blog_title = (By.XPATH, '//input[@id="blogTitle"]')
    description_blog = (By.XPATH, '//textarea[@id="blogDescription"]')
    blog_url = (By.XPATH, '//input[@id="blogAddress"]')
    submit_button = (By.XPATH, '//button[@id="btnAddBlog"]')
    blog_url_error = (By.XPATH, '//input[@id="blogAddress"]/../div//li')
    success_message = (By.XPATH, '//p[@class="section-description"]/strong')

    # locators to select a country and make adjustments to select a country
    selector_country = (By.XPATH, '//select[@id="select-destination"]')
    list_blogs = (By.XPATH, '//div[@class="path"]/span[3]')
    drop_country_box = (By.XPATH, '//span[@id="select2-select-destination-container"]')
    input_country_choice = (By.XPATH, '//span[@class="select2-search select2-search--dropdown"]/input')
    ok_button = (By.XPATH, '//button[@id="btn-search"]')
    alert_message = (By.XPATH, '//td[contains(text(), "Please select at least one criteria for your search")]')

    # Locators choice of the whole world or the region for which to make the choice of the country
    world_field = (By.XPATH, '//li[@class="showIt"][1]//span')
    region_field = (By.XPATH, '//li[@class="showIt"][2]//span')

    # Locator for anyblog
    any_blog = (By.XPATH, '//div[@class="blog-list"]/div[@class="view-row"][3]//div[@class="titre"]/a')

    # Locators for comments
    comment_filed = (By.XPATH, '//div[@data-placeholder="Share your thoughts..."]/p')
    comment_submit_button = (By.XPATH, '//button[@class="editor__action"]')
    my_comment = (By.XPATH, '//div[@class="comment-thread__text"]/p')
    options_list = (By.XPATH, '//img[@class="comment-thread__option-icon"]')
    edit_button = (By.XPATH, '//div[@class="comment-thread__option"]//li[1]/p')
    edit_comment_field = (By.XPATH, f'//p[contains(text(),"{DataUser.comment_for_blog}")]'
                                    f'/../../div[@data-placeholder="Share your thoughts..."]')
    commentator_nick = (By.XPATH, '//span[@class="comment-thread__header-author"]')
    delete_button = (By.XPATH, '//div[@class="comment-thread__option"]//li[2]/p')


class MembersLocator:
    # Locators for selector
    destination = (By.XPATH, '//select[@id="select_destination"]')
    nationality = (By.XPATH, '//select[@id="select_nationality"]')
    age = (By.XPATH, '//select[@id="select_age"]')
    status = (By.XPATH, '//select[@id="select_status"]')
    gender = (By.XPATH, '//select[@id = "select_gender"]')
    professional_status = (By.XPATH, '//select[@id="select_occupation"]')
    language = (By.XPATH, '//select[@id="select_language"]')
    online = (By.XPATH, '//select[@id="select_language"]')
    search_button = (By.CSS_SELECTOR, 'button#filter-btn')

    # Locators for selector click and negotive scenario
    destination_click = (By.CSS_SELECTOR, '#select2-select_destination-container')
    destination_input = (By.CSS_SELECTOR, '.select2-search__field')
    wrong_destination_message = (By.CSS_SELECTOR, '.select2-results__options li')
    nationality_click = (By.CSS_SELECTOR, '#select2-select_nationality-container')
    nationality_input = (By.CSS_SELECTOR, '.select2-search__field')
    wrong_nationality_message = (By.CSS_SELECTOR, '.select2-results__options li')

    # Locators for assert by filter nationality and BUG
    list_users = (By.CSS_SELECTOR, 'div.user-location')
    user_inside_button = (By.CSS_SELECTOR, '.col-md-6:nth-child(3) .user-name.fuddleLnk')
    user_nationality = (By.CSS_SELECTOR, 'div.user-subtitle')


class AdsLocators:
    # locators to check acordd type of ad and lower list
    categories = {
        'activities': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="76"]'),
        'buy_and_sell': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="18"]'),
        'classes': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="32"]'),
        'community': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="1"]'),
        'electronics': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="24"]'),
        'home': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="77"]'),
        'leisure_items': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="78"]'),
        'personals': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="13"]'),
        'pets': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="10"]'),
        'testimonies_lost_items_peple': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="75"]'),
        'vehicles': (By.CSS_SELECTOR, 'div[class*=js-parent-select][data-parent-category="19"]')
    }

    list_subcategory = (By.CSS_SELECTOR, 'div[class="browse-category__items js-category-items"]')

    # locators for post classifieds
    post_add = (By.CSS_SELECTOR, 'a.btn.btn-cta')
    sport_partner = (By.CSS_SELECTOR, 'div[data-cat-id="137"]')
    type_of_ad = (By.CSS_SELECTOR, 'label[for="offering"]')
    your_status = (By.CSS_SELECTOR, 'label[for="individual"]')
    currency_selector = (By.CSS_SELECTOR, '#currency')
    price_value = (By.CSS_SELECTOR, '#price')
    negotiable_yes = (By.CSS_SELECTOR, 'label[for="noNegotiable"]')
    negotiable_no = (By.CSS_SELECTOR, 'label[for="noNegotiable"]')
    calendar = (By.CSS_SELECTOR, '#validity')
    valid_for_today = (By.CSS_SELECTOR, 'button.picker__button--today')
    title_ad = (By.CSS_SELECTOR, '#title0')
    description_frame = (By.XPATH, '//div[@id="cke_description0"]//iframe[@class="cke_wysiwyg_frame cke_reset"]')
    description = (By.CSS_SELECTOR, '.cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders')
    autotranslation_button_yes = (By.CSS_SELECTOR, 'label[for="autoTranslation"]')
    spanish_lang = (By.CSS_SELECTOR, '[for="languageSelected[]_languageSelected1"] .checkbox-label')
    ads_country_selector = (By.CSS_SELECTOR, '#country')
    city_sellector = (By.CSS_SELECTOR, '#region')
    click_city = (By.XPATH, '//div[text()="Ho Chi Minh City, Vietnam"]')
    upload_field = (By.CSS_SELECTOR, '[class="dz-default dz-message"] span')
    contact_name = (By.CSS_SELECTOR, '#contactName')
    phone_number = (By.CSS_SELECTOR, '#telephone')
    email = (By.CSS_SELECTOR, '#email')
    add_button = (By.CSS_SELECTOR, '#ad_submit')
    success_message = (By.CSS_SELECTOR, '.heading-bordered__title')
    error_message = (By.CSS_SELECTOR, '#errorMessage')
