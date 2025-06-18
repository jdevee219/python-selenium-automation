Feature: Cart tests

  Scenario: User can view Cart on Target
    Given Open target main page
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown

  Scenario: Verify item in Target Cart
    Given Open target main page
    When Search for millennium falcon lego
    And Add item to cart
    And Store product name
    And Add item in side panel
    And View cart
    Then Verify item has been added to cart
    And Verify cart has correct product