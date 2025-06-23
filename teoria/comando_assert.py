import time
from tabnanny import check

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Comandos 'assert' → sempre espera um retorno da condição True
"""
# Config. modo anônimo
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
browser = webdriver.Chrome(options=chrome_options) # instancia o Chrome como browser desse teste
browser.implicitly_wait(12) # fica fazendo verificação ate fazer o teste

# Acessa página
browser.maximize_window()
browser.get("https://leogcarvalho.github.io/test-automation-practice/")
wait = WebDriverWait(browser, 30)
"""
# assert numbers
numero_esperado = 1
numero_obtido = 2
#assert numero_esperado == numero_obtido, f"Esperado{numero_esperado} atual {numero_obtido}!"
# falhou porque os números não são iguais

# assert text
text_esperado = "Teste com Selenium e Python"
text_obtido = "Teste com Selenium e Python"
#assert text_esperado. == text_obtido., f"Esperado {text_esperado} obtido {text_obtido}"
# posso usar tratamento de string → .lower,...

# assert text in string → verifica se um elemento do texto ésta presente no outro
text_esperado = "Selenium"
text_obtido = "Teste com Selenium"
#assert text_esperado in text_obtido, f"Esperado '{text_esperado}' obtido '{text_obtido}'"
# ou
# assert text_esperado not in text_obtido, f"Esperado '{text_esperado}' obtido '{text_obtido}'"

# assert is_displayed/is_enabled/is_selected

