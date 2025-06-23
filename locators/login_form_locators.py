from selenium.webdriver.common.by import By


class LoginformLocators:

    """Локаторы"""
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-btn')
    RESULT_MESSAGE = (By.ID, 'result')



