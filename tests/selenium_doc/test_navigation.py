from framework.pages.windows_page import WindowsPage

def test_refresh_resets_input(web_form_page):
    expected_text = "Second"
    web_form_page.send_keys_to_text_area(expected_text)
    assert web_form_page.text_area.get_value() == expected_text
    web_form_page.refresh()
    assert web_form_page.text_area.get_value() == ""


def test_back_and_forward_navigation(web_form_page):
    windows_page = WindowsPage(web_form_page.driver)
    windows_page.open()

    windows_page.back()
    assert web_form_page.file_input.is_displayed(), "File input should be displayed after back navigation"

    web_form_page.forward()
    assert windows_page.link_to_new_window.is_displayed(), "Link to new window should be displayed after forward navigation"
