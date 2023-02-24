from utilities import *

import string
import random
import json

test_dict = {}

def test_valid_email_key():
    test_dict['Email Address'] = 'email'
    assert find_email(test_dict) == 'email'

def test_valid_first_name_key():
    letters = string.ascii_lowercase
    random_first = ''.join(random.choice(letters) for i in range(8))
    test_dict['First Name'] = random_first
    assert find_first_name(test_dict) == random_first

def test_valid_last_name_key():
    letters = string.ascii_lowercase
    random_last = ''.join(random.choice(letters) for i in range(8))
    test_dict['Last Name'] = random_last
    assert find_last_name(test_dict) == random_last