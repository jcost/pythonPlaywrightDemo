from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        print(page.title())
        input("Press Enter to close the browser...")

if __name__ == "__main__":
    test_example()