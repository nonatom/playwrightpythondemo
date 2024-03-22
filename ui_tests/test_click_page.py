from models.click_page import ClickPage
from playwright.sync_api import expect, Page


def test_button_click(page: Page):
    click_page = ClickPage(page)
    click_page.click_button()
    expect(click_page.button).to_have_class("btn btn-success")
