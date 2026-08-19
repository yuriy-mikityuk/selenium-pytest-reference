def test_scroll_to_button(scroll_page):
    # Before scroll page offset is 0
    assert scroll_page.execute_script("return window.scrollY;") == 0

    # Scroll to button 1
    scroll_page.button1.scroll_into_view()

    # After scroll page moves down
    assert scroll_page.execute_script("return window.scrollY;") != 0
