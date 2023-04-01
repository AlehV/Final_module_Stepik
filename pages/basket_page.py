from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    
    def empty_basket(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"

    def empty_basket_negative(self):
        assert not self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "Basket is empty"