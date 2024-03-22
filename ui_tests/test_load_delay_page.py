from models.load_delay_page import LoadDelayPage
from playwright.sync_api import expect, Page


def test_load_delay(page: Page):
    load_delay_page = LoadDelayPage(page)
    expect(load_delay_page.button).to_be_visible()
