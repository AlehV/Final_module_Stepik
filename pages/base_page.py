from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, CSS_SELECTOR, login_link):
        try:
            self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        except (NoSuchElementException):
            return False
        return True