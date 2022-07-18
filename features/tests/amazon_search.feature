# Created by EZ-Trainer at 4/16/2022
Feature: Test for Amazon search

  Scenario: Verify that user can search for table
    Given Open Amazon page
    When Search for table
    Then Verify search results for "table" are shown

  Scenario: Verify that user can search for dress
    Given Open Amazon page
    When Search for dress
    Then Verify search results for "dress" are shown

  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select books department
    And Search for Faust
    Then Verify books department is selected








