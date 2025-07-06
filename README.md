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

#### Clone repository
```bash
git clone https://github.com/YOUR_USERNAME/eurofins-quote-creation-tests.git
cd eurofins-quote-creation-tests
```

#### Create virtual environment
```bash
python3 -m venv venv
```

#### Activate virtual environment
#### On macOS/Linux:
```bash
source venv/bin/activate
#### On Windows:
```bash
venv\Scripts\activate
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
#### Copy environment template
```bash
cp .env.example .env
```

#### Edit .env with your API settings
```bash
nano .env
```

Example .env configuration:
```bash
API_BASE_URL=http://localhost:8000/api
AUTH_URL=http://localhost:8000/auth
TEST_USER=sales_user
TEST_PASSWORD=password123
```


### 3. Run Tests
#### Run all tests
behave

#### Run specific feature
```bash
behave features/quote_creation_happy.feature
```

#### Run by tag
```bash
behave --tags=@performance
behave --tags=-@performance  # Exclude performance tests
```

#### Run with HTML report
```bash
behave -f html -o reports/test-report.html
```



