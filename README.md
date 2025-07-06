# Quote Creation Test Suite

## Overview
Automated test suite for Quote Creation API using Python Behave BDD framework.

## Features Tested
- ✅ Happy path scenarios - Create quotes with various configurations
- ✅ Edge cases - Boundary values and special characters
- ✅ Negative scenarios - Invalid inputs validation
- ⚡ Performance tests - Load, spike, and memory tests

## Requirements
- Python 3.6+
- pip

## Quick Start

### 1. Clone and Setup
```bash
# Clone repository
git clone <repository-url>
cd Eurofins

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

Configure Environment

# Copy environment template
cp .env.example .env

# Edit .env with your API settings
# API_BASE_URL=http://localhost:8000/api
# TEST_USER=sales_user
# TEST_PASSWORD=password123

Run Tests
# Run all tests
behave

# Run specific feature
behave features/quote_creation_happy.feature

# Run by tag
behave --tags=@performance
behave --tags=-@performance  # exclude performance tests

# Run with HTML report
behave -f html -o reports/test-report.html

Project Structure

Eurofins/
├── features/               # Feature files (test scenarios)
│   ├── quote_creation_happy.feature
│   ├── quote_creation_edge.feature
│   ├── quote_creation_negative.feature
│   └── quote_creation_performance.feature
├── steps/                  # Step definitions
│   ├── common/            # Common steps (auth, api)
│   ├── customers/         # Customer-related steps
│   ├── item/              # Item-related steps
│   ├── quote/             # Quote-specific steps
│   └── performance/       # Performance test steps
├── support/               # Helper utilities
├── config/                # Configuration
├── reports/               # Test reports
├── environment.py         # Behave hooks
├── behave.ini            # Behave configuration
└── requirements.txt       # Python dependencies

Using Test Runner
# Run with test runner
python3 test_runner.py

# Run specific suite
python3 test_runner.py --suite regression
python3 test_runner.py --suite performance

# Run with options
python3 test_runner.py --tags @security --format json


Test Results Example
Feature: Quote Creation - Happy Cases
  Scenario: Create quote with single item
    Given I am authenticated as a sales user      # 0.002s
    And a customer exists with name "Test"        # 0.015s
    Given one item "Desktop" with price 1000.00   # 0.012s
    When I create a quote...                      # 0.025s
    Then the quote total should be 2000.00        # 0.001s

1 feature passed, 0 failed, 0 skipped
10 scenarios passed, 0 failed, 0 skipped
45 steps passed, 0 failed, 0 skipped, 0 undefined