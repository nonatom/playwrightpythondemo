from playwright.sync_api import Page


class TextInputPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/textinput")

        self.text_box = self.page.get_by_label("Set New Button Name")
        self.button = self.page.locator("button.btn-primary")

    def input_text(self, text: str):
        self.text_box.fill(text)

    def click_button(self):
        self.button.click()
