from selenium.webdriver.common.by import By


class LoginformPage:
    def __init__(self, driver):
        self.driver = driver

    """Найти элементы"""
    def add_loginform(self, username_text, password_text):
        username = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')

        """Ввод логина и пароля"""
        username.send_keys(username_text)
        password.send_keys(password_text)
        return self

        """Нажать кнопку Вход"""
    def click_login_button(self):
        login_button = self.driver.find_element(By.ID, 'login-btn')
        login_button.click()

    """Получаем текст результата ПОСЛЕ нажатия на кнопку"""
    def get_result_text(self):

        result = self.driver.find_element(By.ID, 'result')
        return result.text

    """Сообщение об успешном входе"""
    def check_success_message(self):

        result_text = self.get_result_text()
        expected_message = 'Успешно! Вход выполнен.'

        return result_text == expected_message

    """Сообщение об ошибке"""
    def check_error_message(self):
        result_text = self.get_result_text()
        expected_error = 'Ошибка: Неверный логин или пароль.'

        return result_text == expected_error

