from playwright.sync_api import Page


class ClassAttributePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/classattr")
        # CSS
        self.primary_btn = self.page.locator("button.btn-primary")
        # XPath
        # self.primary_btn = self.page.locator("//button[ contains(@class, 'btn-primary')]")
