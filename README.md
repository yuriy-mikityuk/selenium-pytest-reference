# Selenium Reference Framework

[![CI](https://github.com/yuriy-mikityuk/selenium-pytest-reference/actions/workflows/ci.yml/badge.svg)](https://github.com/yuriy-mikityuk/selenium-pytest-reference/actions/workflows/ci.yml)

**English** · [Русский](README.ru.md)

A reference Selenium 4 + pytest framework: core WebDriver APIs — including BiDi network and log interception, WebAuthn and Shadow DOM — wired into a layered Page Object architecture and verified in CI.

Every UI feature is exercised by a real test against the official Selenium test pages, so the repository doubles as runnable documentation: find the API you need in the table, open the test, then follow it into the page object.

## What's covered

| Area | What the tests exercise | Test file |
|---|---|---|
| Web forms | text, textarea, select, checkbox, radio, file upload, range, color, date, datalist, disabled and readonly inputs | `test_selenium_web_form.py` |
| Keyboard | typing with modifier keys, select-all-and-replace | `test_selenium_web_form.py` |
| Locators | relative locators (`locate_with(...).below()`) | `test_selenium_web_form.py` |
| Waits | dynamically added and revealed elements | `test_first_with_selenium_doc.py` |
| Navigation | back, forward, refresh | `test_navigation.py` |
| Alerts | alert, confirm, prompt | `test_alerts.py` |
| Windows and frames | opening a new window, switching into an iframe | `test_switch_to_new_window.py`, `test_frames.py` |
| Cookies | add, get, delete, SameSite | `test_cookies.py` |
| Actions | hover, drag and drop, context and double click, pen input, scroll wheel | `test_mouse_interaction.py`, `test_pen.py`, `test_scroll.py` |
| Shadow DOM | interacting with elements inside a shadow root | `test_shadow_dom.py` |
| Screenshots and printing | page and element screenshots, print to PDF with custom options | `test_screenshots.py`, `test_print_page.py` |
| WebAuthn | virtual authenticator, resident keys, credential management | `test_virtual_authenticator.py` |
| WebDriver BiDi | console logs, JavaScript errors, network request interception | `test_bidi_logging.py`, `test_bidi_network.py` |
| Sessions | isolated browser sessions created on demand by a driver factory | `test_driver_factory.py` |
| REST API | GET, POST and PATCH against JSONPlaceholder with `requests` | `tests/api/test_posts_api.py` |

## Architecture

```
framework/
├── elements/   BaseElement and typed wrappers: Button, TextInput, Checkbox, RadioButton, Dropdown
├── pages/      BasePage and one page object per test page
├── browser/    browser-level services attached to pages (CookieManager)
└── bidi/       WebDriver BiDi helpers (RequestCollector)
tests/
├── conftest.py      driver, page and factory fixtures
├── selenium_doc/    UI tests, one file per Selenium documentation topic
└── api/             REST API tests
```

- **Tests never touch the driver or locators directly.** Everything goes through page objects and element wrappers.
- **Elements** wrap a locator together with the explicit waits around it.
- **Pages** declare `URL` as `ClassVar[str]`, so a page without a URL is caught by the type checker instead of failing later as `driver.get(None)`.
- **Browser services are composed, not inherited.** `page.cookies` is a `CookieManager` instance rather than a set of proxy methods on `BasePage`.
- **Network interception** lives in `RequestCollector`, a context manager: the handler is registered on enter and always removed on exit, even when the test fails.
- **Factory fixtures** create resources on demand. `driver_factory` opens as many independent sessions as a test needs and closes each one through `request.addfinalizer`.

## Quick start

Requires Python 3.12, [uv](https://docs.astral.sh/uv/), Google Chrome and Firefox. Browser drivers are resolved automatically by Selenium Manager.

```bash
uv sync
uv run pytest    # all tests, headless
uv run mypy      # type-check the framework package
```

Run a single area:

```bash
uv run pytest tests/selenium_doc/test_bidi_network.py -v
```

## Known browser issues

Browser bugs hit while building this framework, each reproduced and taken upstream.

**Chrome: BiDi network interception hangs classic navigation.**
With a network intercept active, `driver.get()` blocks until the page load timeout and fails with `Timed out receiving message from renderer`. It affects `continueRequest`, `failRequest` and `continueWithAuth`, so BiDi network tests run on Firefox (see the `firefox_bidi_driver` fixture).
[Chromium issue 425906330](https://issues.chromium.org/issues/425906330) — reproduction matrix across Selenium and ChromeDriver versions contributed by the author.

**ChromeDriver on macOS: Shift+letter produces lowercase text with a Russian input source.**
`test_type_uppercase_text` fails locally on macOS while the Russian input source is active, and passes on Linux in CI.
[Chromium issue 553408024](https://issues.chromium.org/issues/553408024) — reported by the author.
