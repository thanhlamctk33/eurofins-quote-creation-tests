Feature: Quote Creation - Happy Cases
              As a sales representative
              I want to create quotes with various configurations
  So that I can provide accurate pricing to customers

        Background:
            Given I am authenticated as a sales user
              And a customer exists with name "Test Customer"

        Scenario: Create quote with single item
            Given one item "Desktop" with price 1000.00
             When I create a quote for that customer with that item with quantity 2 and price 1000.00
             Then the quote total should be 2000.00

        Scenario: Create quote with single item and discount
            Given one item with name "Product"
             When I create a quote for that customer with that item with quantity 3, price 500.00, and discount 150.00
             Then the quote total should be 1350.00

        Scenario: Create quote with two items
            Given two items
                  | name     | quantity | price |
                  | Mouse    | 5        | 25.00 |
                  | Keyboard | 3        | 75.00 |
             When I create a quote for that customer with these items
             Then the quote total should be 350.00

        Scenario: Create quote with multiple items and mixed discounts
            Given the following items with absolute discounts
                  | name       | quantity | price   | discount |
                  | Desktop PC | 1        | 1500.00 | 150.00   |
                  | Scanner    | 2        | 250.00  | 100.00   |
             When I create a quote with all items
             Then the quote total should be 1750.00

        Scenario: Create quote with percentage discount
            Given one item "Desktop PC" with price 800.00
             When I create a quote with quantity 2 and discount 15.0%
             Then the quote total should be 1360.00

        Scenario: Create quotes with various quantities and prices
            Given the following items
                  | name     | quantity | price |
                  | Notebook | 10       | 15.00 |
                  | Keyboard | 100      | 2.50  |
             When I create a quote with all items
             Then the quote total should be 400.00

        Scenario: Create quotes with various discounts
            Given the following items with absolute discounts
                  | name     | quantity | price | discount |
                  | Notebook | 10       | 15.00 | 10.00    |
                  | Keyboard | 100      | 2.50  | 25.00    |
             When I create a quote with all items
             Then the quote total should be 365.00

        Scenario: Create quote with large quantity
            Given one item "Notebook" with price 20.00
             When I create a quote for that customer with that item with quantity 500 and price 20.00
             Then the quote total should be 10000.00

        Scenario: Create quote with decimal quantities and prices
            Given one item "Notebook" with price 3.99
             When I create a quote for that customer with that item with quantity 25 and price 3.99
             Then the quote total should be 99.75

        Scenario: Create quote with multiple items and mixed discounts - variation 1
            Given the following items with absolute discounts
                  | name     | quantity | price  | discount |
                  | Notebook | 2        | 100.00 | 10.00    |
                  | Keyboard | 2        | 50.00  | 0.00     |
                  | Scanner  | 1        | 200.00 | 15.00    |
             When I create a quote with all items
             Then the quote total should be 475.00

        Scenario: Create quote with decimal quantities and prices - variation 2
            Given the following items with absolute discounts
                  | name     | quantity | price  | discount |
                  | Notebook | 2        | 100.00 | 10.00    |
                  | Keyboard | 2        | 99.99  | 2.00     |
                  | Scanner  | 1        | 200.00 | 15.00    |
             When I create a quote with all items
             Then the quote total should be 572.98

        Scenario: Handle various decimal precision in calculations
            Given the following items with absolute discounts
                  | name     | quantity | price | discount |
                  | Notebook | 10.01    | 33.33 | 20.03    |
                  | Keyboard | 99.99    | 14.28 | 599.99   |
             When I create a quote with all items
             Then the quote total should be 1141.22