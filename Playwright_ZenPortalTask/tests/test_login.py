from pages.login_page import LoginPage
from playwright.sync_api import expect


def test_valid_login(page):
   login_page = LoginPage(page)
   # Arrange
   login_page.visit("https://www.zenclass.in/login")
   # Act
   # Waiting for locators to be present on the webpage
   page.wait_for_selector("text=Email ID" and "text=Password")
   page.wait_for_selector("text=Sign in")
   login_page.login("ramyabhat.v@gmail.com","Raksh@2025")
   # Assert the login page details
   expect(page).to_have_title("GUVI")
   expect(page.locator("text=Dashboard")).to_be_enabled()   
   expect(page.locator("text=Welcome,Ramya V")).to_be_visible()
   # Take a screenshot of the successful login page
   page.screenshot(path="Playwright_ZenPortalTask/screenshot/WelcomeScreen_Valid_Credentials.png") 
   # Logout after successful login
   login_page.logout()


def test_invalid_login(page):
   login_page = LoginPage(page)
   login_page.visit("https://www.zenclass.in/login")
   page.wait_for_selector("text=Email ID" and "text=Password")
   page.wait_for_selector("text=Sign in")
   # Entering invalid credentials to check the error functionality
   login_page.login("ram@xyz.com","1177tt72")
   expect(page.locator("form")).to_contain_text("*Incorrect password!")
   # Take a screenshot of the error message
   print("Taking screenshot of the error screen...")
   page.screenshot(path="Playwright_ZenPortalTask/screenshot/ErrorScreen_Invalid_Credentials.png")


def test_login_without_entering_credentials(page):
   login_page = LoginPage(page)
   login_page.visit("https://www.zenclass.in/login")
   page.wait_for_selector("text=Email ID" and "text=Password")
   page.wait_for_selector("text=Sign in")
   # Passing empty strings as email and password to check the error functionality
   login_page.login("","")
   expect(page.locator("form")).to_contain_text("Email and password required!")
   # Take a screenshot of the error message
   print("Taking screenshot of the error screen...")
   page.screenshot(path="Playwright_ZenPortalTask/screenshot/ErrorScreen_Without_Credentials.png")

