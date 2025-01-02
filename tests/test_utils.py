import os
import logging
from src.utils import configure_logging

def test_configure_logging():
    """Test the configure_logging function."""
    log_file = "test.log"

    # Configure logging
    configure_logging(log_file)

    # Write a log message
    logging.info("This is a test log message.")

    # Check if the log file is created
    assert os.path.exists(log_file)

    # Clean up
    os.remove(log_file)
