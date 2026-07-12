"""
Файл содержит локаторы веб‑элементов для автотестов Stellar Burgers.
Каждый локатор — это XPath‑выражение, которое точно находит элемент на странице.
Рекомендуется хранить все локаторы в одном файле, чтобы:
- избежать дублирования;
- быстро находить нужные селекторы;
- легко обновлять их при изменениях в интерфейсе.
"""

# === РЕГИСТРАЦИЯ И АВТОРИЗАЦИЯ ===
NAME_FIELD = "//input[@name='name']"  # Поле ввода имени на странице регистрации
EMAIL_FIELD = "//input[contains(@type, 'email')]"  # Поле для email (ищем по типу)
PASSWORD_FIELD = "//input[contains(@type, 'password')]"  # Поле пароля
REGISTER_BUTTON = "//button[contains(text(), 'Зарегистрироваться')]"  # Кнопка «Зарегистрироваться»
LOGIN_BUTTON_MAIN = "//a[contains(text(), 'Войти в аккаунт')]"  # Ссылка «Войти в аккаунт» с главной страницы
LOGIN_SUBMIT = "//button[@type='submit']"  # Кнопка отправки формы входа
ERROR_MESSAGE = "//div[@class='input__error']"  # Сообщение об ошибке валидации (например, «Пароль слишком короткий»)

# === НАВИГАЦИЯ ===
PERSONAL_ACCOUNT_BUTTON = "//p[contains(text(), 'Личный Кабинет')]"  # Элемент «Личный кабинет» в шапке
CONSTRUCTOR_LINK = "//nav//a[text()='Конструктор']"  # Ссылка «Конструктор» в навигационном меню
LOGO_LINK = "//header//img[@alt='Stellar Burgers']"  # Логотип в шапке (кликабельный)
LOGOUT_BUTTON = "//button[contains(text(), 'Выйти')]"  # Кнопка «Выйти» в профиле

# === РАЗДЕЛЫ КОНСТРУКТОРА БУРГЕРОВ ===
BUNS_SECTION = "//div[@class='Tab_Tab__1STfX' and .//span[text()='Булки']]"  # Вкладка «Булки»
SAUCES_SECTION = "//div[@class='Tab_Tab__1STfX' and .//span[text()='Соусы']]"  # Вкладка «Соусы»
FILLINGS_SECTION = "//div[@class='Tab_Tab__1STfX' and .//span[text()='Начинки']]"  # Вкладка «Начинки»

# === ДОПОЛНИТЕЛЬНЫЕ СПОСОБЫ ВХОДА ===
LOGIN_IN_FORM = "//a[@href='/login']"  # Ссылка «Войти» на странице регистрации
LOGIN_RECOVERY_FORM = "//a[@class='Auth_link__1fOlj']"  # Ссылка входа из формы восстановления пароля
