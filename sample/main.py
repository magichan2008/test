# -*- coding: utf-8 -*-
'''
サンプル用モジュール
'''
import os
try:
    from configparser import SafeConfigParser, NoOptionError
except ImportError:
    from ConfigParser import SafeConfigParser, NoOptionError


SESSION_NAME = 'TEST'
conf_file = os.path.join(
    os.getenv("HOME") or os.getenv("USERPROFILE"), "test.ini")


def dummy():
    '''
    サンプル用ダミー関数
    '''
    return 1


def create_conf():
    parser = SafeConfigParser()
    parser.add_section(SESSION_NAME)
    with open(conf_file, "w") as f:
        parser.write(f)


def read_conf():
    parser = SafeConfigParser()
    parser.read(conf_file)
    try:
        addr = parser.get(SESSION_NAME, 'addr')
    except NoOptionError:
        addr = 'localhost'
    try:
        port = parser.get(SESSION_NAME, 'port')
    except NoOptionError:
        port = 8080
    try:
        password = parser.get(SESSION_NAME, 'password')
    except NoOptionError:
        password = None
    return addr, port, password


def write_conf(addr=None, port=None, password=None):
    parser = SafeConfigParser()
    parser.read(conf_file)
    if addr:
        parser.set(SESSION_NAME, 'addr', addr)
    if port:
        parser.set(SESSION_NAME, 'port', port)
    if password:
        parser.set(SESSION_NAME, 'password', password)
    with open(conf_file, "w") as f:
        parser.write(f)


def countup():
    for i in range(10):
        print("COUNT : {}".format(i))


def hello():
    print("hello world")


def add(a, b):
    print("{}".format(a + b))
