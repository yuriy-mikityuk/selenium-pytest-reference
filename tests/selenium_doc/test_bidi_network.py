from framework.pages.bidi_network_page import BidiNetworkPage
from framework.bidi.request_collector import RequestCollector

def test_firefox_bidi_intercepts_navigation(firefox_bidi_driver):
    page = BidiNetworkPage(firefox_bidi_driver)

    with RequestCollector(firefox_bidi_driver, [page.URL], timeout=10) as requests:
        page.open()
        requests.wait_for(1)

    assert requests[0].url == page.URL
    assert requests[0].method == "GET"
