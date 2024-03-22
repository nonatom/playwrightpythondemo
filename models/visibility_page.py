from playwright.sync_api import Page


class VisibilityPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/visibility")

        self.hide_button = self.page.get_by_role("button", name="Hide")
        self.removed_button = self.page.get_by_role("button", name="Removed")
        self.zero_width_button = self.page.get_by_role("button", name="Zero Width")
        self.overlapped_button = self.page.get_by_role("button", name="Overlapped")
        self.opacity_0_button = self.page.get_by_role("button", name="Opacity 0")
        self.visibility_hidden_button = self.page.get_by_role("button", name="Visibility Hidden")
        self.display_none_button = self.page.get_by_role("button", name="Display None")
        self.offscreen_button = self.page.get_by_role("button", name="Offscreen")

    def click_hide_button(self):
        self.hide_button.click()

    def click_overlapped_button(self):
        self.overlapped_button.click(timeout=2000)
