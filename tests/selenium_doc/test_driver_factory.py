def test_driver_sessions_keep_cookies_separate(web_form_factory):
    cookie_name = "factory_user"

    alice_page = web_form_factory()
    bob_page = web_form_factory()

    alice_page.cookies.set(cookie_name, "alice")
    assert alice_page.cookies.get(cookie_name) == "alice"

    assert bob_page.cookies.get(cookie_name) is None

    bob_page.cookies.set(cookie_name, "bob")
    assert bob_page.cookies.get(cookie_name) == "bob"

    assert alice_page.cookies.get(cookie_name) == "alice"
