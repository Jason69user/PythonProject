import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')
# options.add_argument('--headless')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.maximize_window() # окно максимального разрешения

user_name = driver_chrome.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input')
user_name.send_keys("standard_user") # вводим логин
print('input login')

password = driver_chrome.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("secret_sauce") # вводим пароль
print('input password')

button_login = driver_chrome.find_element(By.ID, 'login-button')
button_login.click() # кликаем на авторизацию
print("Click Login")

menu = driver_chrome.find_element(By.ID, 'react-burger-menu-btn').click() # нажимаем сендвич меню

time.sleep(1)

logout = driver_chrome.find_element(By.ID, "logout_sidebar_link").click() # нажмаем на разлогирование

# print(driver_chrome.current_url)

# get_url = driver_chrome.current_url
# url = 'https://www.saucedemo.com/inventory.html'
# assert url == get_url # сравниваем корректность url
# print('URL корректен')
#
# warning_text = driver_chrome.find_element(By.XPATH, '//h3[@data-test="error"]') # ищем окно ошибки при вводе некорретного пароля
# value_warning_text = warning_text.text
# assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service' # сравниваем текст ошибки
# print('Сообщение об ошибки корректно')
#
# error_button = driver_chrome.find_element(By.XPATH, '//button[@class ="error-button"]')
# error_button.click() # нажимаем на закрытие текста ошибки
# print("Error button click")

# text_products = driver_chrome.find_element(By.XPATH, "//span[@class='title']")
# print(text_products.text) # ищем уникальное значение для определения корректности страницы
#
# value_text_products = text_products.text
# assert value_text_products == 'Products' # сравниваем уникальное значение с корректным
# print('Заголовок корректен')