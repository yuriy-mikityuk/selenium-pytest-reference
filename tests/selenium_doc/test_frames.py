from framework.pages.simple_page import SimplePage

def test_switch_to_frame(windows_page):
    windows_page.switch_to_frame("myframe")
    expected_text = "Simple page with simple test."

    simple_page = SimplePage(windows_page.driver)
    assert simple_page.page_text.get_text()  == expected_text
    windows_page.switch_to_default_content()
    assert windows_page.link_to_new_window.is_displayed()
