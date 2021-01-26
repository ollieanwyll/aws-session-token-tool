import boto3
from botocore.exceptions import ClientError
import os
from os.path import expanduser

# CUSTOM VARIABLES
credentialsFile = expanduser("~") + '/.aws/credentials'
UserSerialNumber = 'REPLACE ME'
# ---------

# User input and validation
UserTokenCode = input("Enter AWS Token Code: ")
try:
   val = int(UserTokenCode)
except ValueError:
   print('Invaild token characters.')
   exit()

if len(UserTokenCode) != 6:
    print('Invaild token length.')
    exit()

# Open credentials file
try:
    file = open(credentialsFile)
    lines = file.read().splitlines()
    file.close()
except IOError:
    print('Failed to read credentials file.')
    exit()

# Get AWS session token
client = boto3.client('sts')
try:
    response = client.get_session_token(
        DurationSeconds=43200,
        SerialNumber=UserSerialNumber,
        TokenCode=UserTokenCode
    )
    print('AWS Session token retrived..')
except ClientError:
    print('Unable to authenticate with AWS.')
    exit()

AccessKeyId = response['Credentials']['AccessKeyId']
SecretAccessKey = response['Credentials']['SecretAccessKey']
SessionToken = response['Credentials']['SessionToken']

# Cut and extend credentials
lines = lines[:-3]
lines.extend((
    'aws_access_key_id = ' + AccessKeyId,
    'aws_secret_access_key = ' + SecretAccessKey,
    'aws_session_token = ' + SessionToken
))

# Create backup and write new credentials file
os.popen('cp credentials credentials.bak') 
fileWrite = open(credentialsFile, 'w')
for line in lines:
  fileWrite.write(line + '\n')
fileWrite.close()

print('SUCCESS - AWS Credentials file overwritten.')
