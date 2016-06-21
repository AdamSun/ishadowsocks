# -*- coding: utf-8 -*-

'''
    翻墙网站www.ishadowsocks.com定时获取密码
    created by Adam Sun
'''

import urllib2, re, time, json, os

def update():
    myUrl = "http://www.ishadowsocks.com/"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    
    #encode的作用是将unicode编码转换成其他编码的字符串
    #decode的作用是将其他编码的字符串转换成unicode编码
    unicodePage = urllib2.urlopen(req).read().decode("utf-8")

    #re.S是任意匹配模式，也就是.可以匹配换行符
    a_psw = re.findall('<h4>A.*?(\d+)</h4>', unicodePage)
    b_psw = re.findall('<h4>B.*?(\d+)</h4>', unicodePage)
    #c_psw = re.findall('<h4>C.*?(\d+)</h4>', unicodePage)
    
    with open('F:\\Downloads\\software\\Shadowsocks-2.5.8\\gui-config.json', 'r') as fr:
        config = json.loads(fr.read())
        config['configs'][0]['password'] = a_psw[0]
        config['configs'][1]['password'] = b_psw[0]
        #config['configs'][1]['password'] = c_psw[0]
    with open('F:\\Downloads\\software\\Shadowsocks-2.5.8\\gui-config.json', 'w') as fw:
        json.dump(config, fw)

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
	update()
	os.popen("@TASKKILL /F /IM Shadowsocks.exe")
	os.popen('F:\\Downloads\\software\\Shadowsocks-2.5.8\\Shadowsocks.exe')

	while True:
		if datetime.datetime.now().hour % 6 == 0: # 6:00 12:00 18:00 0:00
			if datetime.datetime.now().minute < 5:
				update()
				os.popen("@TASKKILL /F /IM Shadowsocks.exe") # kill process
				os.popen('F:\\Downloads\\software\\Shadowsocks-2.5.8\\Shadowsocks.exe')
		time.sleep(180) # 3 minutes
