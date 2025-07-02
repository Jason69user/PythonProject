import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://lambdatest.com/selenium-playground/simple-form-demo' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1920, 1080) # задаем параметры окна разрешения

# отправляем сообщение с проверкой на корректность передачи
single_input = driver_chrome.find_element(By.XPATH, "//input[@id = 'user-message']")
input_message = "Магнус не предавал"
single_input.send_keys(input_message)
input_checked_value = driver_chrome.find_element(By.XPATH, "//button[@id = 'showInput']")
input_checked_value.click()
time.sleep(1)
your_message = driver_chrome.find_element(By.XPATH, "//p[@id = 'message']")
text_message = your_message.text
print(text_message)
assert text_message == input_message
print('Сообщения передаются корректно')


# вводим числовые значения и проверяем корректность их подсчета
first_value = 100
second_value = 200
result_sum = first_value + second_value
print(result_sum)

input_first_value = driver_chrome.find_element(By.XPATH, "//input[@id= 'sum1']")
input_first_value.send_keys(first_value) # вводим первое число
input_second_value = driver_chrome.find_element(By.XPATH, "//input[@id= 'sum2']")
input_second_value.send_keys(second_value) # вводим второе число
get_sum = driver_chrome.find_element(By.XPATH, "//*[@id='gettotal']/button")
get_sum.click()
time.sleep(1)
result_message = driver_chrome.find_element(By.XPATH, "//p[@id= 'addmessage']")
text_result = result_message.text
assert text_result == str(result_sum)
print("Значения равны")

driver_chrome.close()