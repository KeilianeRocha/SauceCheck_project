import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver: webdriver.Remote


@pytest.fixture()
def setup_teardown():
    # setup
    global driver
    # Config. modo anônimo
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
    driver = webdriver.Chrome(options=chrome_options)  # instancia o Chrome como driver desse teste
    driver.implicitly_wait(12)  # fica fazendo verificação ate fazer o teste

    # Acessa página
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run test
    yield

    # teardown
    driver.quit()


