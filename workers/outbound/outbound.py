from utilities import *
from segment_handler import segment_handler
import logging
#import sqs_utilis as sqs

if len(logging.getLogger().handlers) > 0:
    logging.getLogger().setLevel(debug_level())
else:
    logging.basicConfig(level=logging.DEBUG)

def process_event(event, context):
    """Main method of S3 consumer lambda

    The lambda receives an SQS event containing a record list of imported user data.
    This data is subsequently converted and filtered into a valid list of destination batches.
    The batch list is then sent to the target destination feed while respecting the set rate limit.

    Parameters
    ----------
    event :  AWS trigger event
        the SQS event that triggers the lambda
    context
        the origin of the AWS trigger event - not used in this case
    """

    print(event)
    print(context)

    """here write a code check no message attribute or message attributes to retry counter if it exists then check retry count is less than 5
    THEN call below steps
    Else call DLQ
    """

    event_records = event.get("Records")
    dlq_list = [event for event in event_records if int(event.get(
        'messageAttributes', {}).get('retry_counter', {}).get('stringValue', 0)) > 5]
    event_list = [event for event in event_records if event not in dlq_list]


# Push event records to destination (e.g. Segment)
    if event_list:
        event_records = {'Records': ''}
        event_records['Records'] = event_list
        segment_handler(event_records)

# send event_records that require retries to dlq

    if dlq_list:
        dlq_event_records = {'Records': ''}
        dlq_event_records['Records'] = dlq_list
        #sqs_utilis = sqs.Sqs_utilis(
            #"mparticle", os.getenv('DLQ_SQS_URL'), dlq_event_records)
        #sqs_utilis.hit_sqs()

    # need to edit dlq