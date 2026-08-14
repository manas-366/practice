Feature: Flipkart login page
    Scenario: launching flipkart website
        Given i launched flipkart website
        When i enter Admin and admin123 and click on login
        Then i verify user is successfully logged in or not
