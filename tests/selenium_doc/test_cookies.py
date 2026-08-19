def test_add_and_get_cookie(web_form_page):
    web_form_page.add_cookie({"name": "foo", "value": "bar"})
    cookie = web_form_page.get_cookie("foo")
    assert cookie["value"] == "bar"

def test_delete_cookie(web_form_page):
    web_form_page.add_cookie({"name": "test_cookie", "value": "bar"})
    web_form_page.delete_cookie("test_cookie")
    assert web_form_page.get_cookie("test_cookie") is None


