from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():

    def __init__(self, driver):
        self.driver_chrome = driver

    # проводим авторизацию
    def autorization(self, login_name, login_password):
        WebDriverWait(self.driver_chrome, 30).until(EC.element_to_be_clickable
                                               ((By.ID, 'user-name'))).send_keys(login_name)  # вводим логин
        print('Input User Name')

        WebDriverWait(self.driver_chrome, 30).until(EC.element_to_be_clickable
                                               ((By.ID, 'password'))).send_keys(login_password)  # вводим пароль
        print('Input Password')

        WebDriverWait(self.driver_chrome, 30).until(EC.element_to_be_clickable
                                               ((By.ID, 'login-button'))).click()  # кликаем на авторизацию
        print('Click Login Button')
