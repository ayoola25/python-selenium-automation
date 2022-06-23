# Created by EZ-Trainer at 6/17/2022
Feature: Test for Amazon searches

  Scenario Outline: Verify that user can search for products
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search results for <search_result> are shown
    Examples:
    |search_word |search_result |
    |table       |"table"       |
    |dress       |"dress"       |
    |spoon       |"spoon"       |

