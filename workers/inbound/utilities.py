from constants import *
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
