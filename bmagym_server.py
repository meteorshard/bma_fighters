#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import json

from classes.bmadb import BMAdb
from classes.bmamember import BMAMember

bmagym_server = Flask(__name__)

@bmagym_server.route('/api/member', methods=['GET'])
def search():
    member_to_search = BMAMember()
    member_to_search.deserialize(**request.args)
    db_search = BMAdb()
    result_members = db_search.search_member(member_to_search)
    result_list = []
    for each_member in result_members:
        result_list.append(each_member.serialize())

    return json.dumps(result_list)

def main():
    bmagym_server.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
