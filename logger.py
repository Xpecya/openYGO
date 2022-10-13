import logging


def init(config_data):
    log_config = config_data["log"]
    level_string = log_config["level"]
    level = logging.getLevelName(level_string)
    logging.basicConfig(
        level=level,
        format=log_config["format"],
        datefmt=log_config["dateFormat"]
    )


def get_logger(name):
    return logging.getLogger(name)
