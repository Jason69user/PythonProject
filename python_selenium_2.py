import time

from selenium import webdriver
from faker import Faker
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1920, 1080) # задаем параметры окна разрешения
fake = Faker('en_US') # инициализируем faker

# вставляем в поле Username сгенерированное имя
name = fake.name()
user_name = driver_chrome.find_element(By.ID, 'user-name')
user_name.send_keys(name) # вводим логин
time.sleep(2)

driver_chrome.close()