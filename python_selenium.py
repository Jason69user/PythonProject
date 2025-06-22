import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/buttons' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1920, 1080) # окно разрешения
action = ActionChains(driver_chrome)

# имитируем двойной клик мыши по кнопке
double_click = driver_chrome.find_element(By.XPATH, "//button[@id = 'doubleClickBtn']")
action.double_click(double_click).perform()
print('Двойной клик мыши')

# имитируем клик правой кнопки мыши
right_click = driver_chrome.find_element(By.XPATH, "//button[@id = 'rightClickBtn']")
action.context_click(right_click).perform()
print('Клик ПКМ')

time.sleep(2)

driver_chrome.close()