Feature: Cart tests

  Scenario: User can view Cart on Target
    Given Open target main page
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown
    Then Verify Cart page opened

  Scenario: Verify item in Target Cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

  # Lesson 4 Homework
  Scenario: Verify item in Target Cart
    Given Open target main page
    When Search for coffee
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product