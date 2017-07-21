#!/usr/bin/env python
# -*- coding: utf-8 -*-


def subtract(x, y):
    return x - y

def add(x, y):
    return x + y

def get_config():
    # config variable is a dict that is loaded into the cloud_functions file at runtime
    return config

def get_config_keys():
    return config.keys()

def get_config_values():
    return config.values()

def log_something(message):
    logger.debug('{}'.format(message))
    logger.info('{}'.format(message))
    logger.exception('{}'.format(message))
    logger.warning('{}'.format(message))
    logger.critical('{}'.format(message))
