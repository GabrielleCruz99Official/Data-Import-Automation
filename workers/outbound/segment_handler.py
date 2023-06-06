from utilities import *
from segment_utilities import *
import logging
#import os

""" LOGGING """
if len(logging.getLogger().handlers) > 0:
    logging.getLogger().setLevel(debug_level())
else:
    logging.basicConfig(level=logging.DEBUG)
logging.getLogger('segment').setLevel('DEBUG')

def segment_handler(event):
    initialize_write_key()
    segment_data_list = list(map(convert_to_segment_elem, event['Records']))
    batched_payload = list(filter(is_valid_elem, segment_data_list))
    batch_list = []
    while len(batched_payload) > 0 and len(batched_payload) >= 100:
        batch_list, batched_payload = batched_payload[:100], batched_payload[100:]

        call_segment(batch_list, event)
        logging.info("Partial data sent to Segment.")
        
    call_segment(batched_payload, event)
    logging.info("All data sent to Segment!")
    analytics.flush()



