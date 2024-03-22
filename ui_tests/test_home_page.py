from models.home_page import HomePage
from playwright.sync_api import expect, Page


def test_dynamic_id_link(page: Page):
    home_page = HomePage(page)
    home_page.click_dynamic_id_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/dynamicid")


def test_class_attribute_link(page: Page):
    home_page = HomePage(page)
    home_page.click_class_attribute_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/classattr")


def test_hidden_layers_link(page: Page):
    home_page = HomePage(page)
    home_page.click_hidden_layers_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/hiddenlayers")


def test_load_delay_link(page: Page):
    home_page = HomePage(page)
    home_page.click_load_delay_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/loaddelay")


def test_ajax_data_link(page: Page):
    home_page = HomePage(page)
    home_page.click_ajax_data_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/ajax")


def test_client_side_delay_link(page: Page):
    home_page = HomePage(page)
    home_page.click_client_side_delay_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/clientdelay")


def test_click_link(page: Page):
    home_page = HomePage(page)
    home_page.click_click_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/click")


def test_text_input_link(page: Page):
    home_page = HomePage(page)
    home_page.click_text_input_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/textinput")


def test_scrollbars_link(page: Page):
    home_page = HomePage(page)
    home_page.click_scrollbars_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/scrollbars")


def test_dynamic_table_link(page: Page):
    home_page = HomePage(page)
    home_page.click_dynamic_table_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/dynamictable")


def test_verify_text_link(page: Page):
    home_page = HomePage(page)
    home_page.click_verify_text_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/verifytext")


def test_progress_bar_link(page: Page):
    home_page = HomePage(page)
    home_page.click_progress_bar_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/progressbar")


def test_visibility_link(page: Page):
    home_page = HomePage(page)
    home_page.click_visibility_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/visibility")


def test_sample_app_link(page: Page):
    home_page = HomePage(page)
    home_page.click_sample_app_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/sampleapp")


def test_mouse_over_link(page: Page):
    home_page = HomePage(page)
    home_page.click_mouse_over_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/mouseover")


def test_nonbreaking_space_link(page: Page):
    home_page = HomePage(page)
    home_page.click_nonbreaking_space_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/nbsp")


def test_overlapped_element_link(page: Page):
    home_page = HomePage(page)
    home_page.click_overlapped_element_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/overlapped")


def test_shadow_dom_link(page: Page):
    home_page = HomePage(page)
    home_page.click_shadow_dom_link()
    expect(home_page.page).to_have_url("http://uitestingplayground.com/shadowdom")