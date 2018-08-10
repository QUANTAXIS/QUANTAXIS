import socket
import  socketserver

import re
from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


import time
import datetime
import os
from QUANTAXIS.QAUtil import (DATABASE)

'''
一种是 keep 长时间的 socket 连接

另一种是 操作完毕后主动关闭 socket 连接， 本服务程序 重新 accept 新的连接
现在使用的是每次发送命令，后断开连接

客户端发送 下面4个命令
start_chrome_driver
shutdown_chrome_driver
fetch_a_stock_data_to_mongodb
shutdown_process


'''

##http://www.xiaomilu.top/archives/106
#🛠todo fix 已到 QA_SU 目录下面

start_up_chrome_driver_error_message = ""

def open_chrome_driver():

    browser = None
    strErrorMsg = ""
    try:

        # todo 🛠 使用绝对路径
        print("chrome_driver 加载路径")
        currentFile  = __file__
        print(currentFile);
        dirName = os.path.dirname(currentFile)
        dirName1 = os.path.dirname(dirName)
        dirName2 = os.path.dirname(dirName1)
        print(dirName2)
        print("chrome_driver 加载路径")


        # chrome_options = Options()
        # prefs = {
        #     'profile.default_content_setting_values': {
        #         'images': 2,  # 禁用图片的加载
        #         # 'javascript': 2  ##禁用js，可能会导致通过js加载的互动数抓取失效
        #     }
        # }
        # chrome_options.add_experimental_option("prefs", prefs)


        if sys.platform == 'darwin':
            browser = webdriver.Chrome(dirName2 + '/QUANTAXIS_WEBDRIVER/macos/chromedriver')
        elif sys.platform == 'win32':
            browser = webdriver.Chrome(dirName2 + '/QUANTAXIS_WEBDRIVER/windows/chromedriver')
        elif sys.platform == 'linux':
            browser = webdriver.Chrome(dirName2 + './QUANTAXIS_WEBDRIVER/linux/chromedriver')
            # todo 🛠  linux 下没有测试， linux 下 非gui环境下，用chrome headless driver
            print("🎃")
            print("🎃./selenium_driver/linux/chromedrive   linux 平台上的的      🤖chromedriver 的路径")
            print("🎃./selenium_driver/windows/chromedrive windows 平台上的的    🤖chromedriver 的路径")
            print("🎃   https://npm.taobao.org/mirrors/chromedriver/            🤖chromedriver下载地址")
            print("🎃")


        # browser.implicitly_wait(60)  # 操作、获取元素时的隐式等待时间
        browser.set_page_load_timeout(60)

    except Exception as ee:
        print(ee)
        #nonlocal start_up_chrome_driver_error_message
        strErrorMsg = ee.__str__()

        #todo fixhere 不能访问全局变量 ？？？？
        start_up_chrome_driver_error_message = strErrorMsg
        browser = None

    return browser


def do_open_web_page(strCode, browser):

    try:
        urls = 'http://data.eastmoney.com/zjlx/{}.html'.format(strCode)

        ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
        ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
        ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()


        browser.set_page_load_timeout(60)  # throw a TimeoutException when thepage load time is more than 15 seconds
        browser.get(urls)
        browser.get_cookies()
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        browser.minimize_window()

        print("😇Ok成功打开网页😇")
        return "😇Ok成功打开网页😇"
    except Exception as ee:
        # nonlocal start_up_chrome_driver_error_message
        strErrorMsg = ee.__str__()
        print(ee)
        return strErrorMsg


#新添加到数据库到记录
new_rec = 0

