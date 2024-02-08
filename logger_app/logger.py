import logging


def configure_logger(loglevel):
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {loglevel}")

    # Clear all existing handlers before app starts.
    for handler in logging.root.handlers[:]:
        handler.close()
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=numeric_level,
        filename="application.log",
        format='[%(asctime)s][%(levelname)s]%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')


def app(loglevel="info"):
    configure_logger(loglevel=loglevel)

    # Writing all log level messages
    logging.debug("Debug message")
    logging.info("Info message")
    logging.warning("Warning message")
    logging.error("Error message")
    logging.critical("Critical message")


if __name__ == "__main__":
    app()
