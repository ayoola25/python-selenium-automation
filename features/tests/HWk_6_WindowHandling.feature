# Created by EZ-Trainer at 6/30/2022
Feature: Test to show window Handling

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    And Store original window
    When Click on Amazon Privacy Notice link
    And Switch to new window
    Then Verify Amazon Privacy Notice page is opened
    And Close Privacy Notice
    And User can close new window and switch back to original window