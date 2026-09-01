def test_firefox_bidi_intercepts_navigation(firefox_bidi_network_page):
    request = firefox_bidi_network_page.capture_navigation_request()

    assert request.url == firefox_bidi_network_page.URL
    assert request.method == "GET"