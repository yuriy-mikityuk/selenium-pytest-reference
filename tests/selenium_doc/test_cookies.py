def test_add_and_get_cookie(web_form_page):
    web_form_page.cookies.add_cookie({"name": "foo", "value": "bar"})
    cookie = web_form_page.cookies.get_cookie("foo")
    assert cookie["value"] == "bar"

def test_delete_cookie(web_form_page):
    web_form_page.cookies.add_cookie({"name": "test_cookie", "value": "bar"})
    web_form_page.cookies.delete("test_cookie")
    assert web_form_page.cookies.get_cookie("test_cookie") is None

def test_delete_all_cookies(web_form_page):
    web_form_page.cookies.add_cookie({"name": "test_cookie", "value": "bar"})
    web_form_page.cookies.add_cookie({"name": "test_cookie2", "value": "bar"})
    web_form_page.cookies.delete_all_cookies()
    assert web_form_page.cookies.get_cookies() == []

def test_cookie_same_site(web_form_page):
    web_form_page.cookies.add_cookie({"name": "strict_cookie", "value": "test", "sameSite": "Strict"})
    web_form_page.cookies.add_cookie({"name": "lax_cookie", "value": "test", "sameSite": "Lax"})
    assert web_form_page.cookies.get_cookie("strict_cookie")["sameSite"] == "Strict"
    assert web_form_page.cookies.get_cookie("lax_cookie")["sameSite"] == "Lax"

