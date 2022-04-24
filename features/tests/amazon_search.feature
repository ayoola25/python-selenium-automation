# Created by EZ-Trainer at 4/16/2022
Feature: Test for Amazon search
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon
    When Search for "coffee"
    And Click on search icon
    Then Verify search results are shown



