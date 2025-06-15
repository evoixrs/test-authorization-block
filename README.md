# test-authorization-block
 training Python Selenium

Этот проект представляет собой учебные автоматизированные тесты для формы авторизации с использованием 
Python, Selenium и паттерна Page Object

Проект демонстрирует автоматизацию тестирования формы авторизации на сайте https://berpress.github.io/selenium-login-demo/. 
Тесты проверяют различные сценарии входа в систему, включая:
1. Успешную авторизацию с правильными учетными данными
2. Неуспешную авторизацию с неверным логином
3. Неуспешную авторизацию с неверным паролем

test-authorization-block/
├── .github/workflows/    # Конфигурация GitHub Actions
├── locators/             # Локаторы элементов страницы
├── pages/                # Классы страниц (Page Objects)
│   ├── base_page.py      # Базовая страница с общими методами
│   ├── loginform.py      # Страница авторизации (первая версия)
│   └── loginform_2.py    # Улучшенная страница авторизации
├── tests/                # Тестовые файлы
│   ├── conftest.py       # Конфигурация pytest и фикстуры
│   ├── test_loginform_1.py  # Базовые тесты авторизации
│   ├── test_loginform_2.py  # Тесты с использованием Page Object
│   ├── test_loginform_3.py  # Тесты с использованием фикстур
│   └── test_loginform_4.py  # Расширенные тесты с базовой страницей
├── .gitignore            # Файлы, исключенные из репозитория
├── pytest.ini            # Конфигурация pytest
└── requirements.txt      # Зависимости проекта

Установка

Клонируйте репозиторий:
bashgit clone https://github.com/ваш-пользователь/test-authorization-block.git
cd test-authorization-block

Создайте и активируйте виртуальное окружение:
bash# Windows
python -m venv venv
venv\Scripts\activate

**Linux/MacOS**

python -m venv venv
source venv/bin/activate

Установите зависимости:
bashpip install -r requirements.txt

Установите веб-драйвер для Chrome (если не установлен):

Скачайте ChromeDriver соответствующей версии
Добавьте его в PATH или укажите путь в коде

Запуск тестов
Запуск всех тестов:
bashpytest
Запуск конкретного тестового файла:
bashpytest tests/test_loginform_4.py
Запуск с генерацией отчета:
bashpytest --junit-xml=reports/results.xml
Запуск в режиме без графического интерфейса (headless):
bashpytest --headless
Запуск с указанием URL:
bashpytest --url="https://berpress.github.io/selenium-login-demo/"
