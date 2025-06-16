from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Number of benefit cells
@then('Verify page has correct amount of benefit cells')
def verify_benefit_cells(context):
    cells = context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")
    assert len(cells) >= 10, f'Expected more than 10 links but got {len(cells)}'