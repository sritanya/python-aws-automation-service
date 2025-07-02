import boto3

iam_client = boto3.client('iam')

def list_access_key():
    response = iam_client.list_access_keys()
    #print(response)
    for key in response.get('AccessKeyMetadata', []):
        access_key_id = key.get('AccessKeyId')
        print(f"Access Key : {access_key_id}")


list_access_key()