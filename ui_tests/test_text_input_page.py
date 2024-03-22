from models.text_input_page import TextInputPage
from playwright.sync_api import expect, Page


def test_input_text(page: Page):
    text_input_page = TextInputPage(page)
    text = "Hello"
    text_input_page.input_text(text)
    text_input_page.click_button()
    expect(text_input_page.button).to_have_text(text)
