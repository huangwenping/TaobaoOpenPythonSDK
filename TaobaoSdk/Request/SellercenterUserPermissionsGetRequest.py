#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 获取指定用户的权限集合，并不组装成树。如果是主账号，返回所有的权限列表；如果是子账号，返回所有已授权的权限。只能查询属于自己的账号信息 (如果是主账号，则是主账号以及所属子账号，如果是子账号则是对应主账号以及所属子账号)
# @author wuliang@maimiaotech.com
# @date 2013-03-07 19:54:40
# @version: 0.0.0

import os
import sys
import time



def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

__modulePath = os.path.join(__getCurrentPath(), os.path.pardir)
__modulePath = os.path.normpath(__modulePath)
if __modulePath not in sys.path:
    sys.path.insert(0, __modulePath)


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取指定用户的权限集合，并不组装成树。如果是主账号，返回所有的权限列表；如果是子账号，返回所有已授权的权限。只能查询属于自己的账号信息 (如果是主账号，则是主账号以及所属子账号，如果是子账号则是对应主账号以及所属子账号)</SPAN>
# <UL>
# </UL>
class SellercenterUserPermissionsGetRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.sellercenter.user.permissions.get"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">用户标识，次入参必须为子账号比如zhangsan:cool。如果只输入主账号zhangsan，将报错。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.nick = None
