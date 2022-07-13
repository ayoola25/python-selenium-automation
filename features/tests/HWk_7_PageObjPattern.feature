# Created by EZ-Trainer at 6/30/2022
Feature: Test to show window Page Object Pattern

   Scenario: Logged out user sees Sign in page when clicking Orders
      Given Open Amazon page
      When Click Amazon Orders link
      Then Verify Sign In page is opened

   @smoke
   Scenario: 'Your Shopping Cart is empty' shown if no product added
      Given Open Amazon page
      When Click on cart_icon
      Then Verify Your Amazon Cart is empty text present