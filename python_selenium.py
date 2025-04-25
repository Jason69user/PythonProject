import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.maximize_window() # окно максимального разрешения
user_name = driver_chrome.find_element(By.ID, "user-name")
user_name.send_keys("problem_user") # вводим логин
password = driver_chrome.find_element(By.ID, "password")
password.send_keys("secret_sauce") # вводим пароль
# time.sleep(10)
# driver_chrome.close()

