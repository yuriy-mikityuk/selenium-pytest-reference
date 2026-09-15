# Selenium Reference Framework

[![CI](https://github.com/yuriy-mikityuk/selenium-pytest-reference/actions/workflows/ci.yml/badge.svg)](https://github.com/yuriy-mikityuk/selenium-pytest-reference/actions/workflows/ci.yml)

[English](README.md) · **Русский**

Референсный фреймворк на Selenium 4 и pytest: основные API WebDriver — включая перехват сети и логов через BiDi, WebAuthn и Shadow DOM — встроены в многослойную архитектуру Page Object и проверяются в CI.

Каждая UI-возможность покрыта настоящим тестом на официальных тестовых страницах Selenium, поэтому репозиторий работает как исполняемая документация: находишь нужный API в таблице, открываешь тест, а из него переходишь в page object.

## Что покрыто

| Область | Что проверяют тесты | Файл |
|---|---|---|
| Веб-формы | текст, textarea, select, чекбоксы, радиокнопки, загрузка файла, range, color, date, datalist, disabled и readonly поля | `test_selenium_web_form.py` |
| Клавиатура | ввод с клавишами-модификаторами, выделить всё и заменить | `test_selenium_web_form.py` |
| Локаторы | относительные локаторы (`locate_with(...).below()`) | `test_selenium_web_form.py` |
| Ожидания | динамически добавляемые и появляющиеся элементы | `test_first_with_selenium_doc.py` |
| Навигация | назад, вперёд, обновление | `test_navigation.py` |
| Алерты | alert, confirm, prompt | `test_alerts.py` |
| Окна и фреймы | открытие нового окна, переключение в iframe | `test_switch_to_new_window.py`, `test_frames.py` |
| Куки | добавление, чтение, удаление, SameSite | `test_cookies.py` |
| Действия | наведение, drag and drop, контекстный и двойной клик, ввод пером, колесо прокрутки | `test_mouse_interaction.py`, `test_pen.py`, `test_scroll.py` |
| Shadow DOM | работа с элементами внутри shadow root | `test_shadow_dom.py` |
| Скриншоты и печать | скриншоты страницы и элемента, печать в PDF с настройками | `test_screenshots.py`, `test_print_page.py` |
| WebAuthn | виртуальный аутентификатор, resident keys, управление учётными данными | `test_virtual_authenticator.py` |
| WebDriver BiDi | логи консоли, ошибки JavaScript, перехват сетевых запросов | `test_bidi_logging.py`, `test_bidi_network.py` |
| Сессии | изолированные браузерные сессии, которые фабрика драйверов создаёт по требованию | `test_driver_factory.py` |
| REST API | GET, POST и PATCH к JSONPlaceholder через `requests` | `tests/api/test_posts_api.py` |

## Архитектура

```
framework/
├── elements/   BaseElement и типизированные обёртки: Button, TextInput, Checkbox, RadioButton, Dropdown
├── pages/      BasePage и по одному page object на каждую тестовую страницу
├── browser/    сервисы уровня браузера, подключаемые к страницам (CookieManager)
└── bidi/       помощники для WebDriver BiDi (RequestCollector)
tests/
├── conftest.py      фикстуры драйверов, страниц и фабрик
├── selenium_doc/    UI-тесты, по файлу на каждую тему документации Selenium
└── api/             тесты REST API
```

- **Тесты не обращаются к драйверу и локаторам напрямую.** Всё идёт через page objects и обёртки элементов.
- **Элементы** объединяют локатор с явными ожиданиями вокруг него.
- **Страницы** объявляют `URL` как `ClassVar[str]`, поэтому страницу без URL ловит проверка типов, а не падение `driver.get(None)` во время прогона.
- **Сервисы браузера подключаются композицией, а не наследованием.** `page.cookies` — это экземпляр `CookieManager`, а не набор методов-прокси в `BasePage`.
- **Перехват сети** живёт в `RequestCollector` — контекстном менеджере: обработчик регистрируется на входе и гарантированно снимается на выходе, даже если тест упал.
- **Фикстуры-фабрики** создают ресурсы по требованию. `driver_factory` открывает столько независимых сессий, сколько нужно тесту, и закрывает каждую через `request.addfinalizer`.

## Быстрый старт

Нужны Python 3.12, [uv](https://docs.astral.sh/uv/), Google Chrome и Firefox. Драйверы браузеров Selenium Manager подтягивает автоматически.

```bash
uv sync
uv run pytest    # все тесты, headless
uv run mypy      # проверка типов пакета framework
```

Запустить отдельную область:

```bash
uv run pytest tests/selenium_doc/test_bidi_network.py -v
```

## Известные проблемы браузеров

Баги браузеров, найденные в процессе работы над фреймворком. Каждый воспроизведён и передан разработчикам.

**Chrome: перехват сети через BiDi вешает обычную навигацию.**
При активном сетевом перехвате `driver.get()` блокируется до таймаута загрузки страницы и падает с `Timed out receiving message from renderer`. Затрагивает `continueRequest`, `failRequest` и `continueWithAuth`, поэтому сетевые BiDi-тесты запускаются в Firefox (см. фикстуру `firefox_bidi_driver`).
[Chromium issue 425906330](https://issues.chromium.org/issues/425906330) — матрицу воспроизведения по версиям Selenium и ChromeDriver добавил автор репозитория.

**ChromeDriver на macOS: Shift+буква печатает строчные при русской раскладке.**
`test_type_uppercase_text` падает локально на macOS, когда активна русская раскладка, и проходит на Linux в CI.
[Chromium issue 553408024](https://issues.chromium.org/issues/553408024) — завёл автор репозитория.
