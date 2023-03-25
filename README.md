# pytest_ui_api

## Шаблон для автоматизации тестирования на python

### Шаги
1.  Склонировать проекти `git clone https://github.com/BeHuAMuH1991/pytest_ui_api.git`
2. Установить все зависимости `pip instal -r requiments.txt`
3. запустить тесты `pytest`
4. Сформировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- request
- _sqlalchemy_
- allure
- config
- json
- webdriver meneger 
- configparser

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы по работе с API
- ./db - хелперы по работе с БД
- test_config.ini - настройки для тестов

### Полезные ссылки
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
