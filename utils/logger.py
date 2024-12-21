import logging
import os

def get_logger(name, log_file="pipeline.log"):
    """Creates a logger for the project."""
    os.makedirs("logs", exist_ok=True)  # Ensure logs directory exists
    log_path = os.path.join("logs", log_file)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    # Stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
