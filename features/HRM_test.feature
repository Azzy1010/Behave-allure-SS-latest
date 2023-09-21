Feature: OrangeHRM
  Scenario: Login_user_is_visible
    Given  launch_browser
    When  Open_URL
    Then check_if user can login
    And  close_browser
