from models.scrollbars_page import ScrollbarsPage
from playwright.sync_api import expect, Page


def test_scrolling_to_view_button(page: Page):
    scrollbars_page = ScrollbarsPage(page)
    scrollbars_page.scroll_button_into_view()
    expect(scrollbars_page.hidden_button).to_be_visible()
