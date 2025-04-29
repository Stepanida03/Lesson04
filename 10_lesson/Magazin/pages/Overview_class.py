from selenium.webdriver.common.by import By

class OverviewPage:

    def __init__(self, _driver):
        """
        Инициализация страницы итоговой информации.
        """
        self.driver = _driver

    def overview(self):
        """
        Выыод итоговой суммы.
        """
        itogo = self.driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label").text
        return itogo