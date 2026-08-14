def test_fill_inputs(web_form_page):
    expected_text = "First"  # Arrange
    expected_received_text = "Received!"
    web_form_page.text_input.fill(expected_text)  # Act

    assert web_form_page.text_input.get_value() == expected_text  # Assert

    submitted_form_page = web_form_page.submit()
    assert (
            submitted_form_page.received_text.get_text()
            == expected_received_text
    )

def test_choose_dropdown_option(web_form_page):
    expected_option = "Two"
    web_form_page.dropdown_options.choose_option_in_dropdown(expected_option)
    actual_option = web_form_page.dropdown_options.read_actual_dropdown()

    assert actual_option == expected_option

def test_set_checkbox_state(web_form_page):
    # Default is on
    assert web_form_page.checked_checkbox.is_checked()
    # Checked is off
    assert not web_form_page.default_checkbox.is_checked()

    expected_state = True
    web_form_page.default_checkbox.set_checked(expected_state)
    actual_state = web_form_page.default_checkbox.is_checked()

    assert actual_state == expected_state

    web_form_page.checked_checkbox.set_checked(False)
    assert not web_form_page.checked_checkbox.is_checked()