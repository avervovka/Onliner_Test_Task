from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


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

    def is_element_clickable(self, locator):
        try:
            element = WebDriverWait(self.browser, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except:
            return False

    def is_element_presented(self, locator):
        try:
            element = WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False

    def script_click_element(self, locator):
        element = self.find_element(locator)
        self.execute_script("arguments[0].click();", element)

    def script_scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView(true);", element)

    def execute_script(self, param, element):
        pass

    def select_and_set_dropdown(self, locator, text):
        select = Select(self.find_element(locator))
        options = select.options
        for option in options:
            if option.text == text:
                option.click()
