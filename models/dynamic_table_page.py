from playwright.sync_api import Page


class DynamicTablePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/dynamictable")

        self.label = self.page.locator("p.bg-warning").inner_text()
        self.percentage = self.label.split()[-1]

        self.column_headers = self.page.get_by_role("columnheader")

        for index in range(self.column_headers.count()):
            self.column_header = self.column_headers.nth(index)

            if self.column_header.inner_text() == "CPU":
                self.cpu_column = index
                break

        self.row_group = self.page.get_by_role("rowgroup").last
        self.chrome_row = self.row_group.get_by_role("row").filter(
            has_text="Chrome"
        )

        self.chrome_cpu = self.chrome_row.get_by_role("cell").nth(self.cpu_column)