import pytest
from models.hidden_layers_page import HiddenLayersPage
from playwright.sync_api import TimeoutError, Page


def test_cannot_click_hidden_button(page: Page):
    hidden_layers_page = HiddenLayersPage(page)
    hidden_layers_page.click_green_button()

    with pytest.raises(TimeoutError):
        hidden_layers_page.click_green_button(timeout=2000)
