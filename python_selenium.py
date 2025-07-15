import glob, os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

path_download = r"D:\GitHub\Project\PythonProject\files_download" # даем ссылку на директорию куда загружать файл
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": path_download,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
         }
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo' # Даём ссылку на тестируемый сайт
driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1261, 2399) # задаем параметры окна разрешения

# нажимаем на скачивание файла
click_button = driver_chrome.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
click_button.click()
time.sleep(3)

# проверяем скачанный файл по названию
file_name = "LambdaTest.pdf"
file_path = os.path.join(path_download, file_name)
assert os.access(file_path, os.F_OK) == True
print("Файл в директории")

# проверяем скачанный файл пустой он или нет по размеру
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("Файл не пуст")
    else:
        print("Файл пуст")

# удаляем файл после проверки
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    os.remove(file)

driver_chrome.close()