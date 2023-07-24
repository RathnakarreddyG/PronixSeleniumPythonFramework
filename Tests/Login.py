from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
BaseCase.main(__name__, __file__)


class LoginInto(BaseCase):
    def login(self):
        self.open("http://183.82.123.57:3000/login")
        self.send_keys('email', 'admin', By.NAME, 10)
        self.send_keys('password', '123qwe', By.NAME, 10)
        self.click("button")
        self.wait(2)
        self.select_option_by_text("facility","Apollo",By.ID,10)
        self.select_option_by_text("roles","ADMIN",By.ID,10)
        self.click("button")
        self.wait(5)
        self.click("user", By.CLASS_NAME, 5)
    def logout(self):
        self.click('')
        

        
