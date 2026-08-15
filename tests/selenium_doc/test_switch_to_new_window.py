def test_switch_to_new_window(windows_page):
    expected_text = "Simple page with simple test."
    current_window = windows_page.current_window_handle()

    simple_page = windows_page.open_new_window()
    new_window = windows_page.current_window_handle()
    assert new_window != current_window

    new_window_text = simple_page.text_in_new_window.get_text()
    assert new_window_text == expected_text
