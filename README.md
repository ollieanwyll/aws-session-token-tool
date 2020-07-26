# AWS-Session-Token-Tool

A python script that takes an MFA token code, retrieves a new session login from AWS and updates the credentials file.

## Requirements

* Boto3 - `pip install boto3`

* The AWS profile you wish to replace must be on the last lines of your `.aws/credentials` file.

* AWS Credentials file must be located at `~/.aws/credentials`

* In the Custom Variables section of `aws-mfa.py` assign your MFA device's serial number ARN to `UserSerialNumber`.

## Usage

```
python aws-mfa.py
```