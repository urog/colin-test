#!/usr/bin/env python
# -*- coding: utf-8 -*-


def add(x, y):
    return x + y

def get_config():
    # config variable is a dict that is loaded into the cloud_functions file at runtime
    return config

def get_config_keys():
    return config.keys()

def get_config_values():
    return config.values()

def log_something():
    logger.debug('this is the debug message')
    logger.info('this is the info message')
    logger.error('this is the error message')
    logger.exception('this is the exception message')
    logger.warning('this is the warning message')
    logger.critical('this is the critical message')

def my_new_func():
    return 'this is new'

def my_second_new_func():
    return 'this is my second new func'
