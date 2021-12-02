# from unittest import TestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# class Tests(TestCase):
#     def test_SearchWithIncorrectName(self):
#         #arrange
#         url = 'https://www.yakaboo.ua/'
#         search_text = "ehqkhkhfkhlwhvwvehvev.lewhve"
#         browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         browser.fullscreen_window
#         browser.implicitly_wait(30)

#         #act
#         browser.get(url)
#         searchBox = browser.find_element(by=By.ID, value='search')
#         searchBox.send_keys(search_text)
#         searchBox.submit()

#         #assert
#         response = browser.find_element(by=By.CLASS_NAME, value='note-msg').text
#         expectedMessage = "На жаль, за вашим запитом нічого не знайдено."
#         assert expectedMessage in response
#         browser.close()

#     def test_aboutInfo(self):
#         #arrange
#         url = 'https://www.yakaboo.ua/'
#         search_text = "Акції"
#         browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         browser.implicitly_wait(10)

#         #act
#         browser.get(url)
#         browser.find_element(by=By.LINK_TEXT, value=search_text).click()
#         response = browser.find_elements(by=By.CLASS_NAME, value="blog")[0].text
        
#         #assert
#         assert search_text in response
#         browser.close()

from PajeObject import RequestHelper

def test_SearchWithIncorrectName(browser):
    #arrange
    search_text = "ehqkhkhfkhlwhvwvehvev.lewhve"
    yakaboo_page = RequestHelper(browser)
    yakaboo_page.go_to_site()

    #act
    search_field = yakaboo_page.enter_word(search_text)
    yakaboo_page.submit_request(search_field)
    response = yakaboo_page.get_error_response()

    #assert
    expectedMessage = "На жаль, за вашим запитом нічого не знайдено."
    assert expectedMessage in response

def test_aboutInfo(browser):
    #arrange
    search_text = "Акції"
    yakaboo_page = RequestHelper(browser)
    yakaboo_page.go_to_site()

    #act
    search_field = yakaboo_page.find_link_by_name()
    yakaboo_page.click_on_button(search_field)
    response = yakaboo_page.get_response_for_clicked_link()

    #assert
    assert search_text in response

