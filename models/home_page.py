from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):

        self.page = page
        self.page.goto("http://uitestingplayground.com")

        self.dynamic_id_link = page.get_by_role("link", name="Dynamic ID")
        self.class_attribute_link = page.get_by_role("link", name="Class Attribute")
        self.hidden_layers_link = page.get_by_role("link", name="Hidden Layers")
        self.load_delay_link = page.get_by_role("link", name="Load Delay")
        self.ajax_data_link = page.get_by_role("link", name="AJAX Data")
        self.client_side_delay_link = page.get_by_role("link", name="Client Side Delay")
        self.click_link = page.get_by_role("link", name="Click")
        self.text_input_link = page.get_by_role("link", name="Text Input")
        self.scrollbars_link = page.get_by_role("link", name="Scrollbars")
        self.dynamic_table_link = page.get_by_role("link", name="Dynamic Table")
        self.verify_text_link = page.get_by_role("link", name="Verify Text")
        self.progress_bar_link = self.page.get_by_role("link", name="Progress Bar")
        self.visibility_link = page.get_by_role("link", name="Visibility")
        self.sample_app_link = page.get_by_role("link", name="Sample App")
        self.mouse_over_link = page.get_by_role("link", name="Mouse Over")
        self.nonbreaking_space_link = page.get_by_role("link", name="Non-breaking Space")
        self.overlapped_element_link = page.get_by_role("link", name="Overlapped Element")
        self.shadow_dom_link = page.get_by_role("link", name="Shadow DOM")




    def click_dynamic_id_link(self):
        self.dynamic_id_link.click()

    def click_class_attribute_link(self):
        self.class_attribute_link.click()

    def click_hidden_layers_link(self):
        self.hidden_layers_link.click()

    def click_load_delay_link(self):
        self.load_delay_link.click()

    def click_ajax_data_link(self):
        self.ajax_data_link.click()

    def click_client_side_delay_link(self):
        self.client_side_delay_link.click()

    def click_click_link(self):
        self.click_link.click()

    def click_text_input_link(self):
        self.text_input_link.click()

    def click_scrollbars_link(self):
        self.scrollbars_link.click()

    def click_dynamic_table_link(self):
        self.dynamic_table_link.click()

    def click_verify_text_link(self):
        self.verify_text_link.click()

    def click_progress_bar_link(self):
        self.progress_bar_link.click()

    def click_visibility_link(self):
        self.visibility_link.click()

    def click_sample_app_link(self):
        self.sample_app_link.click()

    def click_mouse_over_link(self):
        self.mouse_over_link.click()

    def click_nonbreaking_space_link(self):
        self.nonbreaking_space_link.click()

    def click_overlapped_element_link(self):
        self.overlapped_element_link.click()

    def click_shadow_dom_link(self):
        self.shadow_dom_link.click()