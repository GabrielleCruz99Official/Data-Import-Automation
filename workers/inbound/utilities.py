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