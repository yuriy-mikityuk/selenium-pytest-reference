def test_pen_input(pen_page):
    pen_page.draw_with_pen()
    assert "pointerType: pen" in pen_page.pointer_down.get_text()

def test_pen_properties(pen_page):
    pen_page.draw_with_pen(
        tilt_x=-72,
        tilt_y=9,
        twist=86,
    )
    assert "tiltX: -72" in pen_page.second_pointer_move.get_text()
    assert "tiltY: 9" in pen_page.second_pointer_move.get_text()
    assert "twist: 86" in pen_page.second_pointer_move.get_text()