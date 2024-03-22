from playwright.sync_api import Page


class MouseOverPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/mouseover")
        self.inactive_link = self.page.get_by_title("Click me")
        self.active_link = self.page.get_by_title("Active link")
        self.click_count = self.page.locator("span#clickCount")

    def click_active_link(self, count: int):
        self.inactive_link.hover()
        self.active_link.click(click_count=count)
