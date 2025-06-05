from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# 3 As: Arrange / Act / Assert

# Arrange (setup)
# init driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# open the url
driver.get('https://www.target.com/')

# Act
driver.find_element(By.ID, "account-sign-in").click()
sleep(5)
driver.find_element(By.XPATH, "//button[@type='button' and text()='Sign in or create account']").click()
sleep(5)


# Assert (Verification)
expected_text = 'Sign in or create account'
actual_text = driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text

assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'
print('Test case passed')
driver.quit()