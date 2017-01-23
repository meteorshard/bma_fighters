#!usr/bin/python
# -*- coding: utf-8 -*-

import datetime

class BMAMember(object):
    def __init__(self):
        self.user_id = 0
        self.name = ''
        self.wechat_id = ''
        self.sex = ''
        self.tel = ''
        self.paper_type = ''
        self.paper_number = ''
        self.email = ''
        self.birthday = datetime.date(1900, 1, 1)
        self.duration_left = 0
        self.count_left = 0
        self.comment = ''

