from base.base_test import BaseTest
import allure
import pytest

@allure.feature("Vacancies page functionality")
class TestVacanciesPopup(BaseTest):
    @allure.title("Сlick on element opens popup")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_click_on_element_opens_popup(self):
        self.home_page.open()
        self.home_page.click_on_vacancies_link()
        self.vacancies_page.is_openned()
        self.vacancies_page.click_on_all_directions_button()
        self.vacancies_page.click_on_software_dev_link()
        self.vacancies_page.is_page_url_switched()
        self.vacancies_page.make_screenshot("Success")
