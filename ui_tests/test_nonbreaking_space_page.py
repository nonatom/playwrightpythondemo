from models.nonbreaking_space_page import NonbreakingSpacePage
from playwright.sync_api import Page


def test_nbsp(page: Page):
    nonbreaking_space_page = NonbreakingSpacePage(page)
    nonbreaking_space_page.click_button()
