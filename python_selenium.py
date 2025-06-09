import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.maximize_window() # окно максимального разрешения

user_name = driver_chrome.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input')
user_name.send_keys("standard_user") # вводим логин
print('input login')

# вводим пароль
password = driver_chrome.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("secret_sauce")
print('input password')

# кликаем на авторизацию
button_login = driver_chrome.find_element(By.ID, 'login-button')
button_login.click()
print("Click Login")

# выбираем товар
button_add_backpack = driver_chrome.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
button_add_backpack.click()
print("select product")

# переходим в корзину
button_cart_link = driver_chrome.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
button_cart_link.click()
print("select cart link")

time.sleep(1)

driver_chrome.back() # нажимаем "назад"
print("select back")

time.sleep(1)

driver_chrome.forward() # нажимаем "вперед"
print("select forward")

time.sleep(1)

driver_chrome.close()