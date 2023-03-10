import os

def debug_level():
    level = os.getenv('FUNCTION_DEBUG_LEVEL')
    if(level == 'DEBUG'): return 10
    elif(level == 'INFO'): return 20
    elif(level == 'WARNING'): return 30
    elif(level == 'ERROR'): return 40
    elif(level == 'CRITICAL'): return 50
    else: return 10