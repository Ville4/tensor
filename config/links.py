class Links:

    HOST = "https://tensor.ru"
    VACANCIES_PAGE = f"{HOST}/vacancies?filter_region=7600000100000000000"

    def VACANCIES_PAGE_FILTER(self, category_num, filter_region='7600000100000000000'):
         return f"https://tensor.ru/vacancies?filter_region={filter_region}&filter_category={category_num}"

