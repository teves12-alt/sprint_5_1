import unittest
from selenium import webdriver
from locators import *

class TestNavigation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://stellarburgers.education-services.ru"

    def tearDown(self):
        self.driver.quit()

    # Тест 3: Вход разными способами
    def test_different_login_methods(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Вход по кнопке «Войти в аккаунт» на главной
        driver.find_element_by_xpath(LOGIN_BUTTON_MAIN).click()
        self.assertIn("/login", driver.current_url)
        driver.back()

        # 2. Вход через «Личный кабинет»
        driver.find_element_by_xpath(PERSONAL_ACCOUNT_BUTTON).click()
        self.assertIn("/login", driver.current_url)
        driver.back()

        # 3. Вход из формы регистрации
        driver.find_element_by_xpath(LOGIN_IN_FORM).click()
        self.assertIn("/login", driver.current_url)
        driver.back()

        # 4. Вход из формы восстановления пароля
        driver.find_element_by_xpath(LOGIN_RECOVERY_FORM).click()
        self.assertIn("/login", driver.current_url)

    # Тест 4: Переход в личный кабинет
    def test_personal_account_transition(self):
        # Предполагаем, что пользователь уже авторизован
        driver = self.driver
        driver.get(f"{self.base_url}/account")
        self.assertTrue(driver.find_element_by_xpath("//h2[contains(text(), 'Личный кабинет')]"))

    # Тест 5: Переход из ЛК в конструктор
    def test_constructor_transition(self):
        driver = self.driver
        driver.get(f"{self.base_url}/account")  # Заходим в ЛК
        driver.find_element_by_xpath(CONSTRUCTOR_LINK).click()  # Кликаем «Конструктор»
        self.assertIn("/", driver.current_url)  # Должны оказаться на главной

        driver.get(f"{self.base_url}/account")  # Снова в ЛК
        driver.find_element_by_xpath(LOGO_LINK).click()
        self.assertIn("Stellar Burgers", driver.title)

    # Тест 6: Выход из аккаунта
    def test_logout(self):
        driver = self.driver
        driver.get(f"{self.base_url}/account")
        driver.find_element_by_xpath(LOGOUT_BUTTON).click()

        # Проверяем, что вышли (редирект на главную)
        self.assertTrue(driver.find_element_by_xpath("//h1[contains(text(), 'Собери свой бургер')]"))

    # Тест 7: Разделы конструктора
    def test_constructor_sections(self):
        driver = self.driver
        driver.get(self.base_url)

        # Переходим в раздел «Булки»
        driver.find_element_by_xpath(BUNS_SECTION).click()
        bun_element = driver.find_element_by_xpath("//div[contains(@class, 'Bun') and .//span[text()='Булка']]")
        self.assertTrue(bun_element.is_displayed())

        # В раздел «Соусы»
        driver.find_element_by_xpath(SAUCES_SECTION).click()
        sauce_element = driver.find_element_by_xpath("//span[contains(., 'Соус')]")
        self.assertTrue(sauce_element.is_displayed())

        # В раздел «Начинки»
        driver.find_element_by_xpath(FILLINGS_SECTION).click()
        filling_element = driver.find_element_by_xpath("//span[contains(., 'Начинка')]")
        self.assertTrue(filling_element.is_displayed())
