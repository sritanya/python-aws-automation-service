import boto3

iam_client = boto3.client('iam')

def list_iam_users():
    response = iam_client.list_users()
    return [user['UserName'] for user in response['Users']]

def set_iam_password(user_name):
    password = input(f"Enter the password for IAM user {user_name}: ")
    iam_client.create_login_profile(
        UserName=user_name, 
        Password=password, 
        PasswordResetRequired=False
    )
    print(f"The password has been set for IAM user: {user_name}")

def create_iam_access_key(user_name):
    access_key = iam_client.create_access_key(UserName=user_name)['AccessKey']
    print(f"Access Key ID: {access_key['AccessKeyId']}")
    print(f"Secret Access Key: {access_key['SecretAccessKey']}")

def attach_policy_to_user(user_name, policy):
    iam_client.attach_user_policy(
        UserName=user_name,
        PolicyArn=policy
    )
    print(f"Policy {policy} has been attached to user {user_name}.")

def update_user_policy(user_name, new_policy):
    attach_policy_to_user(user_name, new_policy)

def create_iam_user():
    users = list_iam_users()

    if len(users) >= 5:
        print("The IAM users have reached their limit.")
        return

    print("The IAM Users list:", *users, sep="\n")
    
    new_user_name = input("Enter the new IAM username: ")
    iam_client.create_user(UserName=new_user_name)
    print(f"Created user: {new_user_name}")
    
    if input("Set a password for IAM console access? (yes/no): ").lower() == 'yes':
       set_iam_password(new_user_name)

    if input("Create access keys for IAM access? (yes/no): ").lower() == 'yes':
       create_iam_access_key(new_user_name)

    policy_arn = input("Enter the ARN of the policy to attach to the new user: ")
    attach_policy_to_user(new_user_name, policy_arn)

    if input("Update the user policy? (yes/no): ").lower() == 'yes':
        new_policy_arn = input("Enter the new ARN of the policy to attach: ")
        update_user_policy(new_user_name, new_policy_arn)

create_iam_user()
