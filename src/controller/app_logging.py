import os
import logging
import logging.config
import yaml
import pkg_resources
import traceback


def logger(name):
    if name is None:
        log = logging.getLogger(__file__)
    else:
        log = logging.getLogger(name)

    default_level = 'DEBUG'
    abs_path = os.path.abspath(__file__ + "/../../")
    log_config_path = os.path.join(abs_path, 'resources/logging.yaml')
    print('>>> log_config_path : ' + log_config_path)

    try:
        if os.path.exists(log_config_path):
            print('>>> os.path.exists...')
            with open(log_config_path, 'rt') as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level,
                                format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s',
                                handlers=[logging.StreamHandler()])
    except Exception:
        print('exception : ' + traceback.print_exc())
        traceback.print_exc()
    finally:
        return log
