# Automation Guide for Notes Application

## Introduction
This document explains the automation testing approach for the Notes Application. 
The main objective of automation is to reduce manual effort for repetitive test cases and ensure quick feedback during regression cycles.

## Tools & Framework
- **Language**: Python
- **Automation Tool**: Selenium WebDriver
- **Test Framework**: Pytest
- **Browser**: Chrome
- **Other Dependencies**: ChromeDriver, virtualenv

## Setup Instructions
1. Install Python 3.10+
2. Create a virtual environment:
    python -m venv venv
    venv\Scripts\activate     
3. Install dependencies:
    pip install selenium pytest
4. Download the correct ChromeDriver version that matches your Chrome browser from: https://chromedriver.chromium.org/downloads
