import boto3
import os
import tempfile
import urllib
import csv
from utilities import debug_level, build_dictionary
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
    sqs = boto3.client('sqs')

    event = next(iter(event['Records']))

    bucket = event['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['s3']['object']['key'])
    path = os.path.dirname(key)

    temp_file = tempfile.mktemp()
    s3.download_file(bucket, key, temp_file)

    try:
        with open(temp_file, encoding='utf-8-sig', newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            sqs_message_entries = []
            for line in reader:
                sqs_entry = build_dictionary(line)
                if sqs_entry != {}:
                    sqs_message_entries.append(sqs_entry)
                if len(sqs_message_entries) == 10:
                    sqs.send_message_batch(
                    QueueUrl=os.getenv('SQS_URL'),
                    Entries=sqs_message_entries
                    )    
                    logging.info("CSV Entries Batch sent to SQS queue")
                    sqs_message_entries = []
            if(len(sqs_message_entries) > 0):
                sqs.send_message_batch(
                QueueUrl=os.getenv('SQS_URL'),
                Entries=sqs_message_entries
                )    
                logging.info("All CSV Entries sent to SQS queue")
    except FileNotFoundError:
        logging.error("File not found!")
