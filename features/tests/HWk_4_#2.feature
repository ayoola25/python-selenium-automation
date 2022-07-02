Feature: Test for Added Product

  # Created by EZ-Trainer at 5/9/2022
  Scenario: Verify that user can add product to the cart
    Given Open Amazon page
    When Search for glass cups
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)