def praseWebPage(code, browser, connection):
    try:

        #计算时间
        nowTime0 = datetime.datetime.now()

        # result = []
        zjlxtable = browser.find_element_by_id('content_zjlxtable')
        table_elements = zjlxtable.find_element_by_tag_name('table')

        table_header = table_elements.find_elements_by_tag_name('thead')
        # todo 🛠 不知道为何，tbody 标签那不到数据
        table_body = table_elements.find_elements_by_tag_name('tbody')

        # chrome debug copy xpath
        table_body2 = browser.find_elements_by_xpath('//*[@id="dt_1"]/tbody')

        head1_list = []
        head2_list = []

        if isinstance(table_header, list) == True:
            # print(table_header[0])
            # print(table_header[0].text)

            table_header_row = table_header[0].find_elements_by_tag_name('tr')

            #assert (len(table_header_row) == 2)
            if  (len(table_header_row) == 2) == False:
                raise WebDriverException("网页数据错误1")

            table_head_name1 = table_header_row[0].find_elements_by_tag_name('th')
            table_head_name2 = table_header_row[1].find_elements_by_tag_name('th')

            for i in range(len(table_head_name1)):
                head_name = table_head_name1[i].get_attribute("innerHTML")
                head1_list.append(head_name)
                # print(table_head_name1[i].get_attribute("value"))

            for i in range(len(table_head_name2)):
                head_name = table_head_name2[i].get_attribute("innerHTML")
                head2_list.append(head_name)
                # print(table_head_name1[i].get_attribute("value"))
        else:
            # raise NoSuchElementException
            print("error !!!!!!!!")
            raise WebDriverException("网页数据错误8")

        row1_list = []
        if isinstance(table_body2, list) == True:

            table_body_row = table_body2[0].find_elements_by_tag_name('tr')
            print("🖼 成功获取 %d 天的资金流向数据️" % (len(table_body_row)))


            row_length = len(table_body_row)
            for i in range(row_length):
                table_body_cell = table_body_row[i].find_elements_by_tag_name('td')
                #assert (len(table_body_cell) == 13)
                if (len(table_body_cell) == 13) == False:
                    raise WebDriverException("网页数据错误2")

                dict_row = {}
                dict_row['stock_code'] = code

                dict_row['date'] = table_body_cell[0].text
                dict_row['zljll_je_wy'] = table_body_cell[1].text
                dict_row['zljll_jzb_bfb'] = table_body_cell[2].text
                dict_row['cddjll_je_wy'] = table_body_cell[3].text
                dict_row['cddjll_je_jzb'] = table_body_cell[4].text
                dict_row['ddjll_je_wy'] = table_body_cell[5].text
                dict_row['ddjll_je_jzb'] = table_body_cell[6].text
                dict_row['zdjll_je_wy'] = table_body_cell[7].text
                dict_row['zdjll_je_jzb'] = table_body_cell[8].text
                dict_row['xdjll_je_wy'] = table_body_cell[9].text
                dict_row['xdjll_je_jzb'] = table_body_cell[10].text
                dict_row['close_price'] = table_body_cell[11].text
                dict_row['change_price'] = table_body_cell[12].text

                row1_list.append(dict_row)

                # todo 🛠  循环获取网页速度非常慢， 进一步学习 selenium 的操作， 批量一次获取数据
                iPct = round((i / row_length) * 100.0)
                #s1 = "\r读取数据%d%%[%s%s]" % (iPct, "🐢" * iPct, " " * (100 - iPct))
                #sys.stdout.write(s1)
                #sys.stdout.flush()


                #############################################################
                strMsg0 = "state@progress@%f"%iPct
                #print("🦀 网页进度 🦀",strMsg0)
                bytes_content = strMsg0.encode()
                bytes_content = bytes_content.zfill(128)
                #assert (len(bytes_content) == 128)
                if (len(bytes_content) == 128) == False:
                    raise WebDriverException("网页数据错误3")

                # 🛠todo fix 128 个byte 很傻
                connection.sendall(bytes_content)
                #
                #############################################################
                strMsg0 = "state@hearbeat@代码:{}日期:{}".format(code, dict_row['date'])
                bytes_content = strMsg0.encode()
                bytes_content = bytes_content.zfill(128)
                #assert (len(bytes_content) == 128)
                if (len(bytes_content) == 128) == False:
                    raise WebDriverException("网页数据错误4")

                # 🛠todo fix 128 个byte 很傻
                connection.sendall(bytes_content)
                #############################################################

                # v = []
                # v.append() # 日期
                # v.append(table_body_cell[1].text) # 收盘价
                # v.append(table_body_cell[2].text) # 涨跌幅
                # v.append(table_body_cell[3].text) # 主力净流入_净额(万元)
                # v.append(table_body_cell[4].text) # 主力净流入_净占比(%)
                # v.append(table_body_cell[5].text) # 超大单净流入_净额(万元)
                # v.append(table_body_cell[6].text) # 超大单净流入_净占比(%)
                # v.append(table_body_cell[7].text) # 大单净流入_净额(万元)
                # v.append(table_body_cell[8].text) # 大单净流入_净占比(%)
                # v.append(table_body_cell[9].text) # 中单净流入_净额(万元)
                # v.append(table_body_cell[10].text)# 中单净流入_净占比(%)
                # v.append(table_body_cell[11].text)# 小单净流入_净额(万元)
                # v.append(table_body_cell[12].text)# 小单净流入_净占比(%)

            #print('总体耗时间： %f' % t)

        else:
            #raise NoSuchElementException
            #print("error !!!!!!!!")
            raise WebDriverException("网页数据错误23")
            pass

        # assert (len(row1_list) != 0)
        # assert (len(head1_list) != 0)
        # assert (len(head2_list) != 0)

        ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()

        nowTime1 = datetime.datetime.now()

        secondsUsed = (nowTime1 - nowTime0).seconds
        print("❤️❤️🖼 完成网页解析使用了%d秒 ️🖼👍👍"%secondsUsed)


        client = DATABASE
        coll_stock_zjlx = client.eastmoney_stock_zjlx

        print("🥕准备写入mongodb 🎞保存数据库 eastmoney_stock_zjlx")

        global new_rec
        new_rec = 0
        row_length = len(row1_list)
        for i in range(row_length):

            #https://www.jianshu.com/p/53cf61220828
            aRec = row1_list[i]

            # 🛠todo 当天结束后，获取当天的资金流相，当天的资金流向是瞬时间点的
            ret = coll_stock_zjlx.find_one(aRec)
            if ret == None:
                coll_stock_zjlx.insert_one(aRec)
                new_rec = new_rec + 1
                #print("🤑 插入新的记录 ", aRec)
                pass
            else:
                #print("😵 记录已经存在 ", ret)
                pass


            iPct = round((i / row_length) * 100.0)
            #############################################################
            strMsg0 = "state@progress@%f" % iPct
            # print("🦀 网页进度 🦀",strMsg0)
            bytes_content = strMsg0.encode()
            bytes_content = bytes_content.zfill(128)
            #assert (len(bytes_content) == 128)
            # 🛠todo fix 128 个byte 很傻
            connection.sendall(bytes_content)

            # #############################################################
            # strMsg0 = "state@hearbeat@代码:{}日期:{}".format(code, dict_row['date'])
            # bytes_content = strMsg0.encode()
            # bytes_content = bytes_content.zfill(128)
            # assert (len(bytes_content) == 128)
            # # 🛠todo fix 128 个byte 很傻
            # connection.sendall(bytes_content)
            # #############################################################

        print("🖼  🎞写入数据库  🐌 新纪录{}条 💹 ".format(new_rec))

        return ["😇Ok成功解析网页😇",new_rec]

    except WebDriverException  as ee:
        print("❌ read_east_money_page_zjlx_to_sqllite 读取网页数据错误 🤮")

        strErroMsg = ee.__str__()
        #errorMsg0 = "finished@code {} msg{}".format(code, ee.__str__())
        print(strErroMsg)

        # bytes_content = errorMsg0.encode()
        # bytes_content = bytes_content.zfill(512)
        # assert (len(bytes_content) == 512)
        # # 🛠todo fix 固定512 个byte 很傻
        # conn.sendall(bytes_content)

        ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
        ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
        ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()

        return [strErroMsg,new_rec]


