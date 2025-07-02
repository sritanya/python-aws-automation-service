import boto3

# Create an IAM client using the default session (credentials from `aws configure`)
iam_client = boto3.client('iam')

# List all IAM users
response = iam_client.list_users()
print("IAM Users:")
def create_users():
    print("IAM Users:")
    for user in response['Users']:
    print(user['UserName'])
    response = iam_client.create_user(UserName='Tanya')
    print(f"Created user: {response['User']['UserName']}")

# Print the names of IAM users

create_users()
update_users()


