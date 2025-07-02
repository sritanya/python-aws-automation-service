import boto3

iam_client = boto3.client('iam')

def list_iam_users():
    response = iam_client.list_users()
    return [user['UserName'] for user in response['Users']]
    #return response
    
def set_iam_password(user_name):
    password = input(f"Enter the password for IAM user {user_name}: ")
    iam_client.create_login_profile(
    UserName=user_name, 
    Password=password, 
    PasswordResetRequired=False
    )
    print(f"The Password setting for IAM user: {user_name}")

def create_iam_access_key(user_name):
    access_key = iam_client.create_access_key(UserName=user_name)['AccessKey']
    print(f"Access Key ID: {access_key['AccessKeyId']}")
    print(f"Secret Access Key: {access_key['SecretAccessKey']}")

def create_iam_user():
    users = list_iam_users()

    if len(users) >= 5:
        print("The IAM users reach it's limit of users .")
        return

    print("The IAM Users list:", *users, sep="\n")
    
    new_user_name = input("Enter the new IAM username: ")
    iam_client.create_user(UserName=new_user_name)
    print(f"Created user: {new_user_name}")
    
    if input("Set a password for IAM console access? (yes/no): ").lower() == 'yes':
       set_iam_password(new_user_name)

    if input("Create access keys for IAM access? (yes/no): ").lower() == 'yes':
       create_iam_access_key(new_user_name)


create_iam_user()