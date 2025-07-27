from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


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

# создаем экземпляр класса и запускаем метод
start_test = Test()
start_test.test_select_prod()
