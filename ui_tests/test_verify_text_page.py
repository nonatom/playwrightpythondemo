from models.verify_text_page import VerifyTextPage
from playwright.sync_api import expect, Page


def test_verify_text(page: Page):
    verify_text_page = VerifyTextPage(page)
    expect(verify_text_page.text).to_contain_text("Welcome")
