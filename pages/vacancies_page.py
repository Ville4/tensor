from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure

class VacanciesPage(BasePage):

    PAGE_URL = Links.VACANCIES_PAGE

    ALL_DIRECTIONS_BUTTON = ["xpath", "//div[@name='category']"]
    ALL_DIRECTIONS_POPUP = ["xpath", "//div[@templatename='Controls/filterPopup:SimplePanel']"]
    POPUP_SOFTWARE_DEV_LINK = ["xpath", "//span[text()='Разработка ПО']"]


    Link = Links()
    PAGE_URL_POPUP_SOFTWARE_DEV_LINK = Link.VACANCIES_PAGE_FILTER(1)

    @allure.step("Click on all directions button")
    def click_on_all_directions_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ALL_DIRECTIONS_BUTTON)).click()

    @allure.step("Click on software development link in popup")
    def click_on_software_dev_link(self):
        self.wait.until(EC.element_to_be_clickable(self.ALL_DIRECTIONS_POPUP))
        self.wait.until(EC.element_to_be_clickable(self.POPUP_SOFTWARE_DEV_LINK)).click()

    @allure.step("Click on software development link in popup")
    def click_on_software_dev_link(self):
        self.wait.until(EC.element_to_be_clickable(self.ALL_DIRECTIONS_POPUP))
        self.wait.until(EC.element_to_be_clickable(self.POPUP_SOFTWARE_DEV_LINK)).click()

    @allure.step("Page url is switched to right url")
    def is_page_url_switched(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL_POPUP_SOFTWARE_DEV_LINK))




