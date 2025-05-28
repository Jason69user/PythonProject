import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.maximize_window() # окно максимального разрешения

user_name = driver_chrome.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input')
user_name.send_keys("problem_user") # вводим логин
print('input login')

password = driver_chrome.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("secret_sauce") # вводим не корректный пароль
print('input password')

button_login = driver_chrome.find_element(By.ID, 'login-button')
button_login.click() # кликаем на авторизацию
print("Click Login")
time.sleep(1)

now_date = datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
name_screenshot = 'screenshot' + now_date + '.png'
driver_chrome.save_screenshot('D:\\GitHub\\Project\\PythonProject\\screen\\' + name_screenshot) # делаем скриншот страницы
# driver_chrome.refresh() # обновляем страницу