from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Tests(TestCase):
    def test_SearchWithIncorrectName(self):
        #arrange
        url = 'https://www.yakaboo.ua/'
        search_text = "ehqkhkhfkhlwhvwvehvev.lewhve"
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.fullscreen_window
        browser.implicitly_wait(30)

        #act
        browser.get(url)
        searchBox = browser.find_element(by=By.ID, value='search')
        searchBox.send_keys(search_text)
        searchBox.submit()

        #assert
        response = browser.find_element(by=By.CLASS_NAME, value='note-msg').text
        expectedMessage = "На жаль, за вашим запитом нічого не знайдено."
        assert expectedMessage in response
        browser.close()

    def test_aboutInfo(self):
        #arrange
        url = 'https://www.yakaboo.ua/'
        search_text = "Акції"
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(10)

        #act
        browser.get(url)
        browser.find_element(by=By.LINK_TEXT, value=search_text).click()
        response = browser.find_elements(by=By.CLASS_NAME, value="blog")[0].text
        
        #assert
        assert search_text in response
        browser.close()
