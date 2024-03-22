from playwright.sync_api import Page


class ScrollbarsPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/scrollbars")

        self.hidden_button = self.page.get_by_role("button", name="Hiding Button")

    def scroll_button_into_view(self):
        self.hidden_button.scroll_into_view_if_needed()
