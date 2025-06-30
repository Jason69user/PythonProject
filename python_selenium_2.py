import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://lambdatest.com/selenium-playground/jquery-dropdown-search-demo' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1920, 1080) # задаем параметры окна разрешения

# нажимаем на селект
select_drop = driver_chrome.find_element(By.XPATH, "//span[@aria-labelledby = 'select2-country-container']")
select_drop.click()

# выбираем страну из селекта
select_country = driver_chrome.find_element(By.XPATH, "(//li[@class = 'select2-results__option'])[8]")
select_country.click()

time.sleep(3)

driver_chrome.close()