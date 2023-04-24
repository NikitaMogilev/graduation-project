from random import randint



class DataUser:
    right_login: str = 'tester25042023@gmail.com'
    login_without_a = 'nikitamglvyandex.ru'
    login_rus_symbols = "Ты не пройдешь"
    password = 'abrakadabra1234'
    wrong_psw = 'hernya'
    url = 'https://www.expat.com/'
    logined_user_country = 'Vietnam'

    #Block EVENT
    event_title: str = f"Dance and Drinking{randint(0,20)}"
    upt_event_title = event_title + "UPT"
    event_description = 'We will dance,drink Rum, discus about cosmos'
    upt_event_description = 'We will dance,drink Rum, discus about cosmos UPDATE'
    event_venue = 'Ul.Lenina15'
    upt_event_venue = 'Ul.Lenina15 UPT!!!'
    cancel_reason = 'Sorry all I am seek'

    #Block Pictures
    country_for_picture = "Vietnam"

    #Block BLOGS
    country_for_blog = "Russia"
    comment_for_blog = "Nice story, its was interesting"
    upt_comment_for_blog = "Nice story, its was interesting UPDATE"

    #BLOCK MEMBERS
    number_user = "2"
    country_for_members = "Vietnam"
    wrong_country = "456"
    nationality = "American"
    wrong_nationality = "6777"

    #Block classifieds
    price_for_ads = '100'
    title_ad = 'Sport and bike'
    ads_description = 'We will go to the mountain for three days'
    ad_city = 'Ho Chi Minh City'
    ad_incorrect_city = 'new moscow'
    foto_path = '/QA/FinalProject/files_for_upload/foto.jpg'
    name_for_ad = 'Nikita'
    phone_number = ''


    def random_mail(self):
        validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        login = ''
        server = '@mail.ru'
        loginlen = randint(5, 10)
        for i in range(loginlen):
            pos = randint(0, len(validchars) - 1)
            login = login + validchars[pos]
        email = login + server
        return email
