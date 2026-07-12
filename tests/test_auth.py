import unittest
from selenium import webdriver
from fixtures import generate_email, generate_password
from locators import *

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://stellarburgers.education-services.ru"

    def tearDown(self):
        self.driver.quit()

    # Тест 1: Успешная регистрация
    def test_successful_registration(self):
        driver = self.driver
        driver.get(f"{self.base_url}/register")

        name = "Test User"
        email = generate_email()
        password = generate_password(8)

        # Заполняем форму
        driver.find_element_by_xpath(NAME_FIELD).send_keys(name)
        driver.find_element_by_xpath(EMAIL_FIELD).send_keys(email)
        driver.find_element_by_xpath(PASSWORD_FIELD).send_keys(password)
        driver.find_element_by_xpath(REGISTER_BUTTON).click()

        # Проверяем, что регистрация прошла успешно (редирект на главную)
        self.assertIn(self.base_url, driver.current_url)

    # Тест 2: Ошибка при коротком пароле
    def test_invalid_password_registration(self):
        driver = self.driver
        driver.get(f"{self.base_url}/register")

        name = "Test User"
        email = generate_email()
        short_password = "123"  # слишком короткий

        driver.find_element_by_xpath(NAME_FIELD).send_keys(name)
        driver.find_element_by_xpath(EMAIL_FIELD).send_keys(email)
        driver.find_element_by_xpath(PASSWORD_FIELD).send_keys(short_password)
        driver.find_element_by_xpath(REGISTER_BUTTON).click()

        error_message = driver.find_element_by_xpath(ERROR_MESSAGE).text
        self.assertTrue("Пароль слишком короткий" in error_message)
