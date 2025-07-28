from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# создаем класс
class Test:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)

    def test_select_prod(self):
        driver_chrome = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com'  # Даём ссылку на тестируемый сайт
        driver_chrome.get(base_url)  # открываем ссылку в браузере Chrome
        driver_chrome.set_window_size(1261, 924)  # задаем параметры окна разрешения

        print("Старт тест")

        # проводим авторизацию
        WebDriverWait(driver_chrome, 30).until(EC.element_to_be_clickable
                                               ((By.ID, 'user-name'))).send_keys("standard_user")  # вводим логин
        print('Input User Name')
        WebDriverWait(driver_chrome, 30).until(EC.element_to_be_clickable
                                               ((By.ID, 'password'))).send_keys("secret_sauce")  # вводим пароль
        print('Input Password')
        WebDriverWait(driver_chrome, 30).until(EC.element_to_be_clickable
                                               ((By.ID, 'login-button'))).click()  # кликаем на авторизацию
        print('Click Login Button')

        # выбираем товар и переходим в корзину
        WebDriverWait(driver_chrome, 30).until(EC.element_to_be_clickable
                                               ((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
        print('Click Select Product')
        WebDriverWait(driver_chrome, 30).until(EC.element_to_be_clickable
                                               ((By.XPATH, "//a[@class= 'shopping_cart_link']"))).click()
        print('Click Shopping Cart')

        # делаем проверку страницы корзины
        success_text = WebDriverWait(driver_chrome, 30).until(EC.element_to_be_clickable
                                               ((By.XPATH, "//span[@class= 'title']"))).text
        assert success_text == "Your Cart"
        print("Тест завершен")


# создаем экземпляр класса и запускаем метод
start_test = Test()
start_test.test_select_prod()
