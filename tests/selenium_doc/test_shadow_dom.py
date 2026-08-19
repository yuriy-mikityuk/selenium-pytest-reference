def test_shadow_dom_checkbox_click(shadow_root_page):
    checkbox = shadow_root_page.get_shadow_checkbox()

    # До клика чекбокс не выбран
    assert not checkbox.is_selected()

    # Кликаем по элементу внутри Shadow Root
    checkbox.click()

    # После клика чекбокс выбран
    assert checkbox.is_selected()