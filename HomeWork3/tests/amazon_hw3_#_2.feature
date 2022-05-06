# Created by EZ-Trainer at 5/5/2022
Feature: Test for Amazon search


   Scenario: Verify that user can search for Cancel order
    Given Open Amazon page
    When Search for Cancel order
    Then Verify search results for "Cancel order" are shown

