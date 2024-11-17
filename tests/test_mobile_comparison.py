import pytest
from pages.category_page import CategoryPage
# from pages.product_page import ProductPage
# from pages.compare_page import ComparePage
from utils.driver_factory import DriverFactory
# from utils.config import Config


@pytest.fixture(scope="session")
def browser():
    driver = DriverFactory.create_driver()
    yield driver
    driver.quit()


    # 1
def test_mobile_comparison(browser):
    category_page = CategoryPage(browser)
    category_page.open()
    assert category_page.is_opened(), "Category page did not open"

    # 2
    category_page = CategoryPage(browser)
    category_page.find_and_click_cookies_message()
    first_phone, second_phone = category_page.add_two_phones_to_compare()
    assert category_page.is_compare_link_visible(), "Compare link is not visible"
    assert category_page.are_phones_checked(), "Phones are not properly checked for comparison"

    # 3
    category_page.set_search_parameters([first_phone, second_phone])
    assert category_page.are_phones_still_displayed(), "Selected phones are not displayed after setting search parameters"
    assert category_page.are_phones_checked(), "Phones are not properly checked after setting search parameters"

    # 4
    # product_page = category_page.go_to_phone_1()
    #assert product_page.verify_phone_parameters(first_phone), "Phone parameters do not match"
#
    # 5
    #compare_page = category_page.click_compare_link()
    #assert compare_page.verify_phones_comparison(first_phone, second_phone), "Phones comparison is incorrect"


if __name__ == "__main__":
    pytest.main()
