# Created by EZ-Trainer at 7/17/2022
Feature: Wiki search

  Scenario Outline: Search returns correct results
    Given Open main page
    When Search for <query_words>
    Then Verify article opens for <query_words>
    Examples:
    |query_words                    |
    |Cat                            |
    |Python (programming language)  |
    |Java (programming language)    |
    |Selenium (software)            |
    |List of HTTP Status Codes      |

  Scenario: Search can open No Search Results
    Given Open main page
    When Search for ahgsfgaddgast
    Then Verify No Search Results page opens

  Scenario: Article creation can be opened from No Search Results
    Given Open main page
    When Search for ahgsfgaddgast
    Then Verify No Search Results page opens
    When Click to create article
    Then Verify article opens for Wikipedia:Articles for creation