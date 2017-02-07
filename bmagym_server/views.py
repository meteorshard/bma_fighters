#!usr/bin/python
# -*- coding: utf-8 -*-

from . import bmagym_server

import json
from flask import request

from classes.bmadb import BMAdb
from classes.bmamember import BMAMember

@bmagym_server.route('/api/member/search', methods=['GET'])
def search():
    """ 查找会员API
    返回json格式数据

    """

    member_to_search = BMAMember()
    member_to_search.deserialize(**request.args)
    db_search = BMAdb()
    result_members = db_search.search_member(member_to_search)
    result_list = []
    for each_member in result_members:
        result_list.append(each_member.serialize())

    return json.dumps(result_list)

@bmagym_server.route('/api/member/', methods=['POST'])
def member():
    """ 插入/更新会员数据
    只接受POST过来的json数据
    如果u_id已存在就更新
    如果不存在就新建一条
    """

    content = request.get_json()

    if content:
        db_member = BMAdb()

        content_list = []

        if isinstance(content, dict):
            content_list.append(content)
        elif isinstance(content, list):
            content_list = content
        else:
            return 'post failed: unknown data type'

        for each_dict in content_list:
            each_member = BMAMember()
            each_member.deserialize(**each_dict)

            each_member_search = BMAMember(u_id=each_member.u_id)
            search_result = db_member.search_member(each_member_search)

            if search_result: 
                print('Updating')
                db_member.update_member(search_result[0].u_id, each_member)
            else:
                print('Inserting')
                db_member.insert_member(each_member)
        
        return 'success'
    else:
        return 'post failed: not json data'


