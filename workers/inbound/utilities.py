from constants import *
from uuid import uuid4 as generate_id
import json
import os
import logging

def debug_level():
    level = os.getenv('FUNCTION_DEBUG_LEVEL')
    if(level == 'DEBUG'): return 10
    elif(level == 'INFO'): return 20
    elif(level == 'WARNING'): return 30
    elif(level == 'ERROR'): return 40
    elif(level == 'CRITICAL'): return 50
    else: return 10

if len(logging.getLogger().handlers) > 0:
    logging.getLogger().setLevel(debug_level())
else:
    logging.basicConfig(level=logging.DEBUG)

def find_email(reader_dict):
    keys = set(list(reader_dict.keys()))
    for email in EMAIL_HEADERS:
        if email in keys:
            return reader_dict[email]
    logging.warning("No valid email header found in csv keys.")

def find_first_name(reader_dict):
    keys = set(list(reader_dict.keys()))
    for first_name in FIRST_NAME_HEADERS:
        if first_name in keys:
            return reader_dict[first_name]
    logging.warning("No valid first name header found in csv keys.")

def find_last_name(reader_dict):
    keys = set(list(reader_dict.keys()))
    for last_name in LAST_NAME_HEADERS:
        if last_name in keys:
            return reader_dict[last_name]
    logging.warning("No valid last name header found in csv keys.")

def find_id(reader_dict):
    keys = set(list(reader_dict.keys()))
    for id in ID_HEADERS:
        if id in keys:
            return reader_dict[id]
    logging.warning("No valid id header found in csv keys.")

def build_dictionary(reader_dict):
    """Turns a CSV line dictionary into an SQS entry.
    
    Parameters
    ----------
    reader_dict
        A CSV line converted into a dictionary instance
    
    Returns
    sqs_entry
        A dictionary containing an SQS body with valid entries
    """

    sqs_entry = {}
    sqs_body = {}

    # check if keys exist in file, then find value
    email = find_email(reader_dict)
    first_name = find_first_name(reader_dict)
    last_name = find_last_name(reader_dict)
    id = find_id(reader_dict)

    # add to SQS body if value is not null or blank
    sqs_body["firstName"] = first_name
    sqs_body["lastName"] = last_name
    sqs_body["email"] = email
    sqs_body["id"] = id

    sqs_entry['Id'] = str(generate_id())
    sqs_entry['MessageBody'] = json.dumps(sqs_body)

    return sqs_entry