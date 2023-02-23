import boto3
import os
import tempfile
import urllib
import pandas as pd
from utilities import debug_level
import logging

if len(logging.getLogger().handlers) > 0:
    logging.getLogger().setLevel(debug_level())
else:
    logging.basicConfig(level=logging.DEBUG)

def process_event(event, context):
    """Main method of S3 inbound lambda

    The lambda receives a CSV file as a trigger event and reads that file.
    Each line of the file is processed into a JSON string.
    The strings are then sent by batches to the SQS queue.

    Parameters
    ----------
    event :  AWS trigger event
        the SQS event that triggers the lambda
    context
        the origin of the AWS trigger event - not used in this case
    """

    s3 = boto3.client('s3')
    #sqs = boto3.client('sqs')

    event = next(iter(event['Records']))

    bucket = event['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['s3']['object']['key'])
    path = os.path.dirname(key)

    temp_file = tempfile.mktemp()
    s3.download_file(bucket, key, temp_file)

    try:
        pass
    except FileNotFoundError:
        pass
