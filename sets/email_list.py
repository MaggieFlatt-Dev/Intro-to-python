# 1. Initialize Empty Sets
#Create two empty sets named subscribers and unsubscribers.
subscribers = set()
unsubscribers = set()

# 2. Add Emails to the Sets
# Write a function add_email(email, set_name) that adds an email to the specified set (subscribers or unsubscribers) and prints a message indicating the email was added.
def add_email(email, set_name):

    print(f"Email '{email}' added to {'subscribers' if set_name == subscribers else 'unsubscribers'}.")

# 3. Remove Emails from the Sets
#Write a function remove_email(email, set_name) that removes an email from the specified set if it exists, and prints a message indicating the email was removed or a message if the email was not found.
def remove_email(email, set_name):

# 4. Display Emails in a Set
# Write a function display_emails(set_name) that prints all the emails in the specified set.
def display_emails(set_name):

# 5. Find Active Subscribers
# Write a function find_active_subscribers() that returns a set of emails that are in subscribers but not in unsubscribers.
def find_active_subscribers():
    
# Adding emails to subscribers (notice that some people subscribe more than once)
add_email("user1@example.com", subscribers)
add_email("user3@example.com", subscribers)
add_email("user4@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user6@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user8@example.com", subscribers)
add_email("user9@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user10@example.com", subscribers)
add_email("user12@example.com", subscribers)

# Adding emails to unsubscribers
add_email("user6@example.com", unsubscribers)
add_email("user8@example.com", unsubscribers)
add_email("user1@example.com", unsubscribers)
add_email("user10@example.com", unsubscribers)

# Displaying subscribers and unsubscribers
print("All Subscribers:")
print("All Unsubscribers:")

# Finding active subscribers
print("Active Subscribers:")