from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox')
# by css, ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
# ID + tag
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
# by class
driver.find_element(By.CSS_SELECTOR, '.nav-a')
driver.find_element(By.CSS_SELECTOR, '.nav-logo-link')
driver.find_element(By.CSS_SELECTOR, '.nav-a-2.icp-link-style-2')
driver.find_element(By.CSS_SELECTOR, '.nav-a-2.icp-link-style-2.nav-a')
# by tag + class
driver.find_element(By.CSS_SELECTOR, 'a.nav-logo-link.nav-progressive-attribute')
# by tag + id + class
driver.find_element(By.CSS_SELECTOR, 'a#nav-logo-sprites.nav-logo-link.nav-progressive-attribute')
# by attribute
driver.find_element(By.CSS_SELECTOR, '[aria-label="Amazon"]')
# by tag + attribute
driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Amazon"]')
driver.find_element(By.CSS_SELECTOR, '[lang="en"][aria-label="Amazon"]')
driver.find_element(By.CSS_SELECTOR, '[lang="en"][aria-label="Amazon"]')
# tag + id + class + attributes
driver.find_element(By.CSS_SELECTOR, 'a#nav-logo-sprites.nav-logo-link[lang="en"][aria-label="Amazon"]')

# By using attribute partial match, use *=
driver.find_element(By.CSS_SELECTOR, "[href*='ap_signin_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsScreenReaderOnly'][class*='styles_notFocusable']")


#For Homework 3
driver.get('https://www.amazon.com/ap/register?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&showRememberMe=true&openid.pape.max_auth_age=0&pageId=usflex&prepopulatedLoginId=&openid.assoc_handle=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&policy_handle=Retail-Checkout')

# Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo')

# Create account text
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your Name text box
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# Email text box
driver.find_element(By.CSS_SELECTOR, '#ap_email')

# Password text box
driver.find_element(By.CSS_SELECTOR, '#ap_password')

# Passwords must be at least 6 characters.
driver.find_element(By.XPATH, "//a[text()='Passwords must be at least 6 characters.']")

# Re-enter password text box
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Continue button
driver.find_element(By.CSS_SELECTOR, '#continue')

# Conditions of Use link
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_condition_of_use']")

# Privacy Notice link
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice']")

# Sign In link
driver.find_element(By.CSS_SELECTOR, '#ra-sign-in-link')