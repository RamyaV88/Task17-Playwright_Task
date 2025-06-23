from pages.base_page import BasePage


class LoginPage(BasePage):
   def __init__(self, page):
       super().__init__(page)
       self.email_id = ('[placeholder="Enter your mail"]')
       self.password_input = ('[placeholder="Enter your password "]')
       self.login_button = 'button:has-text("Sign in")'
       self.profile_click = ("#profile-click-icon")
       self.logout_button = ('//div[normalize-space()="Log out"]')


   def login(self, email, password):
       self.fill(self.email_id, email)
       self.fill(self.password_input, password)
       self.click(self.login_button)

   
   def logout(self):
        # Ensure the logout button is visible before clicking
        self.page.locator(self.profile_click).is_visible()
        # Click the profile icon to open the dropdown
        self.click(self.profile_click)
        # Click the logout button
        self.click(self.logout_button)
        print("Logging out...")
        # Wait for the logout to complete and return the current URL
        return self.page.url