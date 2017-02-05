#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import json

from classes.bmadb import BMAdb
from classes.bmamember import BMAMember

bmagym_server = Flask(__name__)

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
    print('json is: %s' % content)

    if content:
        db_member = BMAdb()

        print(repr(content))

        for each_dict in content:
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

def main():
    bmagym_server.run(host='127.0.0.1')

if __name__ == '__main__':
    main()
