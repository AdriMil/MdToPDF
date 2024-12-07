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