#
# def doLoop(strPort):
#
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     # Bind the socket to the port
#     server_address = ('localhost', int(strPort))
#     print('starting up on {} port {}'.format(*server_address))
#     sock.bind(server_address)
#
#     # Listen for incoming connections
#     sock.listen(1)
#     working_browser = None
#
#
#
#     while True:
#         try:
#
#             connection, client_address = sock.accept()
#             print('incoming connection is {}, client_address is {}'.format(connection, client_address))
#             print("process is running， wait accept command ,listen port is ", strPort)
#
#             data = connection.recv(128)
#             print('received {!r}'.format(data))
#             if data:
#                 if len(data) == 128:
#                     cmdString = data.decode('utf-8');
#                     cmdString = cmdString.strip('0')
#                     cmdArry = cmdString.split('@')
#
#                     print('cmd is {}'.format(cmdArry[0]))
#                     if cmdArry[0] == 'start_chrome_driver':
#
#                         print("🕹>>>>>>do start_chrome_driver_begin>>>>>");
#
#                         working_browser = open_chrome_driver()
#                         if working_browser is not None:
#                             #############################################################
#                             strMsg0 = "state@start_chrome_driver_ok"
#                             bytes_content = strMsg0.encode()
#                             bytes_content = bytes_content.zfill(128)
#                             assert (len(bytes_content) == 128)
#                             # 🛠todo fix 128 个byte 很傻
#                             connection.sendall(bytes_content)
#                             #############################################################
#                             print("🕹>>>>>>do start_chrome_driver_ok>>>>>>>✅");
#                         else:
#                             #############################################################
#                             strMsg0 = "state@start_chrome_driver_failed@%s"%start_up_chrome_driver_error_message
#                             bytes_content = strMsg0.encode()
#                             bytes_content = bytes_content.zfill(128)
#                             assert (len(bytes_content) == 128)
#                             # 🛠todo fix 128 个byte 很傻
#                             connection.sendall(bytes_content)
#                             #############################################################
#                             print("🕹>>>>>>do start_chrome_driver_failed>>>>>>>❌");
#
#                         #time.sleep(2)
#
#
#                         continue
#
#                     if cmdArry[0] == 'shutdown_chrome_driver':
#
#                         if working_browser is not None:
#                             working_browser.quit()
#                             #############################################################
#                             strMsg0 = "state@shutdown_chrome_driver_ok"
#                             bytes_content = strMsg0.encode()
#                             bytes_content = bytes_content.zfill(128)
#                             assert (len(bytes_content) == 128)
#                             # 🛠todo fix 128 个byte 很傻
#                             connection.sendall(bytes_content)
#                             #############################################################
#                             print("🕹>>>>>>do shutdown_chrome_driver_ok>>>>>>>✅");
#
#                         else:
#                             print("❌working_browser is None❌")
#                             print("🕹>>>>>>do shutdown_chrome_driver_failed>>>>>>>❌");
#
#                         continue
#
#                     if cmdArry[0] == 'fetch_a_stock_data_to_mongodb':
#
#                         assert(len(cmdArry) == 2)
#                         strCodeToOpenPage = cmdArry[1]
#
#                         retMsg = do_open_web_page(strCodeToOpenPage, working_browser)
#                         if retMsg == "😇Ok成功打开网页😇":
#                             #############################################################
#                             strMsg0 = "state@fetch_a_stock_data_to_mongodb_open_web_page_ok"
#                             bytes_content = strMsg0.encode()
#                             bytes_content = bytes_content.zfill(128)
#                             assert (len(bytes_content) == 128)
#                             # 🛠todo fix 128 个byte 很傻
#                             connection.sendall(bytes_content)
#                             #############################################################
#
#                             print("🕹>>>>>>doing fetch_a_stock_data_to_mongodb>>>>>>>>");
#
#                             retMsg2 = praseWebPage(strCodeToOpenPage, working_browser, connection)
#                             if retMsg2[0] == "😇Ok成功解析网页😇":
#
#                                 #############################################################
#                                 strMsg0 = "state@fetch_a_stock_data_to_mongodb_prase_web_page_ok@{}".format(retMsg2[1])
#                                 bytes_content = strMsg0.encode()
#                                 bytes_content = bytes_content.zfill(128)
#                                 assert (len(bytes_content) == 128)
#                                 # 🛠todo fix 128 个byte 很傻
#                                 connection.sendall(bytes_content)
#                                 #############################################################
#                             else:
#                                 #############################################################
#                                 strMsg0 = "state@fetch_a_stock_data_to_mongodb_prase_web_page_failed@%s"%retMsg2[0]
#                                 bytes_content = strMsg0.encode()
#                                 bytes_content = bytes_content.zfill(128)
#                                 assert (len(bytes_content) == 128)
#                                 # 🛠todo fix 128 个byte 很傻
#                                 connection.sendall(bytes_content)
#                                 #############################################################
#
#                         else:
#                             #############################################################
#                             strMsg0 = "state@fetch_a_stock_data_to_mongodb_open_web_page_failed@%s"%retMsg
#                             bytes_content = strMsg0.encode()
#                             bytes_content = bytes_content.zfill(128)
#                             assert (len(bytes_content) == 128)
#                             # 🛠todo fix 128 个byte 很傻
#                             connection.sendall(bytes_content)
#                             #############################################################
#
#                             print("🕹>>>>>>finish fetch_a_stock_data_to_mongodb>>>>>>>>");
#
#                         continue;
#
#                     if cmdArry[0] == 'shutdown_process':
#                         #############################################################
#                         strMsg0 = "state@shutdown_procceed"
#                         bytes_content = strMsg0.encode()
#                         bytes_content = bytes_content.zfill(128)
#                         assert (len(bytes_content) == 128)
#                         # 🛠todo fix 128 个byte 很傻
#                         connection.sendall(bytes_content)
#                         #############################################################
#                         print("🕹>>>>>>do shutdown_process>>>>>>>");
#                         break
#                 else:
#                     print("continue ❌data length is not 128 , continue recv...❌")
#                     print('continue no data from', client_address)
#                     continue
#
#         except Exception as ee:
#             print(ee)
#             strErroMsgGeneral = ee.__str__()
#             #############################################################
#             strMsg0 = "state@error_general_2@%s" % strErroMsgGeneral
#             bytes_content = strMsg0.encode()
#             bytes_content = bytes_content.zfill(128)
#             assert (len(bytes_content) == 128)
#             # 🛠todo fix 128 个byte 很傻
#             connection.sendall(bytes_content)
#             #############################################################
#
#         finally:
#             pass
#
#     # Clean up the connection
#     connection.close()
#     sock.close()
#     print('connect closed', client_address)
#
#
#
# def doBigLoop(strPort):
#
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     # Bind the socket to the port
#     server_address = ('localhost', int(strPort))
#     print('starting up on {} port {}'.format(*server_address))
#     sock.bind(server_address)
#
#     # Listen for incoming connections
#     sock.listen(1)
#     working_browser = None
#
#
#     # #############################################################
#     # strMsg0 = "state@process_start_ok"
#     # bytes_content = strMsg0.encode()
#     # bytes_content = bytes_content.zfill(128)
#     # assert (len(bytes_content) == 128)
#     # # 🛠todo fix 128 个byte 很傻
#     # connection.sendall(bytes_content)
#     # #############################################################
#     # print("🕹>>>>>>do process startup ok !>>>>>>>✅");
#
#
#     while True:
#         connection, client_address = sock.accept()
#
#         data = connection.recv(128)
#         if data:
#             print('received {!r}'.format(data))
#
#             cmdString = data.decode('utf-8');
#             cmdString = cmdString.strip('0')
#             cmdArry = cmdString.split('@')
#
#             print('cmd is {}'.format(cmdArry[0]))
#             if cmdArry[0] == 'start_chrome_driver':
#
#                 print("🕹>>>>>>do start_chrome_driver_begin>>>>>");
#
#                 working_browser = open_chrome_driver()
#                 if working_browser is not None:
#                     #############################################################
#                     strMsg0 = "state@start_chrome_driver_ok"
#                     bytes_content = strMsg0.encode()
#                     bytes_content = bytes_content.zfill(128)
#                     assert (len(bytes_content) == 128)
#                     # 🛠todo fix 128 个byte 很傻
#                     connection.sendall(bytes_content)
#                     #############################################################
#                     print("🕹>>>>>>do start_chrome_driver_ok>>>>>>>✅");
#                 else:
#                     #############################################################
#                     strMsg0 = "state@start_chrome_driver_failed@%s" % start_up_chrome_driver_error_message
#                     bytes_content = strMsg0.encode()
#                     bytes_content = bytes_content.zfill(128)
#                     assert (len(bytes_content) == 128)
#                     # 🛠todo fix 128 个byte 很傻
#                     connection.sendall(bytes_content)
#                     #############################################################
#                     print("🕹>>>>>>do start_chrome_driver_failed>>>>>>>❌");
#
#                 # time.sleep(2)
#                 continue
#
#
#             if cmdArry[0] == 'shutdown_chrome_driver':
#
#                 if working_browser is not None:
#                     working_browser.quit()
#                     #############################################################
#                     strMsg0 = "state@shutdown_chrome_driver_ok"
#                     bytes_content = strMsg0.encode()
#                     bytes_content = bytes_content.zfill(128)
#                     assert (len(bytes_content) == 128)
#                     # 🛠todo fix 128 个byte 很傻
#                     connection.sendall(bytes_content)
#                     #############################################################
#                     print("🕹>>>>>>do shutdown_chrome_driver_ok>>>>>>>✅");
#                 continue
#
#             if cmdArry[0] == 'shutdown_process':
#                 #############################################################
#                 strMsg0 = "state@shutdown_procceed"
#                 bytes_content = strMsg0.encode()
#                 bytes_content = bytes_content.zfill(128)
#                 assert (len(bytes_content) == 128)
#                 # 🛠todo fix 128 个byte 很傻
#                 connection.sendall(bytes_content)
#                 #############################################################
#                 print("🕹>>>>>>do shutdown_process>>>>>>>");
#                 connection.close()
#                 exit(0)
#                 return
#         pass


