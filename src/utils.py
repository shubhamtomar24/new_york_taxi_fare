import logging

def configure_logging(log_file: str, level=logging.INFO):
    """
    Configure logging for the application.
    
    Parameters:
        log_file (str): Path to the log file.
        level (int): Logging level (e.g., logging.INFO).
    """
    logging.basicConfig(
        filename=log_file,
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Logging configuration completed.")
