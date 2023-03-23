import segment.analytics as analytics
import os
from uuid import uuid4 as generate_userid

def on_error(error, items):
    print("Error occurred:", error)

def login_client():
    write_key = os.getenv('SEGMENT_WRITE_KEY')
    analytics.Client(write_key, debug=True, on_error=on_error, send=True, 
                     max_queue_size=100000, upload_interval=5, upload_size=100, gzip=True)

def build_user_identity(data):
    return {
        'email': data.get('email'),
        'firstName': data.get('firstName'),
        'lastName': data.get('lastName')
    }

def identify_user(user):
    """Adds a user to the Segment environment

    This method allows Segment to reference and identify the current user,
    and record traits or properties on them.
    """
    new_userID = generate_userid()
    analytics.identify(new_userID, user)