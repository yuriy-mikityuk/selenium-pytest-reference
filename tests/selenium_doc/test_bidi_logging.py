def test_bidi_session_has_websocket(bidi_driver):
    assert bidi_driver.capabilities.get("webSocketUrl")

def test_capture_console_log(bidi_logging_page):
    entry = bidi_logging_page.capture_console_log()
    assert entry.text == "Hello, world!"

def test_capture_javascript_error(bidi_logging_page):
    entry = bidi_logging_page.capture_javascript_error()
    assert entry.text == "Error: Not working"
