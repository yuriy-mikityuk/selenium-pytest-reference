import base64

import pytest
from selenium.webdriver.common.print_page_options import PrintOptions
from io import BytesIO
from pypdf import PdfReader

def test_print_page(web_form_page):
    pdf_base64 = web_form_page.print_page()
    pdf_bytes = base64.b64decode(pdf_base64)

    assert pdf_bytes.startswith(b"%PDF")

def test_print_page_with_options(web_form_page):
    settings = PrintOptions()
    settings.orientation = "landscape"

    pdf_base64 = web_form_page.print_page(print_options=settings)

    pdf_bytes = base64.b64decode(pdf_base64)
    reader = PdfReader(BytesIO(pdf_bytes))
    first_page = reader.pages[0]

    width = float(first_page.mediabox.width)
    height = float(first_page.mediabox.height)

    assert width > height

def test_print_page_with_custom_size(web_form_page):
    settings = PrintOptions()
    width_cm = 10
    height_cm = 20

    settings.page_width = width_cm
    settings.page_height = height_cm

    pdf_base64 = web_form_page.print_page(print_options=settings)

    pdf_bytes = base64.b64decode(pdf_base64)
    reader = PdfReader(BytesIO(pdf_bytes))
    first_page = reader.pages[0]

    actual_width_points = float(first_page.mediabox.width)
    actual_height_points = float(first_page.mediabox.height)

    expected_width_points = width_cm / 2.54 * 72
    expected_height_points = height_cm / 2.54 * 72

    assert actual_width_points == pytest.approx(expected_width_points, abs=1)
    assert actual_height_points == pytest.approx(expected_height_points, abs=1)