from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
from .pages.locators import BasePageLocators
from .pages.basket_page import BasketPage
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = BasePage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = BasePage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_there_should_be_login_url(browser):
#     link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_url()
#
# def test_there_should_be_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_form()
#
#
# def test_there_should_be_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb//"  #ГГость открывает главную страницу
    page = BasketPage(browser, link)
    page.open()
    page.should_open_the_basket() # Переходит в корзину по кнопке в шапке
    page.empty_basket() # Ожидаем, что в корзине нет товаров   # Ожидаем, что есть текст о том что корзина пуста

def test_guest_cant_see_product_in_basket_opened_from_main_page_negative(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb//"  #ГГость открывает главную страницу
    page = BasketPage(browser, link)
    page.open()
    page.should_open_the_basket() # Переходит в корзину по кнопке в шапке
    page.empty_basket_negative() #Негатвный Ожидаем, что в корзине нет товаров   # Ожидаем, что есть текст о том что корзина пуста