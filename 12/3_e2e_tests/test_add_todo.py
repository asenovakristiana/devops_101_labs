import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def app_url():
    # Update the URL if your app runs on a different address/port
    return "http://127.0.0.1:8000"


def test_add_todo_item(app_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the app
        page.goto(app_url)

        # Check if the page loaded correctly
        assert page.title() == "Todo App"
       

        # Add a todo item
        todo_text = "Buy groceries"
        page.fill('input[name="todo"]', todo_text)
        page.click('button[type="submit"]')

        # Check if the todo item appears in the list
        todo_list = page.locator("#list-todo li")
        assert todo_list.count() > 0
        assert todo_text in todo_list.last.text_content()

        import time
        time.sleep(10)
        browser.close()