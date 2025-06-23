import logging
from locators.login_form_locators import LoginformLocators
from pages.base_page import BasePage

logger = logging.getLogger("qa")

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        """Локаторы"""
        #self.driver = driver

    def add_login_page(self, username_text, password_text):
        logger.info(f'Try to add user {username_text}, {password_text}')
        self.fill(value=username_text, locator=LoginformLocators.USERNAME)
        self.fill(value=password_text, locator=LoginformLocators.PASSWORD)
        self.click(locator=LoginformLocators.LOGIN_BUTTON)
        return self

    def click_login_button(self):
        """Нажать кнопку входа"""
        self.click(locator=LoginformLocators.LOGIN_BUTTON)
        return self

    def get_result_text(self):
        """Получить текст результата авторизации"""
        return self.text(locator=LoginformLocators.RESULT_MESSAGE)

    def check_success_message(self):
        """Проверить сообщение об успешном входе"""
        result_text = self.get_result_text()
        expected_message = 'Успешно! Вход выполнен.'
        return result_text == expected_message

    def check_error_message(self):
        """Проверить сообщение об ошибке"""
        result_text = self.get_result_text()
        expected_error = 'Ошибка: Неверный логин или пароль.'
        return result_text == expected_error








