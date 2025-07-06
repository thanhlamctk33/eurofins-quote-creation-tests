Feature: Quote Creation - Negative Cases
              As a system
              I want to validate quote inputs and reject invalid data
              So that data integrity is maintained

        Background:
            Given I am authenticated as a sales user

        Scenario: Attempt to create quote without customer
            Given I do not have a customer
             When I attempt to create a quote without customer ID
             Then the response status code should be 400
              And the error message should be "Customer is required"

        Scenario: Create quote with negative quantity
            Given a customer exists with name "Test Customer"
             When I attempt to create a quote with item "Notebook" quantity -2 and price 100.00
             Then the response status code should be 400
              And the error message should contain "Quantity must be greater than 0"

        Scenario: Create quote with negative price
            Given a customer exists with name "Test Customer"
             When I attempt to create a quote with item "Notebook" quantity 2 and price -100.00
             Then the response status code should be 400
              And the error message should contain "Price must be positive"

        Scenario: Create quote with negative discount
            Given a customer exists with name "Test Customer"
             When I attempt to create a quote with item "Notebook" quantity 1 price 100.00 and discount -0.50
             Then the response status code should be 400
              And the error message should contain "Discount must be positive"