import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.maximize_window() # окно максимального разрешения
time.sleep(10)
driver_chrome.close()

driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver_firefox.get(base_url) # открываем ссылку в браузере Firefox
driver_firefox.maximize_window() # окно максимального разрешения
time.sleep(10)
driver_firefox.close()

service = EdgeService(EdgeChromiumDriverManager().install())
driver_edge = webdriver.Edge(service=service)
driver_edge.get(base_url) # открываем ссылку в браузере Edge
driver_edge.maximize_window() # окно максимального разрешения
time.sleep(10)
driver_edge.close()