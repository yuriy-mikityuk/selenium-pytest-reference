from framework.pages.bidi_network_page import BidiNetworkPage
from framework.bidi.request_collector import RequestCollector

def test_bidi_intercepts_navigation(bidi_network_page: BidiNetworkPage):
    page = bidi_network_page

    with RequestCollector(page.driver, [page.URL], timeout=10) as requests:
        page.open_via_bidi()
        requests.wait_for(1)

    assert requests[0].url == page.URL
    assert requests[0].method == "GET"
