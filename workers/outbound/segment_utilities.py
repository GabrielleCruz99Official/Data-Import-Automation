import segment.analytics as analytics
import os
from utilities import *
from uuid import uuid4 as generate_id
import json

analytics.write_key = '07TBfhDd5BjdUYhmTzfgFOmuHy5g68BN'

def on_error(error, items):
    print("Error occurred:", error)

def initialize_write_key():
    write_key = os.getenv('SEGMENT_WRITE_KEY')
    analytics.Client(write_key, debug=True, on_error=on_error, send=True, 
                     max_queue_size=100000, upload_interval=5, upload_size=100, gzip=True)

def is_valid_elem(elem):
    """Checks if the incoming SQS data is a valid Segment identity element.

    Parameters
    ----------
    elem :  Segment Batch
        the Segment Batch to be checked

    Returns
    -------
    Boolean
        True if the email identity in the Batch is valid
    """

    return is_legit_email(elem.get('email'))

def convert_to_segment_elem(elem):
    """Convert SQS Queue JSON into an Segment identity element

    Parameters
    ----------
    elem :  SQS Queue JSON
        a JSON string imported from the SQS Queue

    Returns
    -------
    batch
        an Segment Batch created from the elements of the JSON
    """

    body = json.loads(elem['body'])

    for key in body:
        body[key] = clean_white_spaces(body[key])
    
    return build_user_identity(body)

def call_segment(batch_list):
    for user in batch_list:
        identify_user(user)

def build_user_identity(data):
    print(data)
    return {
        "email": f"{lower(data.get('email'))}",
        "name": f"{capitalize(data.get('firstName'))} {capitalize(data.get('lastName'))}",
    }

def identify_user(user):
    """Adds a user to the Segment environment

    This method allows Segment to reference and identify the current user,
    and record traits or properties on them.
    """
    userId = str(generate_id())
    print(user)
    print(userId)
    analytics.identify(userId, user)