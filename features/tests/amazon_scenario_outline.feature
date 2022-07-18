# Created by EZ-Trainer at 6/17/2022
Feature: Test for Amazon searches

  @smoke
  Scenario Outline: Verify that user can search for products
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search results for <search_result> are shown
    Examples:
    |search_word |search_result |
    |table       |"table"       |
#    |dress       |"dress"       |
#    |spoon       |"spoon"       |

#   Scenario Outline: Verify that user sees correct error message
#    Given Open Amazon page
#    When Enter username <username>
#    When Enter password <password>
#    When Click login btn
#    Then Verify correct error <error_message> shown
#    Examples:
#    |username       |password  |error_message  |
#    |test@test.com  |hgsfdrea  |invalid_credentials |
#    |test@test.com  |          |Password is required                                                                              |


  Scenario: User sees ham menu btn on the main page
    Given Open Amazon page
    When Search for dress
    Then Verify search results for "dress" are shown
    Then Verify hamburger menu btn present

  Scenario: User sees correct amount of footer links
    Given Open Amazon page
    Then Verify there are 38 footer links