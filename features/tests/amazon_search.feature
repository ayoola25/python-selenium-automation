# Created by EZ-Trainer at 4/16/2022
Feature: Test for Amazon search
  # Enter feature description here

  Scenario: Verify that user can search for table
    Given Open Amazon page
    When Search for table
    Then Verify search results for "table" are shown

  Scenario: Verify that user can search for dress
    Given Open Amazon page
    When Search for dress
    Then Verify search results for "dress" are shown







