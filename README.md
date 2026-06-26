# [Playwright](https://playwright.dev/)
## Устанавливаем библиотеку Playwright, командой: 
> pip install playwright
## Устанавливаем браузеры: 
> playwright install
# [Pytest](https://docs.pytest.org/en/stable/)
## Устанавливаем pytest, командой: 
> pip install pytest
## Повторение CSS локаторов
### [Документация по работе с CSS](https://www.w3schools.com/css/default.asp)
### [Документация по составлению CSS локаторов](https://www.w3schools.com/cssref/css_selectors.php)
### [Интерактивный тренажёр по CSS-селекторам](https://flukeout.github.io/)
### [Псевдокласс nth-child](https://www.w3schools.com/cssref/sel_nth-child.php)
## Повторение XPath локаторов
### [Документация по работе с XPath](https://www.w3schools.com/xml/xpath_syntax.asp)
### [Интерактивный тренажёр по XPath](https://automationfc.github.io/xpath-dinner/)
## Pytest маркировки (markers)
### Вывести зарегестрированные маркеровки 
> python -m pytest --markers
### [Официальная документация Pytest по работе с маркировками](https://docs.pytest.org/en/stable/example/markers.html)
### [Официальная документация Pytest по регистрации маркировок](https://docs.pytest.org/en/stable/example/markers.html#registering-markers)
### [Официальная документация Pytest по работе с маркировкой skip](https://docs.pytest.org/en/stable/how-to/skipping.html#skipping-test-functions)
### [Официальная документация Pytest по работе с маркировкой skipif](https://docs.pytest.org/en/stable/how-to/skipping.html#id1)
### [Официальная документация Pytest по работе с маркировкой xfail](https://docs.pytest.org/en/stable/how-to/skipping.html#xfail-mark-test-functions-as-expected-to-fail)
## Фикстуры в pytest
### [Официальная документация Pytest по работе с фикстурами](https://docs.pytest.org/en/6.2.x/fixture.html)
### [Официальная документация Pytest по работе с conftest.py файлами](https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files)
#### Scope фикстуры:
> autouse=True - запускаеться автоматически на каждый тест (имет дефолтное значение )
>
> scope="session" - используеться один раз на тестовую ссесию
> 
> scope="class" - используеться один раз на тестовый класс 
> 
> scope="function" - используеться на каждую функцию
## Работа с плагином pytest-playwright
### [Официальная документация плагина pytest-playwright](https://playwright.dev/python/docs/intro)
> pip install pytest-playwright
## Знакомство с pytest плагинами
### [Официальная документация по pytest плагинам](https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html)
### [Список всех доступных плагинов](https://docs.pytest.org/en/stable/reference/plugin_list.html)
## Параметризация в pytest
### [Официальная документация pytest по параметризации](https://docs.pytest.org/en/7.1.x/how-to/parametrize.html)
### [Официальная документация Pytest по работе с идентификаторами в параметризации](https://docs.pytest.org/en/stable/example/parametrize.html#different-options-for-test-ids)
## Перезапуск автотестов в pytest
### [pytest-rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures)
## Знакомство с Page Object
### [Документация от playwright](https://playwright.dev/python/docs/pom)
### [Документация от selenium](https://selenium-python.readthedocs.io/page-objects.html)
## Знакомство с PageFactory
### [Первая статья о PageFactory на Python](https://habr.com/ru/articles/708932/)
### [Подробно о паттерне PageFactory](https://habr.com/ru/articles/896936/)
## Автоматическое добавление флагов в pytest
### [Официальная документация Pytest по добавлению флагов к команде запуска тестов](https://docs.pytest.org/en/stable/example/simple.html#how-to-change-command-line-options-defaults)

