from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# Locators:

# Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Email field
driver.find_element(By.XPATH, "//input[@type='email']")

# Continue button
driver.find_element(By.ID, 'continue')

# Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-list-item']")

# Forgot your password link - Not present on website

# Other issues with Sign-In link - Not present on website

# Create your Amazon account button - Not present on website

# By XPath
#driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
#driver.find_element(By.XPATH, "//input[@role='searchbox']")

# By XPath, any tag
#driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']")

# By XPath, combination of attributes
#driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords' and @spellcheck='false']")
#driver.find_element(By.XPATH, "//*[@tabindex='0' and @name='field-keywords' and @spellcheck='false']")
#driver.find_element(By.XPATH, "//input[@name='field-keywords' and @tabindex='0' and @spellcheck='false']")

# by text
#driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
#driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# partial match
#driver.find_element(By.XPATH, "//a[contains(@href, 'ref_=nav_cs_bestsellers')]")

# parent => child nodes
#driver.find_element(By.XPATH, "//div[@id='navbar']//a[text()='Best Sellers']")
