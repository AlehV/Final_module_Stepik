from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not a login URL"
      
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"
    
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*BasePageLocators.EMAIL_IMPUT)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)

        password_confirm_field = self.browser.find_element(*BasePageLocators.PASSWORD_CONFIRM_INPUT)
        password_confirm_field.send_keys(password)
        
        register_button = self.browser.find_element(*BasePageLocators. REGISTER_BUTTON)
        register_button.click()



        
