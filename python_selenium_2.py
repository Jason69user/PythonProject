import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1700, 1800) # окно максимального разрешения

user_name = driver_chrome.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input')
user_name.send_keys("error_user") # вводим не корректный логин
print('input invalid login')

password = driver_chrome.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("secret_sauce") # вводим корректный пароль
print('input password')

time.sleep(2)

user_name.send_keys(Keys.CONTROL + 'a' + Keys.DELETE) # очищаем поле логин
print('login deleted')
password.send_keys(Keys.CONTROL + 'a' + Keys.DELETE) # очищаем поле пароль
print('password deleted')

time.sleep(2)

user_name.send_keys("standard_user") # повторно вводим логин
print('input correct login')
password.send_keys("secret_sauce") # повторно воодим пароль
print('input password')

button_login = driver_chrome.find_element(By.ID, 'login-button')
button_login.click() # кликаем на авторизацию
print("Click Login")

time.sleep(1)

driver_chrome.close()