import pytest
from models.shadow_dom_page import ShadowDomPage
from playwright.sync_api import expect, Browser


@pytest.mark.skip(reason="Cannot grant clipboard permissions on http")
def test_guid_generator(browser: Browser):
    context = browser.new_context()
    context.grant_permissions(["clipboard-read"])
    page = context.new_page()

    shadow_dom_page = ShadowDomPage(page)
    shadow_dom_page.click_generate_button()
    shadow_dom_page.click_copy_button()
    textfield_text = shadow_dom_page.text_field.input_value()
    clipboard_text = shadow_dom_page.get_clipboard_text()
    expect(clipboard_text).to_have_value(textfield_text)
