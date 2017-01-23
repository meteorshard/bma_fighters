#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

bmafs_app = Flask()

@bmafs_app.route('/')
def index():
    return 'This is index page'

def main():
    bmafs_app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
