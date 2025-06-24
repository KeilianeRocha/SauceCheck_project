import time
from tabnanny import check

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Comandos 'assert' → sempre espera um retorno da condição True

# Config. modo anônimo
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
browser = webdriver.Chrome(options=chrome_options) # instancia o Chrome como browser desse teste
browser.implicitly_wait(12) # fica fazendo verificação ate fazer o teste

# Acessa página
browser.maximize_window()
browser.get("https://www.saucedemo.com/")
wait = WebDriverWait(browser, 30)

username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login = browser.find_element(By.ID, "login-button").click()

homePage = browser.find_element(By.XPATH, "//*[@class='app_logo']")
print(homePage.text)
assert homePage.text == "Swag Labs" # o texto tem que ser igual!
time.sleep(3)