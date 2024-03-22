from models.sample_app_page import SampleAppPage
from playwright.sync_api import expect, Page


def test_successful_login(page: Page):
    sample_app_page = SampleAppPage(page)
    username = "User"
    password = "pwd"

    sample_app_page.login(username, password)
    expect(sample_app_page.label).to_have_text(f"Welcome, {username}!")


def test_unsuccessful_login(page: Page):
    sample_app_page = SampleAppPage(page)
    username = "User"
    password = "wrongpwd"

    sample_app_page.login(username, password)
    expect(sample_app_page.label).to_have_text("Invalid username/password")
