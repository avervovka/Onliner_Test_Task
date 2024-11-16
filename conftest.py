import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture(scope="module")
def browser():
    driver = DriverFactory.create_driver()
    yield driver
    driver.quit()