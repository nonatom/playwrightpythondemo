from models.dynamic_id_page import DynamicIdPage
from playwright.sync_api import expect, Page


def test_click_dynamic_id_button(page: Page):
    dynamic_id_page = DynamicIdPage(page)
    button = dynamic_id_page.button
    expect(button).to_be_visible()
    button.click()
