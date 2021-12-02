from BaseApp import BasePage
from selenium.webdriver.common.by import By

class YakabooLocators:
    LOCATOR_YAKABOO_SEARCH_FIELD = (By.ID, 'search')
    LOCATOR_YAKABOO_GET_RESPONSE_FOR_WRONG = (By.CLASS_NAME, 'note-msg')
    LOCATOR_YAKABOO_LINK_BUTTON = (By.LINK_TEXT, 'Акції')
    LOCATOR_YAKABOO_GET_RESPONSE_FOR_LINK = (By.CLASS_NAME, 'blog')


class RequestHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YakabooLocators.LOCATOR_YAKABOO_SEARCH_FIELD)
        search_field.send_keys(word)
        return search_field

    def submit_request(self, search_field):
        return search_field.submit()

    def click_on_button(self, search_field):
        return search_field.click()

    def get_error_response(self):
        return self.find_element(YakabooLocators.LOCATOR_YAKABOO_GET_RESPONSE_FOR_WRONG).text

    def find_link_by_name(self):
        return self.find_element(YakabooLocators.LOCATOR_YAKABOO_LINK_BUTTON)

    def get_response_for_clicked_link(self):
        return self.find_elements(YakabooLocators.LOCATOR_YAKABOO_GET_RESPONSE_FOR_LINK)[0].text

    
