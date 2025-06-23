import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Comando para localizar elementos dentro de 'browser.'

# Config. modo anônimo
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
browser = webdriver.Chrome(options=chrome_options) # instancia o Chrome como browser desse teste

# Acessa página
browser.maximize_window()
browser.get("https://www.saucedemo.com/")

"""# (find_element()) → encontra uma ocorrência somente / se não encontrar ele retorna ERRO
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")

# (send_keys()) → envia informações para os campos dos elementos anteriores
username.send_keys("standard_user")
password.send_keys("secret_sauce")"""


# (browser.find_elements()) → encontra vários elementos / se não encontrar ele retonar uma lista vazia
auth_fields = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")
print(auth_fields) # → printa a variavel
print(len(auth_fields)) # → printa o tamanho dela
assert len(auth_fields) == 2, "posso deixar uma mensagem para caso de ERRO" # → verifica se são 2 mesmo
time.sleep(3)