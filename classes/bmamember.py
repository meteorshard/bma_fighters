#!usr/bin/python
# -*- coding: utf-8 -*-

import datetime

class BMAMember(object):
    def __init__(self,
            u_id=0,
            name='',
            wechat_id='',
            sex=0,
            tel=0,
            paper_type='',
            paper_number='',
            email='',
            comment=''
            ):
        self.u_id = u_id
        self.name = name 
        self.wechat_id = wechat_id 
        self.sex = sex
        self.tel = tel
        self.paper_type = paper_type
        self.paper_number = paper_number
        self.email = email
        self.birthday = datetime.date(1900, 1, 1)
        self.duration_left = 0
        self.count_left = 0
        self.comment = comment

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

    def deserialize(self, **kwargs):
        """ 反序列化Member类
        把输入的数据灌进属性里去

        Args:
            **kwargs: 输入的属性，按照
            字段名=值 或者 **dict
            的方式输入
        """

        for k, v in kwargs.iteritems():
            if self.__dict__.has_key(k):
                # __dict__是只读的所以只能用setattr来给属性赋值
                setattr(self, k, v) 
