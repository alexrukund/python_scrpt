import boto3

def delete_stopped_instances_and_snapshots():
    ec2 = boto3.client('ec2')
    
    # Get all stopped instances
    stopped_instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
    )
    
    instance_ids = []
    for reservation in stopped_instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    if instance_ids:
        print(f"Deleting stopped instances: {instance_ids}")
        ec2.terminate_instances(InstanceIds=instance_ids)
    else:
        print("No stopped instances found.")
    
    # Get all snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])
    
    snapshot_ids = []
    for snapshot in snapshots['Snapshots']:
        if snapshot['Description'].startswith('Created by CreateImage'):
            snapshot_ids.append(snapshot['SnapshotId'])
    
    if snapshot_ids:
        print(f"Deleting snapshots: {snapshot_ids}")
        ec2.delete_snapshots(SnapshotIds=snapshot_ids)
    else:
        print("No snapshots to delete.")

if __name__ == "__main__":
    delete_stopped_instances_and_snapshots()
