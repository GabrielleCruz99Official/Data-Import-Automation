import segment.analytics as analytics
from utilities import *
from uuid import uuid4 as generate_id
import json
import logging
import os
#import sqs_utilities as sqs

""" LOGGING """
if len(logging.getLogger().handlers) > 0:
    logging.getLogger().setLevel(debug_level())
else:
    logging.basicConfig(level=logging.DEBUG)
logging.getLogger('segment').setLevel('DEBUG')

def on_error(error, items):
    print("Error occurred:", error)

def initialize_write_key():
    analytics.write_key = os.getenv('SEGMENT_WRITE_KEY')
    analytics.debug = True
    analytics.on_error = on_error
    analytics.send = True
    #analytics.Client(MY_WRITE_KEY, debug=True, on_error=on_error, send=True, 
    #                 max_queue_size=100000, upload_interval=5, upload_size=100, gzip=True)

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

    return is_legit_email(elem.get('body').get('email'))

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

def call_segment(batch_list, EVENT=None):
    for user in batch_list:
        try:
            identify_user(user)
        except:
            logging.error(f"Failed\n{user}")
            # pass event 
            raise
            

def build_user_identity(data):
    return {
        "userId": f"{data.get('id')}",
        "body": {
            "email": f"{lower(data.get('email'))}",
            "name": f"{capitalize(data.get('firstName'))} {capitalize(data.get('lastName'))}",
        }
    }

def identify_user(user, timeout=0.1):
    """Adds a user to the Segment environment

    This method allows Segment to reference and identify the current user,
    and record traits or properties on them.
    """
    #try:
    #response=
    analytics.identify(user.get('userId'), user.get('body'))
    #response.raise_for_status()
    print("User added!")
    #except analytics.AnalyticsError as error_response:
        #handle_api_exception(user, error_response, timeout)


### API EXCEPTION HANDLER ###
### WILL DOUBLE-CHECK PACKAGE
### FOR AnalyticsError behavoir
def handle_api_exception(batch, error, timeout):
    """Handle error responses from Segment"""
    if has_to_be_retried(error.status) and timeout < 60:
        new_timeout = timeout * 2
        identify_user(batch, new_timeout)
    else:
        print(f"Exception while calling Segment: {error}\n")
        raise error

def has_to_be_retried(response_status):
    """Check if request must be retried"""
    return response_status == 429 or response_status == 500