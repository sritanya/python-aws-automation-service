import boto3
import re  # Regular expressions for validating username

# Create an IAM client using the default session (credentials from aws configure)
iam_client = boto3.client('iam')

# Function to validate the IAM user name
def is_valid_username(user_name):
    # Check if there is at least one uppercase letter and no numbers
    if re.search(r'[A-Z]', user_name) and not re.search(r'\d', user_name):
        return True
    return False

# Get the list of current IAM users
response = iam_client.list_users()

# Count the number of IAM users
current_user_count = len(response['Users'])

# Print the current number of users
print(f"Current number of IAM users: {current_user_count}")

# New IAM user name to create
new_user_name = 'Chaitu'  # Change this to test different names

# Check if there are fewer than 5 users
if current_user_count < 5:
    # Validate the user name
    if is_valid_username(new_user_name):
        # Create a new IAM user if the name is valid
        try:
            create_response = iam_client.create_user(UserName=new_user_name)
            print(f"Created user: {create_response['User']['UserName']}")
        except Exception as e:
            print(f"Failed to create user: {e}")
    else:
        # Invalid user name, print fail message
        print("Fail: Username must contain at least one capital letter and must not contain numbers.")
else:
    # Do not create the user if there are already 5 or more users
    print("Fail: Cannot create new user. There are already 5 or more IAM users.")

