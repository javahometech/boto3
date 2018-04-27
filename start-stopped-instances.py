# Start Stopped Instances

import boto3

ec2 = boto3.resource('ec2')

# Return type is ec2.Instance

instances = ec2.instances.filter(Filters=[
    {
        "Name": "instance-state-name",
        "Values": ['stopped']
    }
])

for instance in instances:
    instance.start()


