# Created by EZ-Trainer at 6/13/2022
Feature: Tests for Bestsellers Functionality

  Scenario: Verify that Bestsellers links are present
    Given Open Amazon Bestsellers page
    Then Verify there are 5 links

  Scenario: Verify that Bestsellers links can be opened
    Given Open Amazon Bestsellers page
    Then User can click through top links and verify correct page opens