# Onliner Test Task

This project is a test automation framework built using Selenium, Pytest, and the Page Object Model (POM) structure. It is designed to facilitate automated testing of web applications, specifically focusing on the Onliner platform.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [License](#license)

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/avervovka/Onliner_Test_Task.git
   cd Onliner_Test_Task
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

The project is organized as follows:

```
Onliner_Test_Task/
│
├── pages/
│   ├── Base_Page.py            # Base class for page objects
│   ├── category_page.py        # Page object for category page
│   └── compare_page.py         # Page object for comparison page
│
├── tests/
│   └── test_mobile_comparison.py # Test cases for mobile comparison functionality
│
├── utils/
│   ├── config.py               # Configuration settings
│   └── driver_factory.py        # Web driver factory for Selenium
│
├── conftest.py                 # Pytest configuration and fixtures
└── requirements.txt            # Python package dependencies
```

### Pages

- **base_page.py**: Contains the base functionality for all page objects.
- **category_page.py**: Implements methods and attributes specific to the category page.
- **compare_page.py**: Implements methods and attributes specific to the comparison page.

### Tests

- **test_mobile_comparison.py**: Contains test cases for the mobile comparison features of the Onliner platform.

### Utilities

- **config.py**: Holds configuration parameters such as URLs and timeouts.
- **driver_factory.py**: Manages the creation and configuration of Selenium WebDriver instances.

### Configuration

- **conftest.py**: Provides shared fixtures and configurations for the test suite.

## Usage

To run the tests, use the following command:

```bash
pytest -v
```

You can specify additional options such as selecting a specific test file or running tests in parallel.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
