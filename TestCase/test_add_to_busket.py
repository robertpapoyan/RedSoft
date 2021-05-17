from selenium import webdriver
from PageObjects import NecessaryPageObjects
import time

class Test_Add_To_Busket():
    baseURL = "https://specialty.ru/"

    def test_add_to_busket(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.web = NecessaryPageObjects.NecessaryPageObjects(self.driver)

        self.web.goToCofeesPage()
        self.actualName = "Набор кофе Африка NWCC"

        self.web.openCoffeeInnerPage()
        self.web.addToBusket()

        time.sleep(4)

        self.web.goToBusket()

        time.sleep(3)

        if self.driver.find_element_by_link_text(self.actualName):
            assert True
        else:
            assert False

        self.driver.close()

