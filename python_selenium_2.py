from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")
options.add_argument("--headless")

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1700, 1800) # окно максимального разрешения

# вводим корректный логин
user_name = driver_chrome.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input')
user_name.send_keys("standard_user")
print('input login')

# вводим корректный пароль
password = driver_chrome.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("secret_sauce")
print('input password')

# кликаем на авторизацию
button_login = driver_chrome.find_element(By.ID, 'login-button')
button_login.click()
print("Click Login")

# смотрим товар №1
product_1 = driver_chrome.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)

# смотрим цену товара №1
price_product_1 = driver_chrome.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

# кладем товар #1 в корзину
select_product_1 = driver_chrome.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
select_product_1.click()
print('select Product 1')

# смотрим товар №2
product_2 = driver_chrome.find_element(By.XPATH, '//*[@id="item_0_title_link"]')
value_product_2 = product_2.text
print(value_product_2)

# смотрим цену товара №2
price_product_2 = driver_chrome.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
value_price_product_2 = price_product_2.text
print(value_price_product_2)

# кладем товар #2 в корзину
select_product_2 = driver_chrome.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
select_product_2.click()
print('select Product 2')

# переходим в корзину
button_cart_link = driver_chrome.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
button_cart_link.click()
print('select Cart link')

# сравниваем товар в корзине с товаром #1
cart_product_1 = driver_chrome.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print('Info Cart Product 1 good')

# сравниваем цену товара в корзине с товаром #1
cart_price_product_1 = driver_chrome.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_product_1 = cart_price_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print('Info Price Cart Product 1 good')

# сравниваем товар в корзине с товаром #2
cart_product_2 = driver_chrome.find_element(By.XPATH, '//*[@id="item_0_title_link"]')
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2
print('Info Cart Product 2 good')

# сравниваем цену товара в корзине с товаром #2
cart_price_product_2 = driver_chrome.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_cart_price_product_2 = cart_price_product_2.text
print(value_cart_price_product_2)
assert value_price_product_2 == value_cart_price_product_2
print('Info Price Cart Product 2 good')

# кликаем на checkout
checkout = driver_chrome.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()
print('click checkout')

# вводим Имя
first_name = driver_chrome.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys("Leman")
print('input first name')

# вводим Фамилию
last_name = driver_chrome.find_element(By.XPATH, '//*[@id="last-name"]')
last_name.send_keys("Russ")
print('input last name')

# вводим пароль
postal_code = driver_chrome.find_element(By.XPATH, '//*[@id="postal-code"]')
postal_code.send_keys(1234)
print('input postal code')

# кликаем на continue
button_continue = driver_chrome.find_element(By.XPATH, '//*[@id="continue"]')
button_continue.click()
print('click continue')

# сравниваем товар в корзине с товаром #1
finish_product_1 = driver_chrome.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print('info finish product 1 good')

# сравниваем цену товара в корзине с товаром #1
price_finish_product_1 = driver_chrome.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_finish_product_1 = price_finish_product_1.text
print(value_price_finish_product_1)
assert value_price_product_1 == value_price_finish_product_1
print('info price finish product 1 good')

# сравниваем товар в корзине с товаром #2
finish_product_2 = driver_chrome.find_element(By.XPATH, '//*[@id="item_0_title_link"]')
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print('info finish product 2 good')

# сравниваем цену товара в корзине с товаром #2
price_finish_product_2 = driver_chrome.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_price_finish_product_2 = price_finish_product_2.text
print(value_price_finish_product_2)
assert value_price_product_2 == value_price_finish_product_2
print('info price finish product 2 good')

# сравниваем конечную сумму с реальной путем сложения
summary_price = driver_chrome.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
text_summary_price = summary_price.text
value_summary_price = float(text_summary_price.replace("Item total: $", "")) # убрал в цене строку Item total: $
print(f"${value_summary_price}")
price1 = float(value_price_finish_product_1.replace("$", "")) # убрал в цене символ $
price2 = float(value_price_finish_product_2.replace("$", ""))
item_total = price1 + price2
print(f"Item total: ${item_total}")
assert value_summary_price == item_total
print('info item total good')

# кликаем на finish
button_finish = driver_chrome.find_element(By.XPATH, '//*[@id="finish"]')
button_finish.click()
print('input button finish')

# Проверяем финишную страницу
checkout_complete = driver_chrome.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == "Thank you for your order!"
print("info order complete")

driver_chrome.close()