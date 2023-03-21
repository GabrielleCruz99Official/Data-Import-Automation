import os

def debug_level():
    level = os.getenv('FUNCTION_DEBUG_LEVEL')
    if(level == 'DEBUG'): return 10
    elif(level == 'INFO'): return 20
    elif(level == 'WARNING'): return 30
    elif(level == 'ERROR'): return 40
    elif(level == 'CRITICAL'): return 50
    else: return 10

def capitalize(text, name = True):
    """ This method capitalizes the first letter of the input text.

    This method does not transform the entire string into upper case.
    If the text is hyphenated and the name variable is True,
    the text is considered a composed name. This composed name must have
    the first letter of each part be capitalized.
    e.g. (jean-pol becomes Jean-Pol)
    
    If the text is null or None, the method returns a NoneType instance.

    """

    if text is None:
        return None

    # check hyphen
    if name and '-' in text:
        return text.title()

    return text.capitalize()

def is_legit_email(text):
    """ This method checks if the input email is legitimate.
    
    The method returns True if the input passes all criteria,
    and returns False if it violates one of the criteria
    mentioned below:
    
    - The input email cannot and must not be a NoneType instance.
    - The input email must contain only one "@" character.
    - The input text cannot have whitespaces.
    - The local section of the email can only be between 2 and 64 characters long.
    - The domain section of the email cannot exceed 255 characters.
    - The domain section must contain at least one '.' character.
    """

    # check if NoneType
    if text is None: return False

    # check at sign count
    if (text.count('@') != 1): return False
    # check for whitespaces
    if (text.count(' ') > 0): return False

    # split email to local and domain sections
    local, domain = text.split('@')

    # local section check
    if len(local) < 1 or len(local) > 64: return False

    # domain section check
    if (domain.count('.') < 1): return False
    if len(domain) > 255: return False

    return True

def clean_white_spaces(text):
    """ This method clears the whitespaces from the input text. 
    
    If the text is null or None, the method returns a NoneType instance.
    """

    return None if text is None else text.strip()

