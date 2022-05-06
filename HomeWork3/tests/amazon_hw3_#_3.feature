# Created by EZ-Trainer at 5/5/2022
Feature: Test for Amazon cart icon


   Scenario: Verify that user can see that Amazon cart is empty
    Given Navigate to Amazon page
    When click on Cart
    Then Verify click result Amazon Cart is empty is shown

