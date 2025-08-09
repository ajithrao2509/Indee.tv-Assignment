Feature: Profile Picture Upload Validation
  As a registered user,
  I want to upload a profile picture,
  So that I can personalize my profile.

  Scenario: Verify image upload success and failure based on file size
    Given I as a new user gets registered
    And I have logged into the application with credentials
    When I try to upload a profile picture with a size greater than 5MB
    Then I should see a message indicating the upload failed due to file size
    Then I should not see the file name as uploaded
    And I should see a clear error message
    When I try to upload a profile picture with a size less than or equal to 5MB
    Then I should see a success message with the file name