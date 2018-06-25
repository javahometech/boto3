import boto3

client = boto3.client('ec2')
snsClient = boto3.client('sns')

def lambda_handler(event, context):
    
    instanceId = event['detail']['instance-id']
    resp = client.describe_tags(Filters=[
                    {
                        'Name': 'resource-id',
                        'Values': [
                            instanceId
                        ]
                    }
            ])
    
    for tag in resp['Tags']:
        if tag['Key'] == 'Env' and tag['Value'] == 'Prod':
            print('This is production Server')
            snsClient.publish(
                TopicArn='arn:aws:sns:ap-south-1:353848682332:6pmweekday',
                Message='Instance in Prod with Id {}, stopped'.format(instanceId),
                Subject='Prod Alert!!!!'
            )
            break
