def test_add_box(dynamic_page):
    count_before = dynamic_page.get_boxes_count()
    assert count_before == 0
    assert dynamic_page.add_box_button.is_displayed()

    dynamic_page.add_box()
    dynamic_page.add_box()
    assert dynamic_page.get_boxes_count() == count_before + 2

def test_reveal_input(dynamic_page):
    assert not dynamic_page.revealed_input.is_displayed()

    # Кликаем на кнопку добавить инпут
    dynamic_page.reveal_input()

    dynamic_page.revealed_input.fill("First")
    dynamic_page.revealed_input.fill('Selenium')
    assert dynamic_page.revealed_input.get_value() == "Selenium"






