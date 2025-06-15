import time

class TestLoginform4:
    def test_loginform_add_valid(self, loginform_page_2):

        """Ввод логина и пароля + кнопка вход"""
        loginform_page_2.add_loginform(username_text='admin', password_text='password').click_login_button()

        """Сообщение об успешном входе"""
        assert loginform_page_2.check_success_message(), f"Вход не выполнен успешно. Текст сообщения: '{loginform_page_2.get_result_text()}'"


    def test_loginform_add_invalid_login(self, loginform_page_2):

        """Ввод логина и пароля + кнопка вход"""
        loginform_page_2.add_loginform(username_text='abcde', password_text='password').click_login_button()

        """Сообщение что вход Не выполнен (логин)"""
        assert loginform_page_2.check_error_message(), f"Ожидалось сообщение об ошибке, но получено: '{loginform_page_2.get_result_text()}'"

    def test_loginform_add_invalid_password(self, loginform_page_2):

        """Ввод логина и пароля + кнопка вход"""
        loginform_page_2.add_loginform(username_text='admin', password_text='password12345').click_login_button()

        """Сообщение что вход Не выполнен (пароль)"""
        assert loginform_page_2.check_error_message(), f"Ожидалось сообщение об ошибке, но получено: '{loginform_page_2.get_result_text()}'"



