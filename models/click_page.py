from playwright.sync_api import Page


class ClickPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/click")

        self.button = self.page.get_by_role("button", name="Button That Ignores DOM Click Event")

    def click_button(self):
        self.button.click()
