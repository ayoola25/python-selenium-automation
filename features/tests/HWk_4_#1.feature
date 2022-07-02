# Created by EZ-Trainer at 6/13/2022
Feature: Tests for Bestsellers Links

  Scenario: Verify that Bestsellers links can be opened
    Given Open Amazon Bestsellers page
    Then Verify there are 5 links