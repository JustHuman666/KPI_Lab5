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

