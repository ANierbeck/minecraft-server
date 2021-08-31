import json
import boto3
import time
import sys

region = 'eu-central-1'
ec2_client = boto3.client('ec2', region_name=region)
ec2_resource = boto3.resource('ec2', region_name=region)

def get_handler(event, context):
    #'i-093dfe36af46494b4'
    if event.get('pathParameters') is None or event.get('pathParameters').get('instanceId') is None:
        return get_instances(event, context)
    else:
        instanceId = event.get('pathParameters').get('instanceId')
        instance = ec2_resource.Instance(instanceId)
        print('started your instances: ' + str(instance))
        print('instance state: ' + str(instance.state['Code']))
        return instance.public_ip_address

def post_handler(event, context):
    instances = []
    instanceId = event.get('pathParameters').get('instanceId')
    instances.append(instanceId)
    ec2_client.start_instances(InstanceIds=instances)
    ec2_resource = boto3.resource('ec2', region_name=region)
    instance = ec2_resource.Instance(instanceId)
    print('started your instances: ' + str(instances))
    print('instance state: ' + str(instance.state['Code']))
    return instance.public_ip_address

def delete_handler(event, context):
    instanceId = event.get('pathParameters').get('instanceId')
    instances = []
    instances.append(instanceId)
    ec2_client.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
    return 'stopped'

def get_instances(event, context):
    instances_info = ec2_client.describe_instances()['Reservations'][0]['Instances']
    instances = []
    
    for instance in instances_info: 
        instances.append(instance['InstanceId'])
    
    print('found instances: ' + str(instances))
    return instances


def handler(event, context):
    print('received event:')
    print(event)

    """ reqcontxt = event.get("requestContext")
    httpprtcl = reqcontxt.get("http")
    methodname = httpprtcl.get("method")"""

    methodname = event.get("httpMethod")

    print('### http method name ###' + str(methodname))

    result = ''

    if "GET" == methodname.upper():
        result = get_handler(event, context)
    elif "POST" == methodname.upper():
        result = post_handler(event, context)
    elif "DEL" == methodname.upper():
        result = delete_handler(event, context)
    else:
        print('Default handler, nothing to do')

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(result)
    }

    print (response)
  
    return response