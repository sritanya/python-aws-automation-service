import boto3
import datetime
from datetime import datetime, timezone, timedelta


iam_client = boto3.client('iam')

def list_iam_users():
    response = iam_client.list_users()
    # print(response['Users'])
    for user in response['Users']:
        user_name = user['UserName']
        user_created_date = user['CreateDate']
        current_time = datetime.now(timezone.utc)
    
    # Calculate the time difference
        time_difference = current_time - user_created_date
        print(time_difference)
list_iam_users()