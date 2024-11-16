from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    PHONE_OS_LOCATOR = (By.CSS_SELECTOR, ".phone-os")
    PHONE_SCREEN_SIZE_LOCATOR = (By.CSS_SELECTOR, ".phone-screen-size")
    PHONE_SCREEN_DIMENSION_LOCATOR = (By.CSS_SELECTOR, ".phone-screen-dimension")
    PHONE_RAM_LOCATOR = (By.CSS_SELECTOR, ".phone-ram")
    PHONE_MEMORY_LOCATOR = (By.CSS_SELECTOR, ".phone-memory")

    def verify_phone_parameters(self, phone):
        phone_data = {
            "os": phone.find_element(*self.PHONE_OS_LOCATOR).text,
            "screen_size": phone.find_element(*self.PHONE_SCREEN_SIZE_LOCATOR).text,
            "screen_dimension": phone.find_element(*self.PHONE_SCREEN_DIMENSION_LOCATOR).text,
            "ram": phone.find_element(*self.PHONE_RAM_LOCATOR).text,
            "memory": phone.find_element(*self.PHONE_MEMORY_LOCATOR).text,
        }

        return all([
            phone_data["os"] == self.find_element(self.PHONE_OS_LOCATOR).text,
            phone_data["screen_size"] == self.find_element(self.PHONE_SCREEN_SIZE_LOCATOR).text,
            phone_data["screen_dimension"] == self.find_element(self.PHONE_SCREEN_DIMENSION_LOCATOR).text,
            phone_data["ram"] == self.find_element(self.PHONE_RAM_LOCATOR).text,
            phone_data["memory"] == self.find_element(self.PHONE_MEMORY_LOCATOR).text,
        ])
