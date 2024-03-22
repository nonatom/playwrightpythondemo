from playwright.sync_api import Page


class SampleAppPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/sampleapp")

        self.user_textbox = self.page.get_by_placeholder("User Name")
        self.password_textbox = self.page.get_by_placeholder("********")
        self.login_button = self.page.get_by_role("button", name="Log In")
        self.label = self.page.locator("label#loginstatus")

    def login(self, username: str, password: str):
        self.user_textbox.fill(username)
        self.password_textbox.fill(password)
        self.login_button.click()
