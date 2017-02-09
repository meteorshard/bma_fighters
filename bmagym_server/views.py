#!usr/bin/python
# -*- coding: utf-8 -*-

from . import bmagym_server

import json
from flask import request, Response, jsonify
import requests
import qrcode
import datetime
import hashlib

from classes.bmadb import BMAdb
from classes.bmamember import BMAMember

@bmagym_server.route('/api/member/login', methods=['GET'])
def login():
    """ 用户登录
    从客户端发过来微信code
    拿code去微信服务器解密取得open_id
    微信解密api：
        https://api.weixin.qq.com/sns/jscode2session?
            appid=APPID&
            secret=SECRET&
            js_code=JSCODE&
            grant_type=authorization_code

    取得open_id后到本地数据库查询是否存在
    如果存在则取完整信息并返回
    如果不存在则插入一条只有open_id和u_id的记录并返回
    返回数据中不包括open_id

    error code:
        0: 从微信服务器换取open_id失败
        1：微信服务器返回结果不是dict（一般不出现）
        2：传入的参数里面没有code
    
    传入参数：
        code

    returns:
        如果获取成功，返回不带openid的用户信息
        如果获取失败，返回错误
    """

    if request.args['code']:
        app_id = 'wx602359e41eb3beb1'
        secret = 'a47a48dd45ee9ee07cd8cd7cbdf7ef60'

        s = requests.session()
        decrypt_url = (
            'https://api.weixin.qq.com/sns/jscode2session?'
                'appid=%s&' 
                'secret=%s&'
                'js_code=%s&'
                'grant_type=authorization_code'
        ) % (app_id, secret, request.args['code'])
        result = s.get(decrypt_url)

        resultdict = json.loads(result.content)
        if isinstance(resultdict, dict):
            if resultdict.has_key('openid'):
                member_login = BMAMember(wechat_id=resultdict['openid'])
                db_login = BMAdb()

                search_result = db_login.search_member(member_login)
                if search_result == []:
                    db_login.insert_member(member_login) 
                elif search_result:
                    member_login = search_result[0]
                    member_login.wechat_id = ''

                return json.dumps(member_login.serialize())
            else:
                return json.dumps({'error': 0})
        return json.dumps({'error': 1})
    return json.dumps({'error': 2})

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
                # print('Updating')
                db_member.update_member(search_result[0].u_id, each_member)
            else:
                # print('Inserting')
                db_member.insert_member(each_member)
        
        return 'success'
    else:
        return 'post failed: not json data'

@bmagym_server.route('/api/qrcode/checkin/', methods=['GET'])
def get_qrcode():
    """ 生成与时间和用户ID相关的二维码
    """

    extra_string = 'bMafIGhtErreAdYtOfIghT'
    datetime_string = datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M') 

    # 把时间和特定字符串组合生成MD5并转换成字符串
    string_fingerprint = hashlib.md5(datetime_string + extra_string).hexdigest()
    qr_string = ('https://boluogedou.com/api/qrcode/scan?u_id=%s&fp=%s' %
        (request.args['u_id'], string_fingerprint))
    # qr_image = qrcode.make(string_convert)
    qr_image = qrcode.make(qr_string)

    image_file_location = 'tmp/qrcode.jpg'
    qr_image.save(image_file_location)
    image = file(image_file_location)

    resp = Response(image, mimetype="image/jpeg")
    return resp

