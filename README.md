# test-authorization-block
 training Python Selenium

Учебные автоматизированные тесты для формы авторизации с использованием Python, Selenium и паттерна Page Object.  
Проект демонстрирует автоматизацию тестирования формы авторизации на сайте [https://berpress.github.io/selenium-login-demo/](https://berpress.github.io/selenium-login-demo/).
Тесты проверяют различные сценарии входа в систему, включая:

1.Успешную авторизацию с правильными учетными данными  
2.Неуспешную авторизацию с неверным логином  
3.Неуспешную авторизацию с неверным паролем

Структура проекта

```` 
test-authorization-block/
├── .github/workflows/           # Конфигурация GitHub Actions
├── locators/                    # Локаторы элементов страницы
├── pages/                       # Классы страниц (Page Objects)
│   ├── base_page.py             # Базовая страница с общими методами
│   └── login_page.py            # Страница авторизации
├── tests/                       # Тестовые файлы
│   ├── conftest.py              # Конфигурация pytest и фикстуры
│   └── test_login_page.py       # Тесты
├── .gitignore                   # Исключения репозитория
├── pytest.ini                   # Конфигурация pytest
└── requirements.txt             # Зависимости проекта

````

Установка Клонируйте репозиторий:
```bash
git clone https://github.com/evoixrs/test-authorization-block.git
```
Создайте и активируйте виртуальное окружение:

### Windows
````
python  -m venv venv  venv\Scripts\activate
````
### Linux/MacOS
````
python  -m venv venv  source venv/bin/activate
````
### Установите зависимости:  
bash
````
pip install  -r requirements.txt
````
### Запуск всех тестов:  
bash
````
pytest
````
### Запуск конкретного тестового файла:  
bash 
````
pytest tests/test_login_page.py
````
### Запуск с генерацией отчета:  
bash
````
pytest  --junit-xml=reports/results.xml
````