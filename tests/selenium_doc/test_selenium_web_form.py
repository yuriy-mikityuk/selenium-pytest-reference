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
    # Checked is on
    assert web_form_page.checked_checkbox.is_checked()
    # Default is off
    assert not web_form_page.default_checkbox.is_checked()

    expected_state = True
    web_form_page.default_checkbox.set_checked(expected_state)
    actual_state = web_form_page.default_checkbox.is_checked()

    assert actual_state == expected_state

    web_form_page.checked_checkbox.set_checked(False)
    assert not web_form_page.checked_checkbox.is_checked()

def test_select_radio_button(web_form_page):
    assert web_form_page.checked_radio.is_selected()
    assert not web_form_page.default_radio.is_selected()

    web_form_page.default_radio.select()
    assert not web_form_page.checked_radio.is_selected()
    assert web_form_page.default_radio.is_selected()


def test_send_keys_to_text_area(web_form_page):
    expected_text = "Second"
    web_form_page.send_keys_to_text_area(expected_text)
    assert web_form_page.text_area.get_value() == expected_text

def test_upload_file(web_form_page):
    web_form_page.upload_file("README.md")
    assert web_form_page.file_input.get_value() == r"C:\fakepath\README.md"

def test_type_uppercase_text(web_form_page):
    expected_text = "SECOND"
    web_form_page.type_uppercase_text("second")
    assert web_form_page.text_area.get_value() == expected_text

def test_select_all_and_replace(web_form_page):
    initial_text = "Initial"
    replaced_text = "Replaced"
    web_form_page.text_input.fill(initial_text)
    web_form_page.select_all_and_replace(replaced_text)
    assert web_form_page.text_input.get_value() == replaced_text

def test_scroll_to_element(web_form_page):
    web_form_page.return_to_index_link.scroll_into_view()
    assert web_form_page.return_to_index_link.is_displayed()

def test_find_element_below(web_form_page):
    password_input = web_form_page.get_password_input_attribute("name")
    assert password_input == "my-password"
    assert web_form_page.get_password_input_attribute("type") == "password"

def test_disabled_input(web_form_page):
    assert not web_form_page.disabled_input.is_enabled()
    assert web_form_page.disabled_input.get_attribute("disabled") == "true"

def test_readonly_input(web_form_page):
    assert web_form_page.readonly_input.is_enabled()
    assert web_form_page.readonly_input.get_attribute("readonly") is not None
    assert web_form_page.readonly_input.get_value() == "Readonly input"

