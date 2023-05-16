#导入要使用到的模块(工具)
import datetime
import sys
import time

import pyautogui
import win32com.client
from selenium import webdriver
from selenium.webdriver.common.by import By

speaker = win32com.client.Dispatch("SAPI.SpVoice")
print('轩轩技术终端有限公司')
print(' © 2010-2023')

a = (input("请输入Ebay的账号 例：mark757125@21cn.com :"))
b = (input("请输入Ebay的密码 例：thanks757125@% :"))
c = (input("商品的网址 例：https://www.ebay.com/itm/12585727173 :"))
d = (input("商品的价格 例：10 :"))
e = (input("商品的抢购时间 例：2023-04-10 19:56:00 :"))
g = '757125'
h = True

while True:
    f = (input("请输入轩轩授权的秘钥 :"))
    if f == g:
        print('开始运行')
        break
    else:
        if h:
            print('秘钥错误，请重新输入，还剩1次机会')
            h = False
        else:
            print('秘钥错误，运行结束')
            sys.exit()
            break

# 打开浏览器
browser = webdriver.Chrome()
# 进入京东网页
browser.get("https://www.ebay.com/")
time.sleep(2)
pyautogui.click(1460,35)
# 登录
browser.find_element(By.LINK_TEXT,"登录").click()
time.sleep(60)
browser.find_element(By.ID, 'userid').send_keys(a)
time.sleep(2)
browser.find_element(By.ID,"signin-continue-btn").click()
time.sleep(2)
browser.find_element(By.ID, 'pass').send_keys(b)
time.sleep(2)
browser.find_element(By.ID,"sgnBt").click()
time.sleep(2)
# 打开页面
browser.get(c)
time.sleep(2)
#点击出价
browser.find_element(By.ID,"bidBtn_btn").click()
time.sleep(10)
# 出价
browser.find_element(By.ID,"s0-0-1-1-3-placebid-section-offer-section-price-10-textbox").send_keys(d)
time.sleep(2)
while True:
    #获取电脑现在的时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # 对比时间，时间到的话就点击结算
    print(now)
    #判断是不是到了秒杀时间?
    if now >= e:
        # 点击结算按钮
        while 1==1:
            try:
                if browser.find_element(By.CLASS_NAME, "place-bid-actions__submit"):
                    print("here")
                    browser.find_element(By.CLASS_NAME, "place-bid-actions__submit").click()
                    time.sleep(0.000001)
                    print(f"主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单")
                    break
            except:
                pass
                # 点击提交订单按钮
                print(f"主人,我已帮你抢到商品啦,您来支付吧")

