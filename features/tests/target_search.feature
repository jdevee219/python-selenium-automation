Feature: Tests for Target Search

  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify search worked

  Scenario: User can view Cart on Target
    Given Open target main page
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown

  Scenario: User can navigate to Sign In
    Given Open target main page
    When Click Sign In
    Then Verify Sign In form opened