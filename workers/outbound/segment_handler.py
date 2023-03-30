from utilities import *
from segment import analytics as analytics
from segment_utilities import *
import logging
import json

""" LOGGING """
if len(logging.getLogger().handlers) > 0:
    logging.getLogger().setLevel(debug_level())
else:
    logging.basicConfig(level=logging.DEBUG)
logging.getLogger('segment').setLevel('DEBUG')

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
        try:
            identify_user(user)
        except:
            logging.error(f"Failed\n{user}")

def segment_handler(event):
    segment_data_list = list(map(convert_to_segment_elem, event['Records']))
    batched_payload = list(filter(is_valid_elem, segment_data_list))

    batch_list = []
    while len(batched_payload) > 0 and len(batched_payload) >= 100:
        batch_list, batched_payload = batched_payload[:100], batched_payload[100:]

        call_segment(batch_list)
        logging.info("Partial data sent to Segment.")

    # added the message attributes
    call_segment(batched_payload)
    logging.info("All data sent to Segment!")
    analytics.client.flush()



