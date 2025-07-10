import os
import time

from unittest.mock import patch
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1261, 2399) # задаем параметры окна разрешения

# получаем путь до файла
patch_pload = "D:\\GitHub\\Project\\PythonProject\\screen\\shaman.jpg"

# загружаем файл в браузер
click_button = driver_chrome.find_element(By.XPATH, "//input[@id='file']")
click_button.send_keys(patch_pload)
time.sleep(1)

# берем название файла и проверяем на корректность
value = click_button.get_attribute("value")
actual_file_name = os.path.basename(value)
print(actual_file_name)
assert actual_file_name == "shaman.jpg"
print("Название файла совпадает")

driver_chrome.close()