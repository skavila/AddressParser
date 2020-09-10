import os
import logging
import yaml
import pkg_resources
import traceback


def logger(name):
    if name is None:
        log = logging.getLogger(__file__)
    else:
        log = logging.getLogger(name)

    default_level = 'INFO'

    log_config_path = '/resources/logging.yaml'
    try:
        if os.path.exists(log_config_path):
            with open(log_config_path, 'rt') as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
    except Exception:
        traceback.print_exc()
    finally:
        return log
