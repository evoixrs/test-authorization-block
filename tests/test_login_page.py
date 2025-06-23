

class TestLoginPage:
    def test_login_page_add_valid(self, login_page):

        """Ввод логина и пароля + кнопка вход"""
        login_page.add_login_page(username_text='admin', password_text='password').click_login_button()

        """Сообщение об успешном входе"""
        assert login_page.check_success_message(), f"Вход не выполнен успешно. Текст сообщения: '{login_page.get_result_text()}'"


    def test_login_page_add_invalid_login(self, login_page):

        """Ввод логина и пароля + кнопка вход"""
        login_page.add_login_page(username_text='abcde', password_text='password').click_login_button()

        """Сообщение что вход Не выполнен (логин)"""
        assert login_page.check_error_message(), f"Ожидалось сообщение об ошибке, но получено: '{login_page.get_result_text()}'"

    def test_login_page_add_invalid_password(self, login_page):

        """Ввод логина и пароля + кнопка вход"""
        login_page.add_login_page(username_text='admin', password_text='password12345').click_login_button()

        """Сообщение что вход Не выполнен (пароль)"""
        assert login_page.check_error_message(), f"Ожидалось сообщение об ошибке, но получено: '{login_page.get_result_text()}'"



