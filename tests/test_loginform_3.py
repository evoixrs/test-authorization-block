import time

import pytest


@pytest.mark.skip
class TestLoginform3:
    def test_loginform_add_valid(self, loginform_page):

        """Ввод логина и пароля + кнопка вход"""
        loginform_page.add_loginform(username_text='admin', password_text='password').click_login_button()

        """Сообщение об успешном входе"""
        assert loginform_page.check_success_message(), f"Вход не выполнен успешно. Текст сообщения: '{loginform_page.get_result_text()}'"


    def test_loginform_add_invalid_login(self, loginform_page):

        """Ввод логина и пароля + кнопка вход"""
        loginform_page.add_loginform(username_text='abcde', password_text='password').click_login_button()

        """Сообщение что вход Не выполнен (логин)"""
        assert loginform_page.check_error_message(), f"Ожидалось сообщение об ошибке, но получено: '{loginform_page.get_result_text()}'"

    def test_loginform_add_invalid_password(self, loginform_page):

        """Ввод логина и пароля + кнопка вход"""
        loginform_page.add_loginform(username_text='admin', password_text='password12345').click_login_button()

        """Сообщение что вход Не выполнен (пароль)"""
        assert loginform_page.check_error_message(), f"Ожидалось сообщение об ошибке, но получено: '{loginform_page.get_result_text()}'"



