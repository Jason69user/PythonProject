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

def driver_xpath(xpath):
    return driver_chrome.find_element(By.XPATH, xpath)

def driver_id(id):
    return driver_chrome.find_element(By.ID, id)

# выбираем товар
def name_product(product, price_product, select_product): # смотрим товар №1
    value_product = product.text
    value_price_product = price_product.text
    print(value_product)
    print(value_price_product)
    select_product.click()
    print('select Product\n')

# проверка товара в корзине с выбранным
def assert_cart_product(cart_product, value_product, cart_price_product, value_price_product):
    value_cart_product = cart_product.text
    print(value_cart_product)
    text_value_product = value_product
    assert text_value_product == value_cart_product
    print(f'Info Cart Product {value_cart_product} good')
    value_cart_price_product = cart_price_product.text
    print(value_cart_price_product)
    assert value_price_product == value_cart_price_product
    print(f'Info Price Cart Product {value_cart_product} good\n')

# финальная проверка товара
def finish_checkout(finish_product, value_product, price_finish, value_price_product):
    value_finish_product = finish_product.text
    print(value_finish_product)
    assert value_product == value_finish_product
    print(f'info finish product {value_product} good')
    value_price_finish = price_finish.text
    print(value_price_finish)
    assert value_price_product == value_price_finish
    print(f'info price finish product {value_product} good\n')

# вводим корректный логин
user_name = driver_xpath('//*[@id="user-name"]')
user_name.send_keys("standard_user")
print('input login')

# вводим корректный пароль
password = driver_xpath('//*[@id="password"]')
password.send_keys("secret_sauce")
print('input password')

# кликаем на авторизацию
button_login = driver_id('login-button')
button_login.click()
print("Click Login\n")

# смотрим товар №1
product_1 = driver_xpath('//*[@id="item_4_title_link"]')
value_product_1 = product_1.text
price_1 = driver_xpath('//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_1.text
select_1 = driver_id("add-to-cart-sauce-labs-backpack")
name_product(product_1, price_1, select_1)

# смотрим товар №2
product_2 = driver_xpath('//*[@id="item_0_title_link"]')
value_product_2 = product_2.text
price_2 = driver_xpath('//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
value_price_product_2 = price_2.text
select_2 = driver_id("add-to-cart-sauce-labs-bike-light")
name_product(product_2, price_2, select_2)

# переходим в корзину
button_cart_link = driver_chrome.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
button_cart_link.click()
print('select Cart link\n')

# сравниваем товар в корзине с товаром #1
cart_product_1 = driver_xpath('//*[@id="item_4_title_link"]')
cart_price_product_1 = driver_xpath('//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
assert_cart_product(cart_product_1, value_product_1, cart_price_product_1, value_price_product_1)

# сравниваем товар в корзине с товаром #2
cart_product_2 = driver_xpath('//*[@id="item_0_title_link"]')
cart_price_product_2 = driver_xpath('//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
assert_cart_product(cart_product_2, value_product_2, cart_price_product_2, value_price_product_2)

# кликаем на checkout
checkout = driver_xpath('//*[@id="checkout"]')
checkout.click()
print('click checkout')

# вводим Имя
first_name = driver_xpath('//*[@id="first-name"]')
first_name.send_keys("Leman")
print('input first name')

# вводим Фамилию
last_name = driver_xpath('//*[@id="last-name"]')
last_name.send_keys("Russ")
print('input last name')

# вводим пароль
postal_code = driver_chrome.find_element(By.XPATH, '//*[@id="postal-code"]')
postal_code.send_keys("1234")
print('input postal code')

# кликаем на continue
button_continue = driver_xpath('//*[@id="continue"]')
button_continue.click()
print('click continue\n')

# финальное сравнение товара в корзине с товаром #1
finish_product_1 = driver_xpath('//*[@id="item_4_title_link"]')
price_finish_product_1 = driver_xpath('//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_finish_product_1 = price_finish_product_1.text
finish_checkout(finish_product_1, value_product_1, price_finish_product_1, value_price_product_1)

# финальное сравнение товара в корзине с товаром #2
finish_product_2 = driver_xpath('//*[@id="item_0_title_link"]')
price_finish_product_2 = driver_xpath('//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_price_finish_product_2 = price_finish_product_2.text
finish_checkout(finish_product_2, value_product_2, price_finish_product_2, value_price_product_2)

# сравниваем конечную сумму с реальной путем сложения
summary_price = driver_xpath('//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
text_summary_price = summary_price.text
value_summary_price = float(text_summary_price.replace("Item total: $", "")) # убрал в цене строку Item total: $
print(f"${value_summary_price}")
price1 = float(value_price_finish_product_1.replace("$", "")) # убрал в цене символ $
price2 = float(value_price_finish_product_2.replace("$", ""))
item_total = price1 + price2
print(f"Item total: ${item_total}")
assert value_summary_price == item_total
print('info item total good\n')

# кликаем на finish
button_finish = driver_xpath('//*[@id="finish"]')
button_finish.click()
print('input button finish')

# Проверяем финишную страницу
checkout_complete = driver_xpath('//*[@id="checkout_complete_container"]/h2')
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == "Thank you for your order!"
print("info order complete")

driver_chrome.close()