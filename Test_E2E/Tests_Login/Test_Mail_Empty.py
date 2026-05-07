from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_mailEmpty():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver,10)

    driver.get("https://www.saucedemo.com/")

    emailField = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    emailField.send_keys("")
    passwordField = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    passwordField.send_keys("secret_sauce")
    loginButton = wait.until(EC.visibility_of_element_located((By.ID,"login-button")))
    loginButton.click()

    error = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))

    assert "Username is required" in error.text
    print(error.text)

    driver.quit()


if __name__ == "__main__":
    test_mailEmpty()