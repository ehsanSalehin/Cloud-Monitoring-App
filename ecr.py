import boto3

region = 'ca-central-1'
access_key_id = 'it's a secret :)'
secret_access_key = 'it's a secret :)'

ecr_client = boto3.client('ecr',region_name=region, aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key,)

repository_name = "my-cloud-app"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)

