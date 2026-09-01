def test_scroll_to_button(scroll_page):
    # Before scroll page offset is 0
    assert scroll_page.execute_script("return window.scrollY;") == 0

    # Scroll to button 1
    scroll_page.button1.scroll_into_view()

    # After scroll page moves down
    assert scroll_page.execute_script("return window.scrollY;") != 0


def test_scroll_to_button_with_wheel_actions(scroll_page):
    assert scroll_page.execute_script("return window.scrollY;") == 0
    scroll_page.scroll_to_button_2_with_actions()
    assert scroll_page.execute_script("return window.scrollY;") > 0

def test_scroll_by_amount(scroll_page):
    assert scroll_page.execute_script("return window.scrollY;") == 0
    scroll_page.scroll_by_amount(100)
    assert scroll_page.execute_script("return window.scrollY;") == 100

def test_scroll_from_origin(scroll_page):
    assert scroll_page.execute_script("return window.scrollY;") == 0
    scroll_page.scroll_from_origin(origin_element=scroll_page.button1, delta_x=0, delta_y=100)
    assert scroll_page.execute_script("return window.scrollY;") > 0

