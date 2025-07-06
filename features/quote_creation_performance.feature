Feature: Quote Creation - Non-Functional Requirements
              As a system administrator
              I want to ensure the quote system meets performance requirements
              So that users have a reliable and fast experience

        Background:
            Given I am authenticated as a sales user
              And performance monitoring is enabled

        @performance @load
        Scenario: Create quote with 10000000 items within acceptable time - Sustained load test
            Given a customer exists with name "Load Test Customer"
             When I create quotes with item "Notebook" quantity 10000000 and price 20.00 over 60 seconds
             Then the 95th percentile response time should be less than 500ms
              And the 99th percentile response time should be less than 1000ms

        @performance @concurrent
        Scenario: Create multiple quotes simultaneously
            Given 10 customers exist for concurrent testing
             When 10 users create quotes simultaneously
             Then all requests should complete successfully
              And all quote IDs should be unique

        @security @sql-injection
        Scenario: Prevent SQL injection in item names
            Given a customer exists with name "Security Test Customer"
             When I create a quote with item name "'; DROP TABLE quotes; --"
             Then the response status code should be 201
              And the item name should be properly escaped in the response

        @performance @spike
        Scenario: Spike load handling
            Given a customer exists with name "Spike Test Customer"
             When I suddenly send 10000000 concurrent requests within 1 minute
             Then at least 95% of requests should succeed
              And the service should recover within 10 seconds

        @performance @memory
        Scenario: Memory leak detection
            Given a customer exists with name "Memory Test Customer"
              And I record initial memory usage
             When I send 90000000 sequential requests
             Then memory usage should not increase by more than 20%
              And there should be no memory leak indicators

        @performance @large-payload
        Scenario: Large payload performance
            Given a customer exists with name "Large Payload Customer"
             When I create a quote with 100 items each having long descriptions
             Then the response time should be less than 2000ms

        @performance @connection-pool
        Scenario: Connection pool exhaustion test
            Given the system has a connection pool
             When I open 200 concurrent connections and hold them for 30 seconds
             Then new requests should either queue or fail gracefully
              And the service should not crash