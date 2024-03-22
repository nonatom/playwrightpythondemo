from playwright.sync_api import Page


class NonbreakingSpacePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/nbsp")
        # \u00a0 is unicode for a non-breaking space
        self.button = self.page.locator("//button[text()='My\u00a0Button']")
    def click_button(self):
        self.button.click(timeout=2000)
