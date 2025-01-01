from loguru import logger

# Basic logging
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")

# Configure output file with rotation
logger.add("loguru_logging_{time}.log", rotation="500 MB")

# Exception tracking
@logger.catch
def dangerous_function():
    raise ValueError("Something went wrong!")

# Structured logging
logger.info("User {user} logged in from {ip}", user="john", ip="192.168.1.1")

# Context manager
with logger.catch():
    dangerous_function()