# globale

working_browser = None


def unpackParam(data):
    global cmdArry
    cmdString = data.decode('utf-8');
    cmdArry = cmdString.split('@')
    cmdArry[0] = cmdArry[0].strip('0')
    return cmdArry

def send_execute_result(connection, strMsg0):
    bytes_content = strMsg0.encode()
    bytes_content = bytes_content.zfill(128)
    assert (len(bytes_content) == 128)
    # 🛠todo fix 128 个byte 很傻
    connection.sendall(bytes_content)

def do_shutdown_process(data,connection):
    strMsg0 = "state@shutdown_procceed"
    send_execute_result(connection, strMsg0)
    print("🕹>>>>>>finish do shutdown_process>>>>>>>")
    connection.close()

def do_startup_chrome(data, connection):
    global working_browser
    working_browser = open_chrome_driver()
    if working_browser is not None:
        strMsg0 = "state@start_chrome_driver_ok"
        send_execute_result(connection,strMsg0)
        print("🕹>>>>>>do start_chrome_driver_ok>>>>>>>✅");
    else:
        strMsg0 = "state@start_chrome_driver_failed@%s" % start_up_chrome_driver_error_message
        send_execute_result(connection,strMsg0)
        print("🕹>>>>>>do start_chrome_driver_failed>>>>>>>❌");
    pass



def do_shutdown_chrome(data, connection):
    global working_browser
    if working_browser is not None:
        working_browser.quit()
        strMsg0 = "state@shutdown_chrome_driver_ok"
        send_execute_result(connection,strMsg0)
        print("🕹>>>>>>do shutdown_chrome_driver_ok>>>>>>>✅");
    else:
        strMsg0 = "state@shutdown_chrome_driver_failed"
        send_execute_result(connection, strMsg0)
        print("🕹>>>>>>do shutdown_chrome_driver_failed>>>>>>>❌");
    pass



def do_fetch_web_page(data,connection,strcode,):
    global working_browser
    retV = do_open_web_page(strcode, working_browser)
    if retV == "😇Ok成功打开网页😇":
        strMsg0 = "state@fetch_a_stock_data_to_mongodb_open_web_page_ok"
        send_execute_result(connection, strMsg0)
        print("🕹>>>>>>do fetch_a_stock_data_to_mongodb_open_web_page_ok>>>>>>>✅");


        retV2 = praseWebPage(strCode,working_browser,connection)
        if retV2[0] == "😇Ok成功解析网页😇":

            strMsg0 = "state@fetch_a_stock_data_to_mongodb_prase_web_page_ok@{}".format(retV2[1])
            send_execute_result(connection, strMsg0)
            print("🕹>>>>>>do fetch_a_stock_data_to_mongodb_prase_web_page_ok>>>>>>>✅");

        else:
            strMsg0 = "state@fetch_a_stock_data_to_mongodb_prase_web_page_failed@{}".format(retV2[1])
            send_execute_result(connection, strMsg0)
            print("🕹>>>>>>do fetch_a_stock_data_to_mongodb_prase_web_page_failed>>>>>>>✅");

    else:
        strMsg0 = "state@fetch_a_stock_data_to_mongodb_open_web_page_failed@{}".format(retV)
        send_execute_result(connection, strMsg0)
        print("🕹>>>>>>do fetch_a_stock_data_to_mongodb_open_web_page_failed msg:{}>>>>>>>✅".format(retV));
    pass



if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = sys.argv[1]

    # Bind the socket to the port
    server_address = ('localhost', int(port))
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    #accept for the initial connecton
    connection, client_address = sock.accept()

    while True:
        connection, client_address = sock.accept()

        data = connection.recv(128)
        if data:
            print('received {!r}'.format(data))
            cmdArry = unpackParam(data)

            if cmdArry[0] == "start_chrome_driver":
                do_startup_chrome(data, connection)
                continue

            if cmdArry[0] == "shutdown_chrome_driver":
                do_shutdown_chrome(data,connection)
                continue

            if cmdArry[0] == 'fetch_a_stock_data_to_mongodb':
                strCode = cmdArry[1];
                do_fetch_web_page(data,connection,strCode)
                continue

            if cmdArry[0] == 'shutdown_process':
                do_shutdown_process(data,connection)
                break

        else:
            continue


    sock.close()
    print("🕹>>>>>>进程结束了 with port {}>>>>>>>".format(port));