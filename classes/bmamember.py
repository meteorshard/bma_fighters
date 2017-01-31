#!usr/bin/python
# -*- coding: utf-8 -*-

import datetime

class BMAMember(object):
    def __init__(self,
            name='',
            wechat_id='',
            sex=0
            ):
        self.u_id = 0
        self.name = name 
        self.wechat_id = wechat_id 
        self.sex = sex
        self.tel = 0
        self.paper_type = ''
        self.paper_number = ''
        self.email = ''
        self.birthday = datetime.date(1900, 1, 1)
        self.duration_left = 0
        self.count_left = 0
        self.comment = ''

    def serialize(self):
        """ 序列化Member类
        输出为字典

        Returns:
            把类属性输出为字典，只包括有效属性
        """
        serialized_dict = {}

        for k, v in self.__dict__.iteritems():
            # print('Key: %s, Value: %s' %(k, v))

            if (v != '' and
                v != 0 and
                v != datetime.date(1900, 1, 1)):
                serialized_dict[k] = v

            # print(repr(serialized_dict))
        return serialized_dict
