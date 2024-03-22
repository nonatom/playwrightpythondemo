from playwright.sync_api import Page


class ShadowDomPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.bring_to_front()
        self.page.goto("http://uitestingplayground.com/shadowdom", wait_until="load")

        self.text_field = self.page.locator("#editField")
        self.generate_button = self.page.locator("button.button-generate")
        self.copy_button = self.page.locator("button.button-copy")

    def click_copy_button(self):
        self.copy_button.click()

    def click_generate_button(self):
        self.generate_button.click()

    def get_clipboard_text(self):
        return self.page.evaluate("navigator.clipboard.readText()")
