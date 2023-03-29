from .base_page import BasePage
from .locators import ProductPageLocators
import math


class PageObject(BasePage):
    
    def should_be_book_page(self):
        self.click_add_to_backet_button()
        self.should_be_book_page()
        self.should_be_same_product()
        self.should_be_same_price()

    def click_add_to_backet_button(self):
        button = self.browser.find_element(*ProductPageLocators.Add_to_basket_button)
        button.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), ("Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), ("Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name in message, "No product name in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), ("Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), ("Product price is not presented")       
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "No product price in the message"
