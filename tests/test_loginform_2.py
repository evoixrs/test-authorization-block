import time

import pytest
from selenium import webdriver
from pages.loginform import LoginformPage

URL = "https://berpress.github.io/selenium-login-demo/"

@pytest.mark.skip
class TestLoginform2:
    def test_loginform_add_valid(self):

        """Открываем страницу"""
        driver = webdriver.Chrome()
        driver.get(URL)

        """Ввод логина и пароля + кнопка вход"""
        loginform_page = LoginformPage(driver)
        loginform_page.add_loginform(username_text='admin', password_text='password').click_login_button()

        """Сообщение об успешном входе"""
        assert loginform_page.check_success_message(), f"Вход не выполнен успешно. Текст сообщения: '{loginform_page.get_result_text()}'"

        """Закрываем драйвер"""
        driver.quit()

    def test_loginform_add_invalid_login(self):

        """Открываем страницу"""
        driver = webdriver.Chrome()
        driver.get(URL)

        """Ввод логина и пароля + кнопка вход"""
        loginform_page = LoginformPage(driver)
        loginform_page.add_loginform(username_text='abcde', password_text='password').click_login_button()

        """Сообщение что вход Не выполнен"""
        assert loginform_page.check_error_message(), f"Ожидалось сообщение об ошибке, но получено: '{loginform_page.get_result_text()}'"

        """Закрываем драйвер"""
        driver.quit()

    def test_loginform_add_invalid_password(self):

        """Открываем страницу"""
        driver = webdriver.Chrome()
        driver.get(URL)

        """Ввод логина и пароля + кнопка вход"""
        loginform_page = LoginformPage(driver)
        loginform_page.add_loginform(username_text='admin', password_text='password12345').click_login_button()

        """Сообщение что вход Не выполнен"""
        assert loginform_page.check_error_message(), f"Ожидалось сообщение об ошибке, но получено: '{loginform_page.get_result_text()}'"

        """Закрываем драйвер"""
        driver.quit()

