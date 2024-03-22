import pytest
from models.visibility_page import VisibilityPage
from playwright.sync_api import expect, Page, TimeoutError


def test_buttons_visibility(page: Page):
    visibility_page = VisibilityPage(page)
    visibility_page.click_hide_button()

    expect(visibility_page.removed_button).to_be_hidden()
    expect(visibility_page.zero_width_button).to_have_css("width", "0px")
    with pytest.raises(TimeoutError):
        visibility_page.click_overlapped_button()
    expect(visibility_page.opacity_0_button).to_have_css("opacity", "0")
    expect(visibility_page.visibility_hidden_button).to_be_hidden()
    expect(visibility_page.display_none_button).to_be_hidden()
    expect(visibility_page.offscreen_button).not_to_be_in_viewport()
