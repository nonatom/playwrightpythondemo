from models.progress_bar_page import ProgressBarPage
from playwright.sync_api import expect, Page


def test_progress_bar(page: Page):
    progress_bar_page = ProgressBarPage(page)
    progress_bar_page.click_start_button()
    progress_bar_page.click_stop_button_at_percentage(75)
    assert progress_bar_page.current_progress >= 75
