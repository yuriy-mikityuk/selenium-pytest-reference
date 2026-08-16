def test_switch_to_new_window(windows_page):
    expected_text_new_window = "Simple page with simple test."
    current_window = windows_page.current_window_handle()

    simple_page = windows_page.open_new_window()
    new_window = windows_page.current_window_handle()
    assert new_window != current_window

    new_window_text = simple_page.page_text.get_text()
    assert new_window_text == expected_text_new_window

    windows_page.close_current_window()
    windows_page.switch_to_window(current_window)

    assert windows_page.get_number_of_windows() == 1
    assert windows_page.current_window_handle() == current_window
    assert windows_page.link_to_new_window.is_displayed()
