from utilities import *
import string
import random

### Capitalize Method Tests ###
def test_capitalize_normal():
    test_text = "filibuster"
    assert capitalize(test_text) == "Filibuster"

def test_capitalize_composed():
    test_text = "jean-marc"
    assert capitalize(test_text) == "Jean-Marc"

def test_capitalize_none():
    test_text = None
    assert capitalize(test_text) == None

### Check Email Method Tests ###
def test_email_valid():
    test_email = "me.too@gmail.com"
    assert is_legit_email(test_email) == True

def test_email_nonetype():
    test_email = None
    assert is_legit_email(test_email) == False

def test_email_2_ats():
    test_email = "me@too@gmail.com"
    assert is_legit_email(test_email) == False

def test_email_whitespace():
    test_email = "me too@gmail.com"
    assert is_legit_email(test_email) == False

def test_email_short_local():
    test_email = "@gmail.com"
    assert is_legit_email(test_email) == False

def test_email_long_local():
    letters = string.ascii_lowercase
    random_local = ''.join(random.choice(letters) for i in range(65))
    test_email = f"{random_local}.too@gmail.com"
    assert is_legit_email(test_email) == False

def test_email_domain_no_dot():
    test_email = "metoo@gmailcom"
    assert is_legit_email(test_email) == False

def test_email_long_domain():
    letters = string.ascii_lowercase
    random_domain = ''.join(random.choice(letters) for i in range(255))
    test_email = f"me.too@{random_domain}.com"
    assert is_legit_email(test_email) == False

### Lowercase Method Tests ###
def test_lowercase_text():
    test_text = "MASTERING"
    assert lower(test_text) == "mastering"

def test_lowercase_none():
    test_text = None
    assert lower(test_text) == None

### Whitespace Method Tests ###
def test_clean_whitespaces():
    test_text = "   eloquent   "
    assert clean_white_spaces(test_text) == "eloquent"

def test_clean_whitespaces_none():
    test_text = None
    assert clean_white_spaces(test_text) == None