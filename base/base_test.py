import pytest
from pages.home_page import HomePage
from pages.vacancies_page import VacanciesPage


class BaseTest:

    home_page = HomePage
    vacancies_page = VacanciesPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.home_page = HomePage(driver)
        request.cls.vacancies_page = VacanciesPage(driver)
