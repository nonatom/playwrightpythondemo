from models.class_attribute_page import ClassAttributePage
from playwright.sync_api import expect, Page


def test_click_dynamic_id_button(page: Page):
    class_attribute_page = ClassAttributePage(page)
    primary_btn = class_attribute_page.primary_btn
    expect(primary_btn).to_be_visible()
    primary_btn.click()
