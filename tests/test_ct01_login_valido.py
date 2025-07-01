import time
import pytest
from tests import conftest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.loginValido
class TestCT01:
    def test_ct01_login_valido(self):
        driver= conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        homepage = driver.find_element(By.XPATH, "//*[@class='app_logo']")
        print(homepage.text)
        assert homepage.text == "Swag Labs" # o texto tem que ser igual!
        time.sleep(3)