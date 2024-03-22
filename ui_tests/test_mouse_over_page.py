from models.mouse_over_page import MouseOverPage
from playwright.sync_api import expect, Page


def test_mouse_over_state(page: Page):
    mouse_over_page = MouseOverPage(page)
    mouse_over_page.click_active_link(2)
    expect(mouse_over_page.click_count).to_have_text("2")
