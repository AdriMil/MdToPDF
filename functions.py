import os

def debug()->bool:
    """Get from env var DEBUG if debug must be activated
    """
    debug = os.getenv('DEBUG')
    if debug:
        debug_level=True
        print("------------------Debug Activated ---------------------")
    else:
        debug_level=False
    return debug_level

def fileName()->str:
    """Get value from env var and return a default value if the env var is empty.
    Returns:
        str: value read from env var or default value
    """
    get_file_name = os.getenv('FILE_NAME') # Get values from Env var
    if get_file_name is None or get_file_name=="":
        file_name = "Documentation"
    else:
        file_name=get_file_name
    return file_name
