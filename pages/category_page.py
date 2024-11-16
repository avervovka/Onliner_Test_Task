import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from selenium.webdriver.support.ui import Select


class CategoryPage(BasePage):
    CATEGORY_URL = "https://catalog.onliner.by/mobile"
    # PHONE_LOCATOR = (By.CSS_SELECTOR, ".phone-item")
    ACCEPT_COOKIES_BUTTON_LOCATOR = (By.XPATH, "//*[@id='submit-button']")
    COMPARE_BUTTON_LOCATOR = (By.XPATH, '//*[@id="container"]/div/div/div/div/div[3]/div/div/div[1]/a')
    # PHONE_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, ".phone-item input[type='checkbox']")
    PHONE_1_LOCATOR = (By.XPATH,
                       '//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[3]/div[2]/div/div[1]')
    PHONE_2_LOCATOR = (By.XPATH,
                       '//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[3]/div[2]/div/div[4]')
    CHECKBOX_1_LOCATOR = (By.CSS_SELECTOR,
                          '#container > div > div > div > div > div.catalog-content > div.catalog-wrapper > div > div > div.catalog-form__tabs > div > div > div > div > div.catalog-form__filter-part.catalog-form__filter-part_2 > div.catalog-form__offers > div > div:nth-child(1) > div > div > div.catalog-form__offers-part.catalog-form__offers-part_image > label')
    CHECKBOX_2_LOCATOR = (By.CSS_SELECTOR,
                          '#container > div > div > div > div > div.catalog-content > div.catalog-wrapper > div > div > div.catalog-form__tabs > div > div > div > div > div.catalog-form__filter-part.catalog-form__filter-part_2 > div.catalog-form__offers > div > div:nth-child(4) > div > div > div.catalog-form__offers-part.catalog-form__offers-part_image > label')
    phone_price = (By.CSS_SELECTOR,
                   'div.catalog-form__offers-part.catalog-form__offers-part_control > div.catalog-form__description.catalog-form__description_huge-additional.catalog-form__description_font-weight_bold.catalog-form__description_condensed-other.catalog-form__description_primary > a > span:nth-child(2)')
    screen_size = (By.CSS_SELECTOR,
                   'div.catalog-form__parameter.catalog-helpers_hide_tablet > div > div.catalog-form__parameter-part.catalog-form__parameter-part_1 > div:nth-child(2)')
    min_price_field = (By.XPATH,
                       '//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[2]/div[2]/div[12]/div/div/div[2]/div[2]/div/div[1]/input')
    max_price_field = (By.XPATH,
                       '//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[2]/div[2]/div[12]/div/div/div[2]/div[2]/div/div[2]/input')
    min_screen_size = (By.XPATH, '//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[2]/div[2]/div[20]/div/div[2]/div[2]/div[2]/div/div[1]/div/select')

    max_screen_size = (By.XPATH,
                       '//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[2]/div[2]/div[20]/div/div[2]/div[2]/div[2]/div/div[2]/div/select')

    def open(self):
        self.browser.get(self.CATEGORY_URL)

    def is_opened(self):
        return "Мобильный" in self.browser.title

    def find_and_click_cookies_message(self):
        time.sleep(2)
        self.click_element(self.ACCEPT_COOKIES_BUTTON_LOCATOR)
        time.sleep(2)

    def add_two_phones_to_compare(self):
        self.first_phone_checkbox = self.find_element(self.CHECKBOX_1_LOCATOR)
        self.second_phone_checkbox = self.find_element(self.CHECKBOX_2_LOCATOR)
        self.click_element(self.CHECKBOX_1_LOCATOR)
        time.sleep(2)
        self.click_element(self.CHECKBOX_2_LOCATOR)
        first_phone = self.find_element(self.PHONE_1_LOCATOR)
        second_phone = self.find_element(self.PHONE_2_LOCATOR)
        return first_phone, second_phone

    def is_compare_link_visible(self):
        return self.is_element_visible(self.COMPARE_BUTTON_LOCATOR)

    def are_phones_checked(self):
        return self.first_phone_checkbox.get_attribute(
            "title") == "В сравнении" and self.second_phone_checkbox.get_attribute("title") == "В сравнении"

    def set_search_parameters(self, phones):
        phone_prices = []
        phone_screen_size = []
        for phone in phones:
            by, value = self.phone_price
            phone_prices.append(float(phone.find_element(by, value).text.replace(',', '.')[:-3]))

            by, value = self.screen_size
            phone_screen_size.append(int(phone.find_element(by, value).text.replace('.', '')[6:9]))

        self.enter_text(self.min_price_field, min(phone_prices))
        time.sleep(5)
        self.enter_text(self.max_price_field, max(phone_prices))
        time.sleep(2)

        # dropdown menu - PROBLEM!!!!
        # if self.is_element_presented(self.min_screen_size):
        #     self.script_scroll_to_element(self.min_screen_size)
        # self.select_and_set_dropdown(self.min_screen_size, 'qwerty')
        # self.is_element_clickable(self.min_screen_size)
        # self.click_element(self.min_screen_size)
        # time.sleep(5)
        # self.click_element(self.max_screen_size)

        #min_dropdown_element = self.find_element(self.min_screen_size)
        #min_dropdown_element.click()
        #min_dropdown_elements = self.find_elements(self.min_screen_size)
        #print(min_dropdown_elements)
#
        #select = Select(min_dropdown_elements)
        #select.select_by_value(str(min(phone_screen_size)))
        #time.sleep(5)

    def are_phones_still_displayed(self):
        # Check if selected phones are still visible on the page after setting filters
        phone_1 = self.is_element_visible(self.PHONE_1_LOCATOR)
        phone_2 = self.is_element_visible(self.PHONE_2_LOCATOR)
        phones = [phone_1, phone_2]
        return [True, False][False in phones]

    # def go_to_phone_1(self):
    #     self.click_element(self.PHONE_1_LOCATOR)
    #     time.sleep(10)
    # #     # return ProductPage(self.browser)

    def click_compare_link(self):
        self.click_element(self.COMPARE_BUTTON_LOCATOR)
        from pages.compare_page import ComparePage
        return ComparePage(self.browser)
