from .base_page import BasePage
from .locators import LoginPageLocators

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
    
    def register_new_user(email, password):      #Добавьте в LoginPage метод register_new_user(email, password),
        email = str(time.time()) + "@fakemail.org"
        password = "Password1)"
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"  #Гость открывает главную страницу логина
        page = LoginPage(browser, link)
        page.open() #Гость открывает главную страницу логина
        email_imput = browser.find_element(By.ID, "#id_registration-email")
        email_imput.send_keys(email)
        password_input = browser.find_element(By.ID, "#id_registration-password1")
        password_input.send_keys(password)
        password_confirm_input = browser.find_element(By.ID, "#id_registration-password2")
        password_confirm_input.send_keys(password)
        register_button = browser.find_element(By.CSS_SELECTOR, "registration_submit")
        register_button.click()
        #REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
       

