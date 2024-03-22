from playwright.sync_api import Page


class LoadDelayPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/loaddelay")

        self.button = self.page.get_by_role("button", name="Button Appearing After Delay")
