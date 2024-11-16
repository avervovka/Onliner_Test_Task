from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.timeout = 10

    def find_element(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator):
        try:
            element = WebDriverWait(self.browser, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False
