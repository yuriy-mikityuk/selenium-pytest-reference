def test_hover_over_area(mouse_interaction_page):
    mouse_interaction_page.hover_over_area()
    expected_text = "hovered"
    assert mouse_interaction_page.status.get_text() == expected_text


def test_drag_and_drop(mouse_interaction_page):
    mouse_interaction_page.drag_and_drop()
    expected_text = "dropped"
    assert mouse_interaction_page.dropped_text.get_text() == expected_text


def test_drag_and_drop_by_actions(mouse_interaction_page):
    mouse_interaction_page.drag_and_drop_by_actions()
    expected_text = "dropped"
    assert mouse_interaction_page.dropped_text.get_text() == expected_text


def test_context_click(mouse_interaction_page):
    mouse_interaction_page.context_click_element()
    expected_text = "context-clicked"
    assert mouse_interaction_page.click_status.get_text() == expected_text


def test_double_click(mouse_interaction_page):
    mouse_interaction_page.double_click_element()
    expected_text = "double-clicked"
    assert mouse_interaction_page.click_status.get_text() == expected_text
