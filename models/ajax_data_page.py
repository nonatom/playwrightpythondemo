from playwright.sync_api import Page


class AjaxDataPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/ajax")

        self.button = self.page.get_by_role("button", name="Button Triggering AJAX Request")
        self.ajax_data = self.page.locator("p.bg-success")

    def click_ajax_request_button(self):
        self.button.click()
