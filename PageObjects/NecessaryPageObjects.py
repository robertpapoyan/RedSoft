
from selenium.webdriver.support.ui import Select
import time

class NecessaryPageObjects:
    cofees_button_css_selector = ".main-header__submenu > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)"
    coffee_name_linktext = "Набор кофе Африка NWCC"
    coffee_inner_add_to_busket_css_selector = ".product-page-cart__btn > button:nth-child(1)"
    busket_button_css_selector = "div.main-header__shop-menu:nth-child(4) > div:nth-child(1) > a:nth-child(2)"

    def __init__(self,driver):
        self.driver = driver

    def goToCofeesPage(self):
        self.driver.find_element_by_css_selector(self.cofees_button_css_selector).click()

    def openCoffeeInnerPage(self):
        self.driver.find_element_by_link_text(self.coffee_name_linktext).click()

    def addToBusket(self):
        self.driver.find_element_by_css_selector(self.coffee_inner_add_to_busket_css_selector).click()

    def goToBusket(self):
        self.driver.find_element_by_css_selector(self.busket_button_css_selector).click()

