import boto3

region = 'ca-central-1'
access_key_id = 'AKIA5FTZC4U4CWLI4NCG'
secret_access_key = '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'

ecr_client = boto3.client('ecr',region_name=region, aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key,)

repository_name = "my-cloud-app"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)

