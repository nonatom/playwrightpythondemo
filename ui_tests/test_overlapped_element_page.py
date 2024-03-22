from models.overlapped_element_page import OverlappedElementPage
from playwright.sync_api import Page, expect


def test_overlapped_element(page: Page):
    overlapped_element_page = OverlappedElementPage(page)
    overlapped_element_page.input_field_text("Hello")
    expect(overlapped_element_page.name_input).to_have_value("Hello")
