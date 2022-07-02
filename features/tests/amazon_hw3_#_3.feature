# Created by EZ-Trainer at 5/5/2022
Feature: Test for Amazon cart icon


   Scenario: Verify that user can see that Amazon cart is empty
    Given Open Amazon page
    When click on cart_icon
    Then Verify click result Your Amazon Cart is empty is shown

