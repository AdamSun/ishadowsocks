# -*- coding: utf-8 -*-

'''
    翻墙网站www.ishadowsocks.com定时获取密码
    created by Adam Sun
'''

import urllib2
import urllib
import re
import threading
import time
import json
import subprocess

def start():
    myUrl = "http://www.ishadowsocks.com/"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(myUrl, headers = headers)
    myResponse = urllib2.urlopen(req)
    myPage = myResponse.read()
    #encode的作用是将unicode编码转换成其他编码的字符串
    #decode的作用是将其他编码的字符串转换成unicode编码
    unicodePage = myPage.decode("utf-8")

    #re.S是任意匹配模式，也就是.可以匹配换行符
    a_psw = re.findall('<h4>A.*?(\d+)</h4>', unicodePage)
    b_psw = re.findall('<h4>B.*?(\d+)</h4>', unicodePage)
    print u'A服务器新密码:%s' % a_psw[0]
    print u'B服务器新密码:%s' % b_psw[0]
    is_pw_change = False
    if a_psw and b_psw:
        #open the config and convert the config to dict, then change the password
        with open('F:\Downloads\software\Shadowsocks-2.5.8\gui-config.json', 'r') as fr:
            config = json.loads(fr.read())
            print u'A服务器旧密码:' + config['configs'][0]['password']
            print u'B服务器旧密码:' + config['configs'][1]['password']

            #check a server password is changed
            if config['configs'][0]['password'] == a_psw[0]:
                print u'A服务器新旧密码相同，无须修改'
            else:
                is_pw_change = True
                config['configs'][0]['password'] = a_psw[0]

            #check b server password is changed
            if config['configs'][1]['password'] == b_psw[0]:
                print u'B服务器新旧密码相同，无须修改'
            else:
                is_pw_change = True
                config['configs'][1]['password'] = b_psw[0]

        if is_pw_change:
            with open('F:\Downloads\software\Shadowsocks-2.5.8\\gui-config.json', 'w') as fw:
                if config:
                    print u'开始更新密码...'
                    json.dump(config, fw)
                    print u'修改密码成功...'
                else:
                    print u'无法加载配置，无法更新密码'

    #set the timer
    global timer
    timer = threading.Timer(0.5 * 60 * 60, start)
    timer.start()

if __name__ == "__main__":
    #the desc of programming
    print u"""
---------------------------------------
    程序：翻墙网站www.ishadowsocks.com定时半小时获取密码
    版本：1.0
    作者：Adam Sun
    日期：2015-12-31
    语言：Python 2.7.5
---------------------------------------
    """
    #run the Shadowsocks.exe
    print u'打开Shadowsocks.exe...'
    subprocess.Popen('F:\Downloads\software\Shadowsocks-2.5.8\Shadowsocks.exe')
    #start the timer
    timer = threading.Timer(1.0, start)
    timer.start()
raw_input()