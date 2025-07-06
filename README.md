# Quote Creation Test Suite

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Behave](https://img.shields.io/badge/BDD-Behave-green.svg)](https://behave.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Overview

Automated test suite for Quote Creation API using Python Behave BDD framework. This comprehensive test suite ensures the reliability, accuracy, and performance of the quote calculation system.

## ✨ Features Tested

| Feature | Description |
|---------|-------------|
| ✅ **Happy Path** | Create quotes with various configurations |
| 🔍 **Edge Cases** | Boundary values and special characters |
| ❌ **Negative Scenarios** | Invalid inputs validation |
| ⚡ **Performance Tests** | Load, spike, and memory tests |

## 🔧 Requirements

- Python 3.6+
- pip
- Virtual environment (recommended)

## 🚀 Quick Start

### 1. Clone and Setup

# Clone repository
git clone https://github.com/YOUR_USERNAME/eurofins-quote-creation-tests.git
cd eurofins-quote-creation-tests

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt```

### 2. Configure Environment
# Copy environment template
cp .env.example .env

# Edit .env with your API settings
nano .env

Example .env configuration:
API_BASE_URL=http://localhost:8000/api
AUTH_URL=http://localhost:8000/auth
TEST_USER=sales_user
TEST_PASSWORD=password123


### 3. Run Tests
# Run all tests
behave

# Run specific feature
behave features/quote_creation_happy.feature

# Run by tag
behave --tags=@performance
behave --tags=-@performance  # Exclude performance tests

# Run with HTML report
behave -f html -o reports/test-report.html

### 4. Project Structure
eurofins-quote-creation-tests/
├── 📂 features/                    # Feature files (test scenarios)
│   ├── 📄 quote_creation_happy.feature
│   ├── 📄 quote_creation_edge.feature
│   ├── 📄 quote_creation_negative.feature
│   └── 📄 quote_creation_performance.feature
├── 📂 steps/                       # Step definitions
│   ├── 📂 common/                  # Common steps (auth, api)
│   ├── 📂 customers/               # Customer-related steps
│   ├── 📂 item/                    # Item-related steps
│   ├── 📂 quote/                   # Quote-specific steps
│   └── 📂 performance/             # Performance test steps
├── 📂 support/                     # Helper utilities
├── 📂 config/                      # Configuration
├── 📂 reports/                     # Test reports
├── 📄 environment.py               # Behave hooks
├── 📄 behave.ini                   # Behave configuration
├── 📄 requirements.txt             # Python dependencies
└── 📄 README.md                    # This file


