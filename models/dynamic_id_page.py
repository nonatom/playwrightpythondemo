from playwright.sync_api import Page


class DynamicIdPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/dynamicid")

        self.button = self.page.get_by_role("button", name="Button with Dynamic ID")