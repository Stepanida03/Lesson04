Откройте сайт pypi, раздел allure-pytest.

Скопируйте команду для подключения:

pip install allure-pytest

Откройте терминал и перейдите к рабочей директории (lesson9):

cd 10_Lesson

Подключите Allure:

pip install allure-pytest

Запустите тесты и укажите путь к каталогу результатов тестирования:

python -m pytest --alluredir allure-result

В директории с тестами появится папка allure-result. Там сохранятся отчеты о тестах.

Команда ниже запускает Allure и конвертирует результаты теста в отчет:

allure serve allure-result

Чтобы терминал распознал команду

allure

Установите Allure Report.

Allure Report — это утилита. Она обрабатывает результаты тестирования и создает HTML-отчет.

Пользователи macOS: запустите в терминале VS Code команду

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Затем команду

brew install allure
Пользователи Windows: запустите в терминале VS Code команду

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
Затем команду

scoop install allure
Теперь терминал распознает команду
allure
. Введите команду ниже — сгенерируется отчет о тестах:
allure serve allure-results
Отчет откроется на локальном сервере в окне вашего браузера.

Overview — раздел с общей информацией: сколько всего тестов запустили, процент успешных тестов, доля успешных и неуспешных тестов.

В разделе Suits — список тестов и конкретная информация о каждом из них.