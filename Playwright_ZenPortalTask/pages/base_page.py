class BasePage:
   def __init__(self,page):
       self.page = page

   def visit(self,url):
       self.page.goto(url)

   def fill(self, selector, value):
       self.page.locator(selector).is_visible()
       if not self.page.locator(selector).is_visible():
           raise Exception(f"Selector {selector} is not visible on the page.")
       self.page.locator(selector).fill(value)
       print(f"Filling {selector} with value: {value}")

   def click(self,selector):
        self.page.locator(selector).is_visible()
        print(f"Clicking on {selector}")
        # Wait for the element to be visible before clicking
        self.page.locator(selector).click()

   def get_text(self,selector):
       return self.page.wait_for_selector(selector).inner_text()

   def wait_for_selector(self, selector):
       self.page.wait_for_selector(selector)
   
   def is_visible(self, selector):
        return self.page.locator(selector).is_visible()
   


    