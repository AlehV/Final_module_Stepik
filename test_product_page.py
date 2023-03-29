from selenium.common.exceptions import NoAlertPresentException
from .pages.product_page import PageObject
import time
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, link)
    page.open()
    page.click_add_to_backet_button()
    page.solve_quiz_and_get_code() #Решение задачи с помощью данной функции.
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()