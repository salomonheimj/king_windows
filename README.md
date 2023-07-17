# Windows App Test Automation

This repository contains Python test scripts for automating Windows application testing using the Appium library with Python bindings. The tests are designed to interact with a Windows application called "LevelEditor" version 1.0.0.

## Prerequisites

Before running the tests, ensure you have the following software installed:

1. Python 3: Make sure you have Python 3 installed on your system. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Selenium: The tests utilize the Selenium WebDriver library to interact with the Windows application. Install Selenium using the following pip command:

```bash
pip install selenium==3.5.0
```

3. Appium Python Client: Appium Python Client is required to automate the Windows application using Appium. Install it using the following pip command:

```bash
pip install Appium-Python-Client==0.24
```

4. WinAppDriver: WinAppDriver is required to automate Windows desktop applications. Download and install the latest version from the official repository: [https://github.com/microsoft/WinAppDriver/releases](https://github.com/microsoft/WinAppDriver/releases)

## Running the Tests

1. Clone this repository to your local machine:

```bash
git clone https://github.com/<your-username>/windows-app-test-automation.git
```

2. Change the directory to the cloned repository:

```bash
cd windows-app-test-automation
```

3. Launch the Windows App (LevelEditor):

Make sure the "LevelEditor" application (version 1.0.0) is installed on your system. You can launch the application manually before running the tests.

4. Execute the test suite:

To run the test suite, use the following command:

```bash
python -m unittest discover -v
```

This command will discover all test cases in the `WindowsAppTests` class and execute them. The test results will be displayed in the console, indicating whether each test passed or failed.

## Description

The test suite contains the following test cases:

1. **test_01_click_new_level**: This test case verifies the functionality of creating a new level in the application. It clicks the "New level" button, enters a title for the level, and selects a background from the combo box.

2. **test_02_open_level**: This test case verifies the ability to open and modify an existing level. It opens "Level3" from the "Levels" folder, modifies the title and background, and saves the changes.

3. **test_03_open_all_tests**: This test case iteratively opens different levels from the "Levels" folder and verifies their existence.
