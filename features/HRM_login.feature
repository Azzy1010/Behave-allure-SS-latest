Feature: OrangeHRM
  Scenario: Login title check
    Given  launch browser
    When  Open URL
    Then  compare if the URL has been opened
    And  close
