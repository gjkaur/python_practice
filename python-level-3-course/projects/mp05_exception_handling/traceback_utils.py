"""
MP05: Traceback Analysis Utilities

PCPP Objective: 1.9

Functions for analyzing exception tracebacks.
"""

import traceback
from typing import Dict, Any


def analyze_exception(exc: Exception) -> Dict[str, Any]:
    """Analyze exception and extract traceback information.
    
    Args:
        exc: Exception object
        
    Returns:
        Dictionary with traceback information
    """
    # TODO: Implement traceback analysis
    # Extract: exception type, message, formatted traceback
    # Access __traceback__, __cause__, __context__
    pass


def log_exception(exc: Exception, filename: str = "error.log") -> None:
    """Log exception with full traceback to file.
    
    Args:
        exc: Exception object
        filename: Log file path
    """
    # TODO: Implement logging with traceback.format_exception()
    pass
