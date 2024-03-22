from playwright.sync_api import Page


class OverlappedElementPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/overlapped")
        self.name_input = self.page.get_by_placeholder("Name")
        self.div = self.name_input.locator("..")

    def input_field_text(self, text: str):
        self.div.hover()
        self.page.mouse.wheel(0, 200)
        self.name_input.fill(text)
