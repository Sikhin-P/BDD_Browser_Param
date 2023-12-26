Feature: Search Item
  Scenario: Search for an Item
    Given Open a browser
    And Navigate to "https://www.Amazon.in"
    When Search with "Camera"
    Then Save search results to text file

