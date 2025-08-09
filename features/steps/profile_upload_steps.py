import os
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the paths for the test files
LARGE_FILE_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..", "resources", "large-image.jpeg")
)
SMALL_FILE_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..", "resources", "small-image.jpeg")
)

HTML_FILE_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..", "qa-lead-assignment-homepage.html")
)


@given("I as a new user gets registered")
def signup_as_new_user(context):
    """
    Simulates a registered user by interacting with the signup form.
    """
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("http://localhost:8080/qa-lead-assignment-homepage.html")
    
    # Wait for page to load
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "signup-username"))
    )

    # Sign up a new user
    username_field = context.driver.find_element(By.ID, "signup-username")
    password_field = context.driver.find_element(By.ID, "signup-password")
    signup_button = context.driver.find_element(By.XPATH, "//div[@id='signup']//button")

    username_field.clear()
    username_field.send_keys("testuser99")
    password_field.clear()
    password_field.send_keys("testuser99")
    
    # Wait before clicking signup button
    time.sleep(2)
    signup_button.click()

    # Handle the alert pop-up
    try:
        WebDriverWait(context.driver, 10).until(EC.alert_is_present())
        alert = context.driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        pass  # No alert present, continue
    
    # Wait after signup completion
    time.sleep(5)


@given("I have logged into the application with credentials")
def login_as_registered_user(context):
    """
    Logs in the registered user to access the profile page.
    """
    # Wait before starting login process
    time.sleep(3)
    
    # Use the same credentials that were used for signup
    login_username_field = context.driver.find_element(By.ID, "login-username")
    login_password_field = context.driver.find_element(By.ID, "login-password")
    login_button = context.driver.find_element(By.XPATH, "//div[@id='login']//button")

    login_username_field.clear()
    login_username_field.send_keys("testuser99")
    login_password_field.clear()
    login_password_field.send_keys("testuser99")
    
    # Wait before clicking login button
    time.sleep(2)
    login_button.click()

    # Handle any alert that might appear
    try:
        WebDriverWait(context.driver, 3).until(EC.alert_is_present())
        alert = context.driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        pass  # No alert present, continue

    # Wait for the profile section to become visible after login
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "profile"))
    )
    
    # Wait after successful login
    time.sleep(3)


@when("I try to upload a profile picture with a size greater than 5MB")
def upload_large_profile_picture(context):
    """
    Finds the file input element and uploads a large file.
    """
    # Wait before starting upload process
    time.sleep(2)
    
    # Wait for the file input element to be present and visible
    file_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "profile-pic"))
    )

    # Upload the large file using its relative path
    file_input.send_keys(LARGE_FILE_PATH)
    
    # Wait after file selection
    time.sleep(2)

    # Click the upload button
    upload_button = context.driver.find_element(By.XPATH, "//button[text()='Upload']")
    upload_button.click()
    
    # Wait after upload button click
    time.sleep(2)


@then("I should see a message indicating the upload failed due to file size")
def error_message_for_large_file(context):
    """
    Checks for the specific error message on the page.
    """
    # Wait for the error message to become visible and verify its text
    error_message_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "upload-msg"))
    )
    assert "File is too large. Max allowed size is 5MB." in error_message_element.text


@then("I should not see the file name as uploaded")
def to_check_the_uploaded_file_name_as_success_class_for_large_file(context):
    """
    Checks if the success class is not applied, indicating failure.
    """
    message_element = context.driver.find_element(By.ID, "upload-msg")
    assert "Uploaded: large-image.jpeg" not in message_element.text


@then("I should see a clear error message")
def error_message_assertion(context):
    """
    A step to reinforce the clarity of the error message for the test.
    """
    message_element = context.driver.find_element(By.ID, "upload-msg")
    assert "File is too large. Max allowed size is 5MB." in message_element.text


@when("I try to upload a profile picture with a size less than or equal to 5MB")
def upload_small_profile_picture(context):
    """
    Uploads a small file and triggers the upload process.
    """
    # Wait before starting second upload process
    time.sleep(3)
    
    # Wait for the file input element to be present
    file_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "profile-pic"))
    )
    
    # Clear any previous file selection
    file_input.clear()
    file_input.send_keys(SMALL_FILE_PATH)
    
    # Wait after file selection
    time.sleep(2)

    upload_button = context.driver.find_element(
        By.XPATH, "//div[@id='profile']//button[1]"
    )
    upload_button.click()
    
    # Wait after upload button click
    time.sleep(2)


@then("I should see a success message with the file name")
def verify_success_message_with_filename(context):
    """
    Verifies that a success message is displayed with the uploaded file name.
    """
    # Wait for the success message to become visible
    success_message_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "upload-msg"))
    )
    
    # Check that the message contains the file name and has success styling
    assert "Uploaded: small-image.jpeg" in success_message_element.text
    assert "success" in success_message_element.get_attribute("class")


@then("I as a user logs out of the application")
def user_logs_out(context):
    """
    Verifies the logout functionality.
    """
    # Wait before logout
    time.sleep(3)
    
    logout_user_field = context.driver.find_element(
        By.XPATH, "//button[normalize-space()='Logout']"
    )
    logout_user_field.click()
    
    # Wait for the page to reload and show login form
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login"))
    )
    
    # Wait before closing browser
    time.sleep(2)
    context.driver.quit()