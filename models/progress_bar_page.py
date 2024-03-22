from playwright.sync_api import Page


class ProgressBarPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/progressbar")

        self.progress_bar = self.page.get_by_role("progressbar")
        self.start_button = self.page.get_by_role("button", name="Start")
        self.stop_button = self.page.get_by_role("button", name="Stop")
        self.current_progress = int(self.progress_bar.get_attribute("aria-valuenow"))

    def click_start_button(self):
        self.start_button.click()

    def click_stop_button_at_percentage(self, percentage):
        while True:
            self.current_progress = int(self.progress_bar.get_attribute("aria-valuenow"))
            if self.current_progress >= percentage:
                break
            else:
                print(f"Progress: {self.current_progress}%")

        self.stop_button.click()
