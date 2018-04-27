# List EBS volumes of EC2 with Tag Key=Backup and Value = Yes
import boto3

ec2 = boto3.resource('ec2')

# Return type is ec2.Instance

instances = ec2.instances.filter(Filters=[
    {
        "Name": "tag:Backup",
        "Values": ['Yes']
    }
])
volumeIds = []
for instance in instances:
    # Get Attached Volumes, returns list(ec2.Volume)
    volumes = instance.volumes.all()
    for volume in volumes:
        print(volume.volume_id)
        volumeIds.append(volume.volume_id)
        # volume.create_snapshot()

client = boto3.client('sns')

client.publish(
    TopicArn='arn:aws:sns:ap-south-1:999999999999:javahome-weekend-7AM',
    Message=str(volumeIds),
    Subject='EBS Volumes backup alert'
)