Feature: Sign in to a website

  Scenario: User can navigate to Sign In
    Given Open target main page
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened