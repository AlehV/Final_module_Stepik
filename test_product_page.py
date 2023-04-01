from selenium.common.exceptions import NoAlertPresentException
from .pages.product_page import PageObject
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
from .pages.locators import BasePageLocators
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" #Открываем страницу товара
#     page = PageObject(browser, link)
#     page.open()
#     page.click_add_to_backet_button() #Добавляем товар в корзину
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()#    Проверяем, что нет сообщения об успехе с помощью is_not_element_present

# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" #Открываем страницу товара
#     page = PageObject(browser, link)
#     page.open()
#     page.click_add_to_backet_button() #Добавляем товар в корзину
#     page.solve_quiz_and_get_code()
#     page. should_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_disappeared
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = PageObject(browser, link)
#     page.open()
#     page.go_to_login_page()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"  #Гость открывает страницу товара
#     page = BasketPage(browser, link)
#     page.open()
#     page.should_open_the_basket() # Переходит в корзину по кнопке в шапке
#     page.empty_basket() # Ожидаем, что в корзине нет товаров   # Ожидаем, что есть текст о том что корзина пуста
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page_negative(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"  #Гость открывает страницу товара
#     page = BasketPage(browser, link)
#     page.open()
#     page.should_open_the_basket() # Переходит в корзину по кнопке в шапке
#     page.empty_basket_negative()#НЕГАТИВНЫЙ  Ожидаем, что в корзине нет товаров   # Ожидаем, что есть текст о том что корзина пуста.

@pytest.mark.registration
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)     #добавить фикстуру сетап. внетри нее
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"  # открыть страницу регистрации
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Password1)"
        page.register_new_user(email, password)  # зарегать нового польщователя
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"  # Открываем страницу товара
        page = PageObject(browser, link)
        page.open()
        page.should_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5"
        page = PageObject(browser, link)
        page.open()
        page.click_add_to_backet_button()
        page.solve_quiz_and_get_code()  # Решение задачи с помощью данной функции.
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()


