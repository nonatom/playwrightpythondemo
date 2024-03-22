from models.ajax_data_page import AjaxDataPage
from playwright.sync_api import expect, Page

def test_ajax_data_page(page: Page):
    ajax_data_page = AjaxDataPage(page)
    ajax_data_page.click_ajax_request_button()
    ajax_data_page.ajax_data.wait_for()
    expect(ajax_data_page.ajax_data).to_be_visible()
