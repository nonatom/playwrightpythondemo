from playwright.sync_api import Page


class VerifyTextPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/verifytext")

        self.text = self.page.locator("div.bg-primary").get_by_text("Welcome")