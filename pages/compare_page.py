from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ComparePage(BasePage):
    PHONE_NAMES_LOCATOR = (By.CSS_SELECTOR, ".phone-name")
    PHONE_PARAMETERS_LOCATOR = (By.CSS_SELECTOR, ".phone-parameters")

    def verify_phones_comparison(self, first_phone, second_phone):
        # Получаем список телефонов на странице сравнения
        phone_names = [element.text for element in self.find_elements(self.PHONE_NAMES_LOCATOR)]
        phone_parameters = [element.text for element in self.find_elements(self.PHONE_PARAMETERS_LOCATOR)]

        # Проверяем, что оба телефона присутствуют на странице сравнения
        assert first_phone.name in phone_names, f"{first_phone.name} не найден на странице сравнения"
        assert second_phone.name in phone_names, f"{second_phone.name} не найден на странице сравнения"

        # Проверяем, что параметры телефонов соответствуют ожиданиям
        first_phone_params = first_phone.get_parameters()
        second_phone_params = second_phone.get_parameters()

        for param in ["os", "screen_size", "screen_dimension", "ram", "memory"]:
            first_value = first_phone_params[param]
            second_value = second_phone_params[param]
            assert first_value != second_value, f"Параметр {param} одинаков для обоих телефонов, что не соответствует условию задачи"
            assert first_value in phone_parameters, f"Параметр {param} для {first_phone.name} не совпадает с указанным на странице сравнения"
            assert second_value in phone_parameters, f"Параметр {param} для {second_phone.name} не совпадает с указанным на странице сравнения"

        return True
