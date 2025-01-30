import sys
from .tracker import write_requirements

def track_imports():
    """Track imported modules and update requirements.txt."""
    write_requirements()

sys.modules[__name__] = track_imports
