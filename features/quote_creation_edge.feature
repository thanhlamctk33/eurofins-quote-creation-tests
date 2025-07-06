Feature: Quote Creation - Edge and Boundary Cases
              As a system
              I want to handle edge cases and boundary values correctly
              So that the system behaves predictably at limits

        Background:
            Given I am authenticated as a sales user
              And a customer exists with name "Test Customer"

  # Edge Cases
        Scenario: Create quote with invalid discount
            Given one item "Notebook" with price 100.00
             When I attempt to create a quote with quantity 1 price 100.00 and discount 150.00
             Then the response status code should be 400
              And the error message should contain "Discount cannot exceed item total"

        Scenario: Create quote with zero discount
            Given one item "Notebook" with price 120.00
             When I create a quote for that customer with that item with quantity 1, price 120.00, and discount 0.00
             Then the quote total should be 120.00

        Scenario: Create quote with 100% discount on multiple items
            Given the following items
                  | name     | quantity | price  | discount |
                  | Notebook | 1        | 120.00 | 0.00     |
                  | 产品测试     | 1        | 200.00 | 0.00     |
             When I create a quote with all items
             Then the quote total should be 320.00

        Scenario: Create quote with special characters
            Given one item "Café français" with price 120.00
             When I create a quote with quantity 1 and discount 100.0%
             Then the quote total should be 0.00

  # Boundary Cases
        Scenario: Create quote with minimum valid values
            Given one item "Notebook" with price 0.01
             When I create a quote for that customer with that item with quantity 1 and price 0.01
             Then the quote total should be 0.01

        Scenario: Create quote with maximum valid values
            Given one item "Notebook" with price 999999.99
             When I create a quote for that customer with that item with quantity 999999 and price 999999.99
             Then the quote total should be 999998990000.01

        Scenario: Create quote with maximum quantity and minimum price
            Given one item "Notebook" with price 0.01
             When I create a quote for that customer with that item with quantity 999999 and price 0.01
             Then the quote total should be 9999.99

        Scenario: Create quote with maximum price and minimum quantity
            Given one item "Notebook" with price 999999.99
             When I create a quote for that customer with that item with quantity 1 and price 999999.99
             Then the quote total should be 999999.99

        Scenario: Create quote with 99.99% discount
            Given one item "Notebook" with price 10.00
             When I create a quote with quantity 100 and discount 99.99%
             Then the quote total should be 0.10