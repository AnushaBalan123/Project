
import logging
import time
import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from VolvoProject.Config.config import TestData

def pytest_configure(config):
    """Configure the logger to write to the HTML report."""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Capture log messages and attach them to the test report."""
    if call.when == 'call':
        # Capture log messages
        logger = logging.getLogger()
        log_capture = ""
        for handler in logger.handlers:
            if hasattr(handler, 'stream') and hasattr(handler.stream, 'getvalue'):
                log_capture += handler.stream.getvalue()
        # Attach logs to the report
        if log_capture:
            report = item._report
            report.sections.append(('Log', log_capture))

def pytest_html_report_title(report):
    report.title = "Volvo Project!"

@pytest.fixture(scope="class")
def test_setup(request):  # 'request' can be used if you need to interact with the test class
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(TestData.base_url)

    # Assigning the driver to the class instance
    request.cls.driver = driver

    yield

    time.sleep(10)
    driver.quit()
    print("Test Completed")