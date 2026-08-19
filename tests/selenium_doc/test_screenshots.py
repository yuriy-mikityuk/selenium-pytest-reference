def test_page_screenshot_as_png(web_form_page):
    screenshot_as_png = web_form_page.get_screenshot_as_png()
    assert len(screenshot_as_png) > 0
    assert isinstance(screenshot_as_png, bytes)

def test_element_screenshot_save_file(web_form_page, tmp_path):
    file = tmp_path / "submit_btn.png"

    web_form_page.submit_button.take_screenshot(str(file))

    assert file.is_file()
    assert file.stat().st_size > 0
