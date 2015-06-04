Feature: Simple list interaction

    Scenario: Visitor notices 'to-do' site
        # Edith has heard about a cool new online to-do app. 
        # She goes to # check out its homepage and notices 'to-do' 
        # in the page title.
        Given a user
        When user visits the site
        Then the page title and header contins 'To-Do'
        AND user is invited to enter an item

    Scenario: Visitor can enter new to-do
        # She is invited to enter a to-do item straight away
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        Given a user
        When user visits the site
        And user enters 'Buy peacock feathers'
        Then user is taken to a new URL
        And '1. Buy peacock feathers' is in to-do list

    Scenario: Visitor can enter two to-dos
        Given a user
        And user has entered 'Buy peacock feathers'
        When user enters 'Use peacock feathers to make a fly'
        Then '1. Buy peacock feathers' is in to-do list
        And '2. Use peacock feathers to make a fly' is in to-do list


    Scenario: Second visitor does not see first user's items
        Given a user
        And user has entered 'Buy peacock feathers'
        And a new user
        When user visits the site
        Then 'Buy peacock feathers' is not in to-do list


    Scenario: Second visiter gets different url
        Given a user
        And user has entered 'Buy peacock feathers'
        And a new user
        When user visits the site
        And user enters 'Buy Milk'
        Then user is taken to a new URL
        And 'Buy Milk' is in to-do list
        And 'Buy peacock feathers' is not in to-do list


# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep
