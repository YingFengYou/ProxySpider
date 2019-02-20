# encoding=utf-8

import logging
import sys
import time

import selenium.webdriver.support.ui as ui
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf8')
logger = logging.getLogger(__name__)
logging.getLogger("selenium").setLevel(logging.WARNING)  # 将selenium的日志级别设成WARNING，太烦人
account = '985837207'
password = 'huhang19930710'


def getcookies():
    """ 获取一个账号的Cookie """
    try:
        browser = webdriver.PhantomJS()
        browser.get("https://qzone.qq.com/")
        browser.switch_to_frame('login_frame')
        wait = ui.WebDriverWait(browser, 10)
        wait.until(lambda browser: browser.find_element_by_id('switcher_plogin'))
        plogin = browser.find_element_by_id('switcher_plogin')
        plogin.click()
        wait.until(lambda browser: browser.find_element_by_id('u'))
        u = browser.find_element_by_id('u')
        u.send_keys('%s' % (account))
        p = browser.find_element_by_id('p')
        p.send_keys('%s' % (password))
        wait.until(lambda browser: browser.find_element_by_xpath('//*[@id="login_button"]'))
        login = browser.find_element_by_xpath('//*[@id="login_button"]')
        time.sleep(2)
        login.click()
        time.sleep(1)
        try:
            browser.switch_to_frame('vcode')
            print 'Failed!----------------reason:该QQ首次登录Web空间，需要输入验证码！'
        except Exception:
            pass
        try:
            err = browser.find_element_by_id('err_m')
            time.sleep(2)
            d = err.text
            print account, d
            if u'您输入的帐号或密码不正确' in d:
                print 'Failed!----------------reason:账号或者密码错误！'
            if u'网络繁忙' in d:
                time.sleep(2)
        except Exception, e:
            cookie = {}
            for ck in browser.get_cookies():
                cookie[ck['name']] = ck['value']
            browser.quit()
            print "Get the cookie of QQ:%s successfully!(共%d个键值对)" % (account, len(cookie))
            print cookie
            return cookie
    except Exception as e:
        print e
    except KeyboardInterrupt, e:
        raise e


getcookies()
