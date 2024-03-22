from models.dynamic_table_page import DynamicTablePage
from playwright.sync_api import Page, expect


def test_chrome_cpu_values(page: Page):
    dynamic_table_page = DynamicTablePage(page)
    expect(dynamic_table_page.chrome_cpu).to_have_text(dynamic_table_page.percentage)