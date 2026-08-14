def test_simple_alert(alerts_page):
    expected_text = "cheese"

    alert = alerts_page.open_simple_alert()
    assert alert.text == expected_text
    alert.accept()


def test_confirm_alert(alerts_page):
    expected_text = "Are you sure?"

    alert = alerts_page.open_confirm_alert()
    assert alert.text == expected_text
    alert.dismiss()


def test_prompt_alert(alerts_page):
    expected_text = "Enter something"

    alert = alerts_page.open_prompt_alert()
    assert alert.text == expected_text
    alert.send_keys("cheese")
    alert.accept()
