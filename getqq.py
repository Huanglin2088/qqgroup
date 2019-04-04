#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 入口文件
import requests
import json
import time
import re
import sys
import urllib
sys.path.append(".")
import insert

payload = {
    'gc': '607799851',
    'st': '0',
    'end':'20',
    'referer':'https://yundong.qq.com/rank/group/share?_wv=2172899&groupid=826232261&from=appstore_icon',
    'bkn': '287287169'
}
# params={
#     params:
# }

global_headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36','charset':'utf-8'}
cookies = {
    "eas_sid":"61H5k5i0K9Z9J623D7Q1t2k2w9", 
    "pgv_info":"ssid=s6161374738",
    "pgv_pvid":"8084592656", 
    "vfwebqq":"e98242f534ac9b545d003ba2709b4f330b7169b403dd8b62373da3baaafe4409170d9051ef2efb92", 
    "pgv_pvi":"9651279872", 
    "pgv_si":"s6999255040", 
    "RK":"6K5Zosm4d5",
    "ptcz":"868fffc2b1542bcef0b9154ff86cd7869dd2a56005197b66adf7937ccfe0f7c0", 
    "bodong_imet":"1551077374702.5986",
    "pgg_uid":"20012005",
    "pgg_appid":"101503919", 
    "pgg_openid":"73CAE1B3B8F1A8ABF11D15835A777CBA", 
    "pgg_access_token":"BD697E6C6C1CF3E81CC0AC10E170752C", 
    "pgg_type":"1", 
    "pgg_user_type":"5", 
    "ptisp":"ctc", 
    "tvfe_boss_uuid":"2d1e62400c9e797b", 
    "o_cookie":"609359462",
    "enc_uin":"5nBZ8DB40w4Nx4fqaVfXOw",
    "OUTFOX_SEARCH_USER_ID_NCOO":"597356646.2781067", 
    "traceid":"31db807774",
    "uin":"o2137314521", 
    "p_uin":"o2137314521", 
    "_qpsvr_localtk":"1554279407526", 
    "ptui_loginuin":"2137314521", 
    "skey":"@U1ot462va",
    "pt4_token":"Pv71CDLhbULSTpRnhmk3rpOe20uG1SfteFrGGJwi8o0_",
    "p_skey":"QWfqwMtdHHeDyn4CG1M3nGCR4pueV90oa6TkbW-03Nw_",
}

def getpage():
    # res = requests.post('https://qun.qq.com/cgi-bin/qun_mgr/search_group_members',data=payload,cookies=cookies,headers=global_headers)
    # content = res.json()
    # print(content)
    # search_count = content['search_count']
    search_count = 1823
    start = 0
    end = 20
    page = search_count/20
    page = page-1
    for i in range(page):
        start = i*21
        end = start+20
        print(start,end)
        getnumber(start,end)
        time.sleep(100)
    return '123'

def getnumber(start,end):
    print(start,end)
    payload = {
        'gc': '607799851',
        'st': start,
        'end':end,
        'referer':'https://qun.qq.com/member.html',
        'bkn': '287287169'
    }
    res = requests.post('https://qun.qq.com/cgi-bin/qun_mgr/search_group_members',data=payload,cookies=cookies,headers=global_headers)
    content = res.json()
    qq={}
    mems = content['mems']
    print(mems)
    for i in range(len(mems)):
        qq['qqnumber'] = mems[i]['uin']
        qq['name'] = mems[i]['nick']
        try:
            insert.mysqlInsert('qqnumber',qq)
        except:
            print(qq)
    print(content['search_count'])

if __name__ == '__main__':
    getpage()



