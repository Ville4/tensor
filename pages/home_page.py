from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
import time

class HomePage(BasePage):

    PAGE_URL = Links.HOST

    VACANCIES_LINK = ["xpath", "//a[@href='/vacancies']"]

    @allure.step("Click on vacancies link")
    def click_on_vacancies_link(self):
        self.wait.until(EC.element_to_be_clickable(self.VACANCIES_LINK)).click()
