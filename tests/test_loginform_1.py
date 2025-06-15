import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://berpress.github.io/selenium-login-demo/"

@pytest.mark.skip
class TestLoginform:
    def test_loginform_add_valid(self):
        """Открыть страницу"""

        driver = webdriver.Chrome()
        driver.get(URL)

        """Найти элементы"""
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.ID, 'login-btn')

        """Ввод логина и пароля"""
        username.send_keys('admin')
        password.send_keys('password')

        """Нажать кнопку Вход"""
        login_button.click()

        time.sleep(2)

        """Получаем текст результата ПОСЛЕ нажатия на кнопку"""
        result_text = driver.find_element(By.ID, 'result').text

        """Проверяем успешность входа"""
        assert result_text == 'Успешно! Вход выполнен.', f"Вход не выполнен успешно. Текст сообщения: '{result_text}'"

        """Закрываем драйвер"""
        driver.quit()

    def test_loginform_add_invalid_login(self):
        """Открыть страницу"""

        driver = webdriver.Chrome()
        driver.get(URL)

        """Найти элементы"""
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.ID, 'login-btn')

        """Ввод логина и пароля"""
        username.send_keys('abcde')
        password.send_keys('password')

        """Нажать кнопку Вход"""
        login_button.click()

        time.sleep(2)

        """Получаем текст результата ПОСЛЕ нажатия на кнопку"""
        result_text = driver.find_element(By.ID, 'result').text

        """Проверяем что вход не выполнен"""
        assert result_text == 'Ошибка: Неверный логин или пароль.', f"Неожиданный результат. Сообщение: '{result_text}'"

        """Закрываем драйвер"""
        driver.quit()

    def test_loginform_add_invalid_password(self):
        """Открыть страницу"""

        driver = webdriver.Chrome()
        driver.get(URL)

        """Найти элементы"""
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.ID, 'login-btn')

        """Ввод логина и пароля"""
        username.send_keys('admin')
        password.send_keys('password12345')

        """Нажать кнопку Вход"""
        login_button.click()

        time.sleep(2)

        """Получаем текст результата ПОСЛЕ нажатия на кнопку"""
        result_text = driver.find_element(By.ID, 'result').text

        """Проверяем что вход не выполнен"""
        assert result_text == 'Ошибка: Неверный логин или пароль.', f"Неожиданный результат. Сообщение: '{result_text}'"

        """Закрываем драйвер"""
        driver.quit()


