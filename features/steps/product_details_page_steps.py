from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product A-94280240 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/men-39-s-hybrid-shorts-6-34-all-in-motion-8482/-/A-94280240?preselect=93321357#lnk=sametab')



@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Blue', 'Dark Blue', 'Jet Black', 'Red', 'Tan']
    actual_colors = []

    context.driver.wait.until(
        EC.visibility_of_element_located(COLOR_OPTIONS)
    )
    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        c.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'