import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/browser-windows' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1261, 2399) # задаем параметры окна разрешения

# открываем вторую вкладку, переключаемся на неё и возвращаемся обратно
tab_button = driver_chrome.find_element(By.XPATH, "//button[@id = 'tabButton']")
tab_button.click()
driver_chrome.switch_to.window(driver_chrome.window_handles[1])
print("Переключились на вторую вкладку")
time.sleep(2)
driver_chrome.switch_to.window(driver_chrome.window_handles[0])
print("Переключились на первую вкладку")
time.sleep(2)

# открываем второе окно, переключаемся на него и возвращаемся обратно
window_button = driver_chrome.find_element(By.XPATH, "//button[@id = 'windowButton']")
window_button.click()
driver_chrome.switch_to.window(driver_chrome.window_handles[1])
print("Переключились на второе окно")
time.sleep(2)
driver_chrome.switch_to.window(driver_chrome.window_handles[0])
print("Переключились на первое окно")
time.sleep(2)

driver_chrome.close()