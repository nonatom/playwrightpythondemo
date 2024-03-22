from playwright.sync_api import Page


class HiddenLayersPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/hiddenlayers")

        self.green_button = self.page.locator("button#greenButton")

    def click_green_button(self, timeout=30000):
        self.green_button.click(timeout=timeout)
