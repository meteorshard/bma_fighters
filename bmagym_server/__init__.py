#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

bmagym_server = Flask(__name__)

from . import views
