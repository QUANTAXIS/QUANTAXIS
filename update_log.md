# QUANTAXIS 升级日志
![QUANTAXIS LOGO](http://i1.piimg.com/1949/62c510db7915837a.png)
<!-- TOC -->

- [QUANTAXIS 升级日志](#quantaxis-升级日志)
    - [新的功能:](#新的功能)
        - [1.1 组合回测支持](#11-组合回测支持)
        - [1.2 多种交易状态支持](#12-多种交易状态支持)
        - [1.3 实盘交易的支持](#13-实盘交易的支持)
        - [1.4 更加方便的数据更新接口](#14-更加方便的数据更新接口)
        - [1.5 手续费/滑点](#15-手续费滑点)
        - [1.6 QUANTAXIS-Log 优化](#16-quantaxis-log-优化)
        - [1.7 重构了回测流程,简化回测设置步骤](#17-重构了回测流程简化回测设置步骤)
        - [1.8 对于QACMD进行改进](#18-对于qacmd进行改进)
        - [1.9 新增QADataStruct模块](#19-新增qadatastruct模块)
        - [1.10 对于backtest的一个bug修改:](#110-对于backtest的一个bug修改)
        - [1.11 对于SU中心的修改](#111-对于su中心的修改)
        - [1.12 增加了界面的logo以及log的logo](#112-增加了界面的logo以及log的logo)
        - [1.13 增加一个标准化的QUANTAXIS事件队列(0.3.9)](#113-增加一个标准化的quantaxis事件队列039)
        - [1.14 增加了两个时间选择的api(0.3.9)](#114-增加了两个时间选择的api039)
        - [1.15 增加了一个事件订阅的方式QA.QA_Event(0.3.9):](#115-增加了一个事件订阅的方式qaqa_event039)
        - [1.16 修改了CLI中的创建example内容(0.3.9):](#116-修改了cli中的创建example内容039)
        - [1.17 增加了一个带参数的延时装饰器](#117-增加了一个带参数的延时装饰器)
        - [1.18 web 部分的改进](#118-web-部分的改进)
        - [1.19 回测部分的最后一天停牌情况的处理](#119-回测部分的最后一天停牌情况的处理)
        - [1.20 新增一个时间接口 QA_util_time_now()](#120-新增一个时间接口-qa_util_time_now)
        - [1.21 新增一个QAWeb的接口](#121-新增一个qaweb的接口)
        - [1.22 新增一个QACSV的接口](#122-新增一个qacsv的接口)
        - [1.23 新增一个交易时间的变量](#123-新增一个交易时间的变量)
        - [1.24 新增一个k线接口(通达信)](#124-新增一个k线接口通达信)
        - [1.25 在回测的时候,增加一个回测内全局变量](#125-在回测的时候增加一个回测内全局变量)
        - [1.26 新增一个创建多维list的函数](#126-新增一个创建多维list的函数)
        - [1.27 修改了一个QABacktest的传参, 现在在策略中,需要指定买卖状态](#127-修改了一个qabacktest的传参-现在在策略中需要指定买卖状态)
        - [1.28 对于backtest的加载的外部函数的接口进行修改](#128-对于backtest的加载的外部函数的接口进行修改)
        - [1.29 修改了QA_Query 里返回的数组格式](#129-修改了qa_query-里返回的数组格式)
        - [1.30 修改了QA_util_save_csv的模式](#130-修改了qa_util_save_csv的模式)
        - [1.31 通达信5分钟线解析保存](#131-通达信5分钟线解析保存)
        - [1.32 获取指数k线的api更新](#132-获取指数k线的api更新)
        - [1.33 QA_util更新 QA_util_time_stamp](#133-qa_util更新-qa_util_time_stamp)
        - [1.34  QABACKTEST回测引擎更新](#134--qabacktest回测引擎更新)
        - [1.35 QA_fetch_stock_list 函数更新](#135-qa_fetch_stock_list-函数更新)
        - [1.36 回测框架新增一个一键平仓函数](#136-回测框架新增一个一键平仓函数)
        - [1.37 回测框架的报价函数增加回调](#137-回测框架的报价函数增加回调)
        - [1.38 更新了save/update的方式](#138-更新了saveupdate的方式)
        - [1.39 QUANTAXIS CLI 增加一个选项 CLEAN](#139-quantaxis-cli-增加一个选项-clean)
        - [1.40 QA_util_diff_list](#140-qa_util_diff_list)
        - [1.41 QUANTAXIS.QABACKTEST.QABACKTEST_STOCKDAY.QA_backtest_get_OHLCV](#141-quantaxisqabacktestqabacktest_stockdayqa_backtest_get_ohlcv)
        - [1.42 QUANTAXIS MARKET ENGINE修改](#142-quantaxis-market-engine修改)
        - [1.43 QA_util_get_real_datelist](#143-qa_util_get_real_datelist)
        - [1.44 QA_fetch_stock_full('date',type)(0.4.0-beta-dev28)](#144-qa_fetch_stock_fulldatetype040-beta-dev28)
        - [1.45 同花顺日线爬虫可用(0.4.0-beta-dev29)](#145-同花顺日线爬虫可用040-beta-dev29)
        - [1.46 数据源更换 QA_fetch_get_stock_day('ts')(0.4.0-beta-dev30,dev31,dev32)](#146-数据源更换-qa_fetch_get_stock_dayts040-beta-dev30dev31dev32)
        - [1.47 新增数据库api QA_util_mongo_initial,QA_util_mongo_make_index(0.4.0-beta-dev33)](#147-新增数据库api-qa_util_mongo_initialqa_util_mongo_make_index040-beta-dev33)
        - [1.48 修复一个委托单超过市场上下限 返回none的bug(0.4.0-beta-dev34)](#148-修复一个委托单超过市场上下限-返回none的bug040-beta-dev34)
        - [1.49 修复了pytdx的get_k_data api(0.4.0-beta-dev35)](#149-修复了pytdx的get_k_data-api040-beta-dev35)
        - [1.50 修复了一个因为市场返回400状态导致账户数据溢出的bug(0.4.0-beta-dev36,37)](#150-修复了一个因为市场返回400状态导致账户数据溢出的bug040-beta-dev3637)
        - [1.51 QA_data_fq_factor获取从1990年以来的前后复权因子,QA_fetch_get_stock_day 兼容性改动(0.4.0-beta-dev38)](#151-qa_data_fq_factor获取从1990年以来的前后复权因子qa_fetch_get_stock_day-兼容性改动040-beta-dev38)
        - [1.52 QATDX改动(0.4.0-b-dev39)](#152-qatdx改动040-b-dev39)
        - [1.53 Darwin平台的quantaxis 生成路径问题(0.4.0-b-dev40)](#153-darwin平台的quantaxis-生成路径问题040-b-dev40)
        - [1.54 支持下载时候 遇到网络问题 断点续传(0.4.0-beta-dev41)](#154-支持下载时候-遇到网络问题-断点续传040-beta-dev41)
        - [1.55 分钟线获取接口(0.4.0-beta-dev42 43)](#155-分钟线获取接口040-beta-dev42-43)
        - [1.56 QA_Util 新增格式转换 (0.4.0-beta-dev44)](#156-qa_util-新增格式转换-040-beta-dev44)
        - [1.57 QA_SU 新增复权因子的保存(0.4.0-beta-dev44)](#157-qa_su-新增复权因子的保存040-beta-dev44)
        - [1.58 优化QA_QAQuery 和QAMarket_engine的代码(0.4.0-beta-dev44,45,46,47)](#158-优化qa_qaquery-和qamarket_engine的代码040-beta-dev44454647)
        - [1.59 QA_fetch_get_stock_transaction('tdx',code,start,end,retry,ip,port)(0.4.0-beta-dev48,49)](#159-qa_fetch_get_stock_transactiontdxcodestartendretryipport040-beta-dev4849)
        - [1.60 新增多个QAUtil的api (0.4.0-beta-dev50)](#160-新增多个qautil的api-040-beta-dev50)
    - [巨大改动/重构](#巨大改动重构)
        - [2.1 QA.QAARP.QAAccount](#21-qaqaarpqaaccount)
        - [2.2 QA.QABacktest.Backtest_analysis](#22-qaqabacktestbacktest_analysis)
        - [2.3 QA.QABacktest.QABacktest](#23-qaqabacktestqabacktest)
        - [2.4 QA.QA_Queue](#24-qaqa_queue)
        - [2.5 彻底放弃QUANTAXIS-WEBKIT-CLIENT](#25-彻底放弃quantaxis-webkit-client)
        - [2.6 更换QABACKTEST的回测模式](#26-更换qabacktest的回测模式)
        - [2.7 数据源更换(0.4.0-beta-dev30)](#27-数据源更换040-beta-dev30)
    - [重要性能优化  重新定义回测流程,减少数据库IO压力](#重要性能优化--重新定义回测流程减少数据库io压力)
    - [废弃的接口](#废弃的接口)
    - [to do list](#to-do-list)

<!-- /TOC -->

作者: yutiansut


## 新的功能:

### 1.1 组合回测支持
2017/6/13
在之前的版本里,quantaxis是通过穿透性测试去做unit测试.然后对于unit结果进行组合.这种构建组合的方式虽然行之有效,但是在一些情境下会比较笨重.

好比如,你只是想对于特定的股票(如小市值股票)的一些方法进行回测分析,由于这些股票组合是固定的,所以本来只需要进行一次回测,但是在穿透性测试下要进行n次回测并重新组合

新的模式在原有基础上推出了基于组合的unit测试,在固定组合的时候,只需要进行一个测试,就可以得到结果


### 1.2 多种交易状态支持
2017/6/14
之前的版本中,quantaxis只支持单次持仓,及(不能进行买入-继续买入的状态)

0.3.9-gamma进行了一定的修改和优化,目前支持了多次连续买入和卖出的交易状态,并通过order_id和trade_id来锁定买卖的对应关系


### 1.3 实盘交易的支持
2017/6/14
通过tradex的接口,quantaxis实现了一套实盘的解决方案,在quantaxistrade文件夹下,具体详见quantaxis_trade


### 1.4 更加方便的数据更新接口
2017/6/15
```python

import QUANTAXIS as QA

QA.QA_SU_update_stock_day(client=QA.QA_Setting.client,engine='ts')
```
### 1.5 手续费/滑点
2017/6/16

重写了交易撮合引擎,区分不同市场/状态,同时对于股票交易量的区分有了更加接近实盘的表现

1. 对于滑点的设置:

    - 如果报价单的购买数量小于1/16当日成交量
    > 按正常报价进行交易

    - 如果报价单的购买数量在1/16-1/8 当日成交量, 成交价会进行一个浮动:
    > 买入价=mean(max{o,c},h)  卖出价=mean(min{o,c},l)

    - 如果报价单的数量在1/8当日成交量以上,则只能成交1/8的当日成交量
    > 买入价=high  卖出价=low 交易数量=1/8当日成交量


2. 对于手续费的设置:

    买入的时候无需付费,卖出的时候,按成交额收万分之五的手续费,并在现金中扣除



### 1.6 QUANTAXIS-Log 优化
2017/6/15

```shell

ipython

In [1]: import QUANTAXIS as QA

QUANTAXIS>> start QUANTAXIS

QUANTAXIS>> ip:127.0.0.1   port:27017

QUANTAXIS>> Welcome to QUANTAXIS, the Version is 0.3.9-beta-dev20
```



### 1.7 重构了回测流程,简化回测设置步骤
2017/6/21

在quantaxis的backtest的基础上,对于回测的流程和模式进行了重构,通过ini的读取以及函数式编程的方法,把回测简化到一个ini+策略即可进行回测的步骤

具体参见 test/new test 文件夹


### 1.8 对于QACMD进行改进
2017/6/26

对于QACMD的模式进行了修改,现在直接在命令行中输入quantaxis即可进入quantaxis的交互式界面进行操作


### 1.9 新增QADataStruct模块
2017/6/27

datastruct将在未来对于不同的场景下的数据进行重构和规范化处理,目前新增了基础数据类,机器学习类,ohlc价格序列类等

### 1.10 对于backtest的一个bug修改:
2017/6/27

修改了购买的时候的方式,其中mean的报价方式改变为当前可用资金/股票列表数量的资金分配方式

修改了对于cash小于买入报单总量的修正,以免出现在不能买入的时候的误操作

### 1.11 对于SU中心的修改

修改并优化了对于QUANTAXIS backtest的回测过程的资金曲线的存储过程,增加了存为csv的方法,并优化和修正了存储时的结果

### 1.12 增加了界面的logo以及log的logo
![Markdown](http://i2.kiimg.com/1949/4123de6743af4810.png)
![Markdown](http://i2.kiimg.com/1949/ce8c3ee69f64976e.png)

### 1.13 增加一个标准化的QUANTAXIS事件队列(0.3.9)
2017/6/30-2017/7/2,2017/7/4

引入方式:
```python
from QUANTAXIS import QA_Queue
```

使用方式:

首先需要引入一个标准化的队列:

``` python
from six.moves import queue
import queue # python3
import Queue # python2 

qa=queue.Queue()# 你可以自定义队列的大小
#启动一个事件队列:
qa_event=QA_Queue(qa)
# 往事件引擎里发事件,需要有函数
"""
标准的事件是:
{'type':'xxx','fn':'func'}
"""
qa.put({'type':'xxx','fn':'func'})
```
事件引擎会默认一直监听这个队列
2017/7/4 update  重新优化了这个事件引擎 参见test/test_job_queue.py
```shell
13:35:45 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:45 QUANTAXIS>>> job--id:0
13:35:46 QUANTAXIS>>> job--id:1
13:35:46 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 2 tasks to do
13:35:46 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 1 tasks to do
13:35:46 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:47 QUANTAXIS>>> job--id:2
13:35:47 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 1 tasks to do
13:35:47 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:47 QUANTAXIS>>> job--id:3
13:35:48 QUANTAXIS>>> job--id:4
13:35:48 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 2 tasks to do
13:35:48 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 1 tasks to do
13:35:48 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:49 QUANTAXIS>>> job--id:5
13:35:49 QUANTAXIS>>> job--id:6
13:35:49 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 2 tasks to do
13:35:49 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 1 tasks to do
13:35:49 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:50 QUANTAXIS>>> job--id:7
13:35:50 QUANTAXIS>>> job--id:8
13:35:50 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 2 tasks to do
13:35:50 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 1 tasks to do
13:35:50 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:51 QUANTAXIS>>> job--id:9
13:35:51 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 1 tasks to do
13:35:51 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:52 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:53 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:54 QUANTAXIS>>> job--id:1
13:35:54 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>: There are still 1 tasks to do
13:35:54 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:55 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:56 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:57 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:58 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:35:59 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:36:00 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...
13:36:01 QUANTAXIS>>> From Engine <QA_Queue(EVENT ENGINE, started 12488)>Engine will waiting for new task ...


```




### 1.14 增加了两个时间选择的api(0.3.9)
2017/7/3

- QUANTAXIS.QAUtil.QADate.QA_select_hours

- QUANTAXIS.QAUtil.QADate.QA_select_min

引入方式

```python
from QUANTAXIS.QAUtil import QA_select_hours,QA_select_min
```

### 1.15 增加了一个事件订阅的方式QA.QA_Event(0.3.9):
2017/7/3
```python

from QUANTAXIS.QATask import QA_Event

class MyEvent(QA_Event):
    ASK = "askMyEvent"
    RESPOND = "respondMyEvent"

class WhoAsk(object):
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.event_dispatcher.add_event_listener(
            MyEvent.RESPOND, self.on_answer_event
        )

    def ask(self):
        print("who are listener to me?")
        self.event_dispatcher.dispatch_event(MyEvent(MyEvent.ASK, self))

    def on_answer_event(self, event):
        print("receive event %s", event.data)

class WhoRespond(object):
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.event_dispatcher.add_event_listener(
            MyEvent.ASK, self.on_ask_event)

    def on_ask_event(self, event):
        self.event_dispatcher.dispatch_event(
            MyEvent(MyEvent.RESPOND, self))

dispatcher = QA_EventDispatcher()
who_ask = WhoAsk(dispatcher)
who_responde1 = WhoRespond(dispatcher)
who_responde2 = WhoRespond(dispatcher)

# WhoAsk ask
who_ask.ask()
```

result:
```shell
who are listener to me?
receive event %s <__main__.WhoRespond object at 0x02361D50>
receive event %s <__main__.WhoRespond object at 0x02361DB0>
```



### 1.16 修改了CLI中的创建example内容(0.3.9):
2017/7/3

现在在命令行中输入QUANTAXIS:
```shell
λ  quantaxis
QUANTAXIS>> start QUANTAXIS
QUANTAXIS>> ip:127.0.0.1   port:27017
QUANTAXIS>> From Engine <_MainThread(MainThread, started 19040)>2017-07-03 14:22:08.218800
QUANTAXIS>> FROM QUANTAXIS SYS== now running 3 threads
QUANTAXIS>> Welcome to QUANTAXIS, the Version is 0.3.9-beta-dev29


QUANTAXIS> examples
QUANTAXIS>> QUANTAXIS example
QUANTAXIS>> successfully generate a example strategy inC:\Users\yutiansut\strategy\A05-CCI
QUANTAXIS> exit

λ  ls


    目录: C:\Users\yutiansut\strategy\A05-CCI


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---          2017/7/3     14:22        358 backtest.ini
-a---          2017/7/3     14:22        905 backtest.py
-a---          2017/7/3     14:22       2738 quantaxis-2017-07-03-14-22-08-.log

```
### 1.17 增加了一个带参数的延时装饰器
2017/7/4

QUANTAXIS.QAUtil.QADate.QA_util_time_delay()

使用方式

```python
from QUANTAXIS import QA_util_time_dalay


@QA_util_time_dalay(2)
#延时2秒
def pp():
    print(1)


```


### 1.18 web 部分的改进
2017/7/10

web部分,修改了页面布局和回测的显示方式

去除了之前单个股票和行情的对比

改成了资金曲线和组合分析的方式


### 1.19 回测部分的最后一天停牌情况的处理
2017/7/10


```python
_remains_day=0
while __message['header']['status']==500:
    #停牌状态,这个时候按停牌的最后一天计算价值(假设平仓)
    
    __last_bid['date'] = self.trade_list[self.end_real_id-_remains_day]
    _remains_day+=1
    __message = self.market.receive_bid(__last_bid, self.setting.client)

    #直到市场不是为0状态位置,停止前推日期
```
在原来的代码里,组合的最后一天需要被平仓,而如果恰巧这一天停牌:(600127,601001 在2017/6/30都是停牌状态)

那么就会一直陷入市场返回500错误,而回测框架一直在组装报价,来回轮询,陷入死循环

现在加入了对于市场的数据的检测,如果是500状态,则会将交易日向前递推一天,重新组装报价,直到停牌的最后一天为止

### 1.20 新增一个时间接口 QA_util_time_now()
2017/7/10

返回的就是datetime.datetime.now()的结果

### 1.21 新增一个QAWeb的接口
2017/7/10

可以在命令行直接输入 quantaxis_web 来启动这个服务器,端口在5050(带socket)

### 1.22 新增一个QACSV的接口

2017/7/13

现在可以便捷的吧数据存成csv格式:

```python
import QUANTAXIS as QA

data=['1',2,'x','t']
QA.QA_util_save_csv(data,'test')

```


### 1.23 新增一个交易时间的变量
2017/7/13

```python
from QUANTAXIS import trade_date_sse

print(trade_date_sse)
```

### 1.24 新增一个k线接口(通达信)
2017/7/13

```python
import QUANTAXIS as QA
QA.QA_fetch_get_stock_day('tdx','601801','2017-01-01','2017-07-01')

```

```shell
Out[3]:
      open  close   high    low       vol       amount  year  month  day  \
0    14.39  14.70  14.76  14.36  164426.0  239606672.0  2016     12   14
1    14.55  14.99  15.10  14.55  188986.0  281594560.0  2016     12   15
2    15.03  16.00  16.11  14.86  180712.0  281681280.0  2016     12   16
3    15.93  16.79  17.05  15.93  207338.0  345849056.0  2016     12   19
4    16.87  16.80  16.87  16.39   81613.0  135869952.0  2016     12   20
5    16.90  16.88  17.12  16.66   98858.0  166289104.0  2016     12   21
6    16.95  16.61  16.96  16.28   92686.0  153868304.0  2016     12   22
7    16.58  16.51  17.05  16.03   89121.0  147409888.0  2016     12   23
8    16.59  17.30  17.65  16.26  226506.0  387817440.0  2016     12   26
..     ...    ...    ...    ...       ...          ...   ...    ...  ...
114  13.22  13.71  13.73  13.16  186511.0  252084368.0  2017      6   26
115  13.74  13.78  13.81  13.54  135037.0  184420320.0  2017      6   27
116  13.73  13.98  14.05  13.56  242043.0  335440128.0  2017      6   28
117  13.94  13.96  14.01  13.84  178812.0  248913488.0  2017      6   29
118  13.89  13.82  13.94  13.71   83402.0  115219784.0  2017      6   30

     hour  minute          datetime
0      15       0  2016-12-14 15:00
1      15       0  2016-12-15 15:00
2      15       0  2016-12-16 15:00
3      15       0  2016-12-19 15:00
4      15       0  2016-12-20 15:00
5      15       0  2016-12-21 15:00
6      15       0  2016-12-22 15:00
7      15       0  2016-12-23 15:00
8      15       0  2016-12-26 15:00
..    ...     ...               ...
114    15       0  2017-06-26 15:00
115    15       0  2017-06-27 15:00
116    15       0  2017-06-28 15:00
117    15       0  2017-06-29 15:00
118    15       0  2017-06-30 15:00

[119 rows x 12 columns]

```

### 1.25 在回测的时候,增加一个回测内全局变量
2017/7/14


现在的回测加载的函数句柄里面会增加一个叫info的句柄,这个句柄在引擎里面是交易日循环外部的变量,可以存贮一些连续周期信息,和一些点位信息


在quantaxis/test/new test的strategy里面可以看到改动


### 1.26 新增一个创建多维list的函数
2017/7/14

在QUANTAXIS.QAUtil中, 接口的名称是  QA_util_multi_demension_list(row_,col_)

如果需要创建一个[[],[]], 那就用 row_=2,col=0
其他时候,返回的都是[[None]]

```python
import QUANTAXIS as QA
QA.QAUtil.QA_util_multi_demension_list(3,0)
QA.QAUtil.QA_util_multi_demension_list(3,3)

```
```shell

[[], [], []]
[[None, None, None], [None, None, None], [None, None, None]]
```


### 1.27 修改了一个QABacktest的传参, 现在在策略中,需要指定买卖状态
2017/7/19

现在 QUANTAXIS在接受策略的传参的时候,需要指定买卖状态

在开始的时候,quantaxis使用的是if_buy和账户状态来判断是否买卖的

- 账户持仓, if_buy=1 视为卖出
- 账户空仓, if_buy=1 视为买入

买卖行为和账户状态相关联对于买卖的行为有很大的限制,现在对于这个行为和账户持仓状态进行了解耦

同时,为了兼容性,如果策略并没有给出if_buy或者if_sell,则会将其初始化为0,及不操作





以下是改动后的源代码

```python
    def __QA_backtest_excute_bid(self, __result,  __date, __hold, __code, __amount):
        """
        这里是处理报价的逻辑部分
        2017/7/19 修改

        __result传进来的变量重新区分: 现在需要有 if_buy, if_sell
        因为需要对于: 持仓状态下继续购买进行进一步的支持*简单的情形就是  浮盈加仓

        if_buy, if_sell都需要传入

        现在的 买卖状态 和 持仓状态 是解耦的
        """

        # 为了兼容性考虑,我们会在开始的时候检查是否有这些变量
        if 'if_buy' not in list(__result.keys()):
            __result['if_buy'] = 0

        if 'if_sell' not in list(__result.keys()):
            __result['if_sell'] = 0

        self.__QA_backtest_set_bid_model()
        if self.bid.bid['bid_model'] == 'strategy':
            __bid_price = __result['price']
        else:
            __bid_price = self.bid.bid['price']

        __bid = self.bid.bid

        __bid['order_id'] = str(random.random())
        __bid['user'] = self.setting.QA_setting_user_name
        __bid['strategy'] = self.strategy_name
        __bid['code'] = __code
        __bid['date'] = __date
        __bid['price'] = __bid_price
        __bid['amount'], __bid['amount_model'] = self.__QA_bid_amount(
            __result['amount'], __amount)

        if __result['if_buy'] == 1:
            # 这是买入的情况
            __bid['towards'] = 1
            __message = self.market.receive_bid(
                __bid, self.setting.client)

            if float(self.account.message['body']['account']['cash'][-1]) > \
                    float(__message['body']['bid']['price']) * \
                    float(__message['body']['bid']['amount']):
                    # 这里是买入资金充足的情况
                    # 不去考虑
                pass
            else:
                # 如果买入资金不充足,则按照可用资金去买入
                __message['body']['bid']['amount'] = int(float(
                    self.account.message['body']['account']['cash'][-1]) / float(
                        float(str(__message['body']['bid']['price'])[0:5]) * 100)) * 100

            if __message['body']['bid']['amount'] > 0:
                # 这个判断是为了 如果买入资金不充足,所以买入报了一个0量单的情况
                #如果买入量>0, 才判断为成功交易
                self.account.QA_account_receive_deal(__message)

        elif __result['if_buy'] == 0:
            # 如果买入状态为0,则不进行任何买入操作
            pass

        # 下面是卖出操作,这里在卖出前需要考虑一个是否有仓位的问题:
        # 因为在股票中是不允许卖空操作的,所以这里是股票的交易引擎和期货的交易引擎的不同所在

        if __result['if_sell'] == 1 and __hold == 1:
            __bid['towards'] = -1
            __message = self.market.receive_bid(
                __bid, self.setting.client)

            self.account.QA_account_receive_deal(
                __message)
```


### 1.28 对于backtest的加载的外部函数的接口进行修改
2017/7/20

对于backtest的加载的外部策略,现在暂时有以下三个句柄

- on_start
- strategy
- on_end

其中,on_start/on_end这两个句柄可有可无, strategy句柄是必须要有的

### 1.29 修改了QA_Query 里返回的数组格式
2017/7/21

```python
def QA_fetch_stock_day(code, startDate, endDate, collections=QA_Setting.client.quantaxis.stock_day, type_='numpy'):
    # print(datetime.datetime.now())
    startDate = str(startDate)[0:10]
    endDate = str(endDate)[0:10]

    if QA_util_date_valid(endDate) == True:

        list_a = []

        for item in collections.find({
            'code': str(code)[0:6], "date_stamp": {
                "$lte": QA_util_date_stamp(endDate),
                "$gte": QA_util_date_stamp(startDate)}}):
            list_a.append([str(item['code']), float(item['open']), float(item['high']), float(
                item['low']), float(item['close']), float(item['volume']), item['date'], float(item['turnover'])])
        ## 多种数据格式
        if type_ == 'numpy':
            data = numpy.asarray(list_a)
        elif type_ == 'list':
            data = list_a
        elif type_ == 'pandas':
            data = DataFrame(list_a, columns=[
                             'code', 'open', 'high', 'low', 'close', 'volume', 'date', 'turnover'])
        return data
    else:
        QA_util_log_info('something wrong with date')

```
现在可以通过QA_fetch_stock_day里面选择是返回list,numpy还是dataframe. 为了兼容性考虑,默认依然是numpy

### 1.30 修改了QA_util_save_csv的模式
2017/07/21


```python
def QA_util_save_csv(data: list, name: str, column=None, location=None):
    # 重写了一下保存的模式
    
    assert isinstance(data, list)
    if location == None:
        path = './' + str(name) + '.csv'
    else:
        path = location + str(name) + '.csv'
    with open(path, 'w', newline='') as f:
        csvwriter = csv.writer(f)
        if column == 'None':
            pass
        else:
            csvwriter.writerow(column)
        for item in data:
            csvwriter.writerow(item)

```

示例:

```python

import QUANTAXIS as QA

QA.QA_util_save_csv(QA.QA_fetch_stock_day('000001','2017-01-01','2017-07-01','list'),'000001')
```
```csv
000001,9.11,9.18,9.09,9.16,459840.47,2017-01-03,0.31
000001,9.15,9.18,9.14,9.16,449329.53,2017-01-04,0.31
000001,9.17,9.18,9.15,9.17,344372.91,2017-01-05,0.24
000001,9.17,9.17,9.11,9.13,358154.19,2017-01-06,0.24
000001,9.13,9.17,9.11,9.15,361081.56,2017-01-09,0.21
000001,9.15,9.16,9.14,9.15,241053.95,2017-01-10,0.14
000001,9.14,9.17,9.13,9.14,303430.88,2017-01-11,0.18
000001,9.13,9.17,9.13,9.15,428006.75,2017-01-12,0.25
000001,9.14,9.19,9.12,9.16,434301.38,2017-01-13,0.26
000001,9.15,9.16,9.07,9.14,683165.81,2017-01-16,0.4
000001,9.12,9.16,9.1,9.15,545552.38,2017-01-17,0.32
000001,9.14,9.19,9.13,9.17,574269.38,2017-01-18,0.34
000001,9.15,9.24,9.15,9.18,437712.88,2017-01-19,0.26
000001,9.17,9.23,9.17,9.22,393328.56,2017-01-20,0.23
000001,9.22,9.26,9.2,9.22,420299.31,2017-01-23,0.25
000001,9.23,9.28,9.2,9.27,470244.09,2017-01-24,0.28
000001,9.27,9.28,9.25,9.26,304401.97,2017-01-25,0.18
000001,9.27,9.34,9.26,9.33,420712.56,2017-01-26,0.25
000001,9.45,10.26,9.33,10.26,19345.0,2017-02-02,0.01
000001,9.34,9.36,9.23,9.26,315472.25,2017-02-03,0.19
000001,9.26,9.32,9.26,9.31,516786.12,2017-02-06,0.31
000001,9.31,9.32,9.27,9.3,396884.97,2017-02-07,0.23
...........
```
### 1.31 通达信5分钟线解析保存
2017/7/23

首先要下载:

- 深圳5分钟线

http://www.tdx.com.cn/products/data/data/vipdoc/sz5fz.zip

- 上证5分钟线

http://www.tdx.com.cn/products/data/data/vipdoc/sh5fz.zip

然后解压到一个目录里

```python

import QUANTAXIS as QA

QA.QA_SU_save_stock_min_5('你解压好的目录')


#例如 QA.QA_SU_save_stock_min_5('C:\\users\\yutiansut\\desktop\\sh5fz')
```
```bash

In [2]: QA.QA_SU_save_stock_min_5('C:\\users\\yutiansut\\desktop\\sz5fz')
QUANTAXIS>> Now_saving 000001's 5 min tick
QUANTAXIS>> Now_saving 000002's 5 min tick
QUANTAXIS>> Now_saving 000004's 5 min tick
QUANTAXIS>> Now_saving 000005's 5 min tick
QUANTAXIS>> Now_saving 000006's 5 min tick
QUANTAXIS>> Now_saving 000007's 5 min tick
QUANTAXIS>> Now_saving 000008's 5 min tick
QUANTAXIS>> Now_saving 000009's 5 min tick
QUANTAXIS>> Now_saving 000010's 5 min tick
QUANTAXIS>> Now_saving 000011's 5 min tick
QUANTAXIS>> Now_saving 000012's 5 min tick
QUANTAXIS>> Now_saving 000014's 5 min tick
QUANTAXIS>> Now_saving 000016's 5 min tick
QUANTAXIS>> Now_saving 000017's 5 min tick
QUANTAXIS>> Now_saving 000018's 5 min tick
QUANTAXIS>> Now_saving 000019's 5 min tick
QUANTAXIS>> Now_saving 000020's 5 min tick
QUANTAXIS>> Now_saving 000021's 5 min tick
QUANTAXIS>> Now_saving 000022's 5 min tick
QUANTAXIS>> Now_saving 000023's 5 min tick
QUANTAXIS>> Now_saving 000024's 5 min tick
QUANTAXIS>> Now_saving 000025's 5 min tick
QUANTAXIS>> Now_saving 000026's 5 min tick
QUANTAXIS>> Now_saving 000027's 5 min tick
QUANTAXIS>> Now_saving 000028's 5 min tick
```

### 1.32 获取指数k线的api更新
2017/7/24

```python
QA_fetch_index_day(code, startDate, endDate,type_='numpy' ,collections=QA_Setting.client.quantaxis.stock_day)

```

一般而言,直接使用QA_fetch_index_day(code, startDate, endDate)就可以了

### 1.33 QA_util更新 QA_util_time_stamp
2017/7/24

QA_util_time_stamp用于将时间转化成时间戳

```python
import QUANTAXIS as QA
QA.QA_util_time_stamp('2017-01-01 10:25:08')

```

### 1.34  QABACKTEST回测引擎更新  
2017/8/1-8/4



重大更新:
现在大量使用@装饰器来扩展回测引擎的能力

```python

import QUANTAXIS as QA
from QUANTAXIS import QA_Backtest_stock_day as QB


"""
写在前面:
===============QUANTAXIS BACKTEST STOCK_DAY中的变量
常量:
QB.account.message  当前账户消息
QB.account.cash  当前可用资金
QB.account.hold  当前账户持仓
QB.account.history  当前账户的历史交易记录
QB.account.assets 当前账户总资产
QB.account.detail 当前账户的交易对账单
QB.account.init_assest 账户的最初资金



QB.strategy_stock_list 回测初始化的时候  输入的一个回测标的
QB.strategy_start_date 回测的开始时间
QB.strategy_end_date  回测的结束时间


QB.today  在策略里面代表策略执行时的日期

QB.benchmark_code  策略业绩评价的对照行情




函数:
获取市场(基于gap)行情:
QB.QA_backtest_get_market_data(QB,code,QB.today)
获取市场自定义时间段行情:
QA.QA_fetch_stock_day(code,start,end,model)


报单:
QB.QA_backtest_send_order(QB, code,amount,towards,order: dict)

order有三种方式:
1.限价成交 order['bid_model']=0或者l,L
  注意: 限价成交需要给出价格:
  order['price']=xxxx

2.市价成交 order['bid_model']=1或者m,M,market,Market
3.严格成交模式 order['bid_model']=2或者s,S
    及 买入按bar的最高价成交 卖出按bar的最低价成交

查询当前一只股票的持仓量
QB.QA_backtest_hold_amount(QB,code)


"""


@QB.backtest_init
def init():
    #
    QB.setting.QA_util_sql_mongo_ip='192.168.4.189'

    QB.account.init_assest=2500000
    QB.benchmark_code='hs300'

    QB.strategy_stock_list=['000001','000002','600010','601801','603111']
    QB.strategy_start_date='2017-03-01'
    QB.strategy_end_date='2017-07-01'

@QB.before_backtest
def before_backtest():
    global risk_position
    QA.QA_util_log_info(QB.account.message)
    
    
    
@QB.load_strategy
def strategy():
    print(QB.account.message)
    print(QB.account.cash)
    input()
    for item in QB.strategy_stock_list:
        if QB.QA_backtest_hold_amount(QB,item)==0:
        #获取数据的第一种办法[这个是根据回测时制定的股票列表初始化的数据]
            QB.QA_backtest_send_order(QB,item,10000,1,{'bid_model':'Market'})

    
        else:
            print(QB.QA_backtest_hold_amount(QB,item))
            QB.QA_backtest_send_order(QB,item,10000,-1,{'bid_model':'Market'})
    
@QB.end_backtest
def after_backtest():
    pass
```
### 1.35 QA_fetch_stock_list 函数更新

一个获取股票代码的函数

```python

import QUANTAXIS as QA
QA.QA_fetch_stock_list()


# 自定义数据库的模式
import pymongo
QA.QA_fetch_stock_list(pymongo.MongoClient(ip='192.168.4.189',port=27017).quantaxis.stock_list)

```


### 1.36 回测框架新增一个一键平仓函数
2017/8/6

一键平仓:
QB.QA_backtest_sell_all(QB)


### 1.37 回测框架的报价函数增加回调
2017/8/6

现在回测的报价函数增加了回调

###1.38 更新了save/update的方式
2017/8/7-2017/8/8

1. update的时候之前出现了 如果该股票尚未上市,数据库无数据的时候 出现负索引的问题 已经解决
2. 把之前写在easy里面的代码 写进了quantaxis cli中

```bash
quantaxis> save

quantaxis> update
```


### 1.39 QUANTAXIS CLI 增加一个选项 CLEAN
2017/8/9

删除旧的回测报告和log文件
```bash
QUANTAXIS

quantaxis> clean
```

### 1.40 QA_util_diff_list
2017/8/9

一个快速返回前后相减的list函数

### 1.41 QUANTAXIS.QABACKTEST.QABACKTEST_STOCKDAY.QA_backtest_get_OHLCV
2017/8/9

一个快速拿到OHLCV的函数

拿到开高收低量
```python
Open,High,Low,Close,Volume=QB.QA_backtest_get_OHLCV(QB,QB.QA_backtest_get_market_data(QB,item,QB.today))

```


### 1.42 QUANTAXIS MARKET ENGINE修改
2017/8/10

增加了一个严格模式的委托方式
增加了收盘价委托的模式


### 1.43 QA_util_get_real_datelist 
2017/8/10

一个直接拿到真实的交易区间的list



### 1.44 QA_fetch_stock_full('date',type)(0.4.0-beta-dev28)
2017/8/14

一个获取某一天全市场数据的接口 type有三种 
1. list   
2. numpy (默认)
3. pandas  

```python
import QUANTAXIS as QA
In [2]: QA.QA_fetch_stock_full('2017-08-01')
```
```bash
Out[2]:

array([['600808', '4.57', '4.62', ..., '4.56', '1217308.12', '2017-08-01'],
       ['600231', '3.85', '3.9', ..., '3.81', '899979.31', '2017-08-01'],
       ['601619', '3.88', '3.88', ..., '3.88', '1856.2', '2017-08-01'],
       ...,
       ['603320', '42.0', '42.95', ..., '42.54', '50230.13', '2017-08-01'],
       ['hs300', '3738.74', '3770.4', ..., '3770.38', '152546544.0',
        '2017-08-01'],
       ['sz50', '2640.87', '2681.93', ..., '2681.81', '338205.06',
        '2017-08-01']],
      dtype='<U11')
```
```python
In [3]: QA.QA_fetch_stock_full('2017-08-01','p')
```
```bash
Out[3]:
              code     open     high      low    close        volume
2017-08-01  600808     4.57     4.62     4.46     4.56  1.217308e+06
2017-08-01  600231     3.85     3.90     3.71     3.81  8.999793e+05
2017-08-01  601619     3.88     3.88     3.88     3.88  1.856200e+03
2017-08-01  300067     6.45     6.72     6.44     6.55  1.744641e+05
2017-08-01  600610     7.23     7.39     7.22     7.29  8.639420e+04
2017-08-01  603778     9.98    10.30     9.90    10.17  1.652618e+05
2017-08-01  601958     8.47     8.48     8.25     8.31  2.703109e+05
2017-08-01  002302    22.15    22.29    21.65    21.81  3.073918e+05
...            ...      ...      ...      ...      ...           ...
2017-08-01  600230    55.99    57.86    54.09    55.07  4.172212e+05
2017-08-01  600291    35.90    38.30    35.60    36.03  9.485712e+05
2017-08-01  300080     9.05     9.37     8.54     8.65  4.989257e+05
2017-08-01  603320    42.00    42.95    40.61    42.54  5.023013e+04
2017-08-01   hs300  3738.74  3770.40  3737.10  3770.38  1.525465e+08
2017-08-01    sz50  2640.87  2681.93  2638.02  2681.81  3.382051e+05

[3053 rows x 6 columns]
```
### 1.45 同花顺日线爬虫可用(0.4.0-beta-dev29)
2017/8/14

```python
import QUANTAXIS as QA
QA.QA_fetch_get_stock_day('ths','000001','2015-01-01','2017-08-01','01')

#引擎用ths或者THS  

#最后一个选项是复权方式
#00 不复权  01 前复权  02 后复权

```
```bash
Out[3]:
             open   high    low  close     volume         amount factor
date
2015-01-05  10.70  10.90  10.43  10.72  286043640  4565387800.00  0.034
2015-01-06  10.60  10.98  10.39  10.55  216642140  3453446100.00  0.025
2015-01-07  10.40  10.59  10.22  10.34  170012060  2634796400.00  0.020
2015-01-08  10.36  10.41   9.94   9.98  140771420  2128003400.00  0.017
...           ...    ...    ...    ...        ...            ...    ...
2017-07-21  10.83  10.95  10.69  10.89  150102000  1625416400.00  0.007
2017-07-24  10.82  11.06  10.73  10.95  169266440  1846886700.00  0.008
2017-07-25  10.98  11.27  10.95  11.00  195476840  2172114600.00  0.009
2017-07-26  10.92  11.18  10.66  10.74  169741210  1846282200.00  0.008
2017-07-27  10.72  10.77  10.53  10.59  119449040  1273888890.00  0.006
2017-07-28  10.61  10.81  10.58  10.74   81919535   877769280.00  0.004
2017-07-31  10.80  10.82  10.45  10.67  157586440  1671814000.00  0.008
2017-08-01  10.64  11.08  10.60  11.04  203570990  2222887900.00  0.010

[629 rows x 7 columns]
```


### 1.46 数据源更换 QA_fetch_get_stock_day('ts')(0.4.0-beta-dev30,dev31,dev32)
2017/8/14

把tushare的数据源更换成腾讯网的

dev31 更新 增加retry次数,增加暂停时间到0.005秒

dev32 更新 retry200次

### 1.47 新增数据库api QA_util_mongo_initial,QA_util_mongo_make_index(0.4.0-beta-dev33)
2017/8/14

QA_util_mongo_initial()

删除数据库数据文件


QA_util_mongo_make_index()

对于日线和分钟线建立索引


也可以在quantaxis cli中使用

QUANTAXIS> drop_database

QUANATXIS> make_index


### 1.48 修复一个委托单超过市场上下限 返回none的bug(0.4.0-beta-dev34)
2017/8/14

现在返回的是market 400状态

### 1.49 修复了pytdx的get_k_data api(0.4.0-beta-dev35)
2017/8/15

之前这个api 因为停牌原因会导致时间索引错位

现在已经修复

```python
In [2]: QA.QA_fetch_get_stock_day('tdx','000001','1997-01-21','1997-03-21')
```
```bash
Out[2]:
             open  close   high    low       vol        amount
date
1997-01-21  16.82  16.98  17.20  16.80  131296.0  2.229589e+08
1997-01-22  17.20  17.49  17.58  17.02  232687.0  4.047471e+08
1997-01-23  17.50  18.13  18.40  17.50  264847.0  4.773427e+08
1997-01-24  18.20  18.05  18.24  17.68  169601.0  3.046991e+08
1997-01-27  18.09  18.04  18.23  17.99  154886.0  2.805207e+08
1997-01-28  18.00  18.25  18.35  18.00  110507.0  2.011880e+08
1997-01-29  18.26  18.81  19.09  18.24  200763.0  3.763796e+08
1997-01-30  19.01  18.98  19.12  18.66  125712.0  2.374635e+08
1997-01-31  19.00  19.29  19.50  18.90  271490.0  5.232251e+08
1997-02-17  18.98  19.30  19.55  18.73  179070.0  3.419574e+08
1997-02-18  19.00  17.61  19.09  17.30  636572.0  1.145977e+09
1997-02-19  18.00  18.91  18.95  18.00  454504.0  8.426491e+08
1997-02-20  17.03  18.88  19.62  17.03  629958.0  1.170372e+09
1997-02-21  18.80  19.00  19.10  18.68  228541.0  4.309114e+08
1997-02-24  19.10  18.89  19.23  18.87  142884.0  2.713711e+08
1997-02-25  19.00  19.39  19.78  18.83  284111.0  5.501372e+08
1997-02-26  19.60  19.54  19.69  19.35  129555.0  2.524559e+08
1997-02-27  19.50  19.30  19.60  19.20  158984.0  3.085820e+08
1997-02-28  19.25  19.20  19.28  18.90  149898.0  2.866645e+08
1997-03-03  19.28  19.36  19.56  19.18  122863.0  2.377923e+08
1997-03-04  19.33  19.15  19.33  19.00  156856.0  3.004253e+08
1997-03-05  19.18  19.01  19.32  19.00  114645.0  2.188174e+08
1997-03-06  18.98  19.05  19.10  18.89   95569.0  1.818445e+08
1997-03-07  19.08  19.12  19.35  19.00   98483.0  1.882669e+08
1997-03-10  19.20  19.44  19.63  19.15  128497.0  2.496492e+08
1997-03-11  19.45  19.62  19.65  19.27  183575.0  3.580383e+08
1997-03-12  19.70  20.05  20.20  19.64  251126.0  5.020225e+08
1997-03-13  20.10  19.89  20.30  19.75  178583.0  3.577445e+08
1997-03-14  19.88  20.33  20.39  19.60  171159.0  3.415037e+08
1997-03-17  20.80  22.30  22.37  20.80  465572.0  1.015967e+09
1997-03-18  22.50  22.55  23.45  21.90  439436.0  9.973509e+08
1997-03-19  22.60  23.40  23.75  22.45  423729.0  9.799536e+08
1997-03-20  23.51  23.18  24.24  23.00  318485.0  7.548200e+08
1997-03-21  23.01  24.40  24.45  23.01  333392.0  7.951931e+08
```


### 1.50 修复了一个因为市场返回400状态导致账户数据溢出的bug(0.4.0-beta-dev36,37)
2017/8/15

现在只有成功交易的委托单才能被计入账户的修改

### 1.51 QA_data_fq_factor获取从1990年以来的前后复权因子,QA_fetch_get_stock_day 兼容性改动(0.4.0-beta-dev38)
2017/8/15

QAData包  新增一个获取前后复权因子的api
```python
QA_data_fq_factor(code)
```
```bash
            qfqfactor   hfqfactor  bfqfactor
date
1991-01-02   0.006528    1.000000        1.0
1991-01-03   0.006518    1.000000        1.0
1991-01-04   0.006517    1.000000        1.0
1991-01-05   0.006508    1.000000        1.0
1991-01-07   0.006512    1.000000        1.0
1991-01-08   0.006515    1.000000        1.0
1991-01-09   0.006514    1.000000        1.0
1991-01-10   0.006512    1.000000        1.0
1991-01-11   0.006516    1.000000        1.0
...               ...         ...        ...
2017-08-02   1.000000  153.325882        1.0
2017-08-03   1.000000  153.325853        1.0
2017-08-04   1.000000  153.325818        1.0
2017-08-07   1.000000  153.325859        1.0
2017-08-08   1.000000  153.325818        1.0
2017-08-09   1.000000  153.325821        1.0
2017-08-10   1.000000  153.325888        1.0
2017-08-11   1.000000  153.325859        1.0
2017-08-14   1.000000  153.325864        1.0

[6327 rows x 3 columns]
```

QA_fetch_get_stock_day 兼容性改动

现在可以选择走tushare的引擎 选择拿到是洗好的json格式还是pandas格式,默认还是json

```
bfq=QA_fetch_get_stock_day('ts',code,'1991-01-01','','00','pd/json')
qfq=QA_fetch_get_stock_day('ts',code,'1991-01-01','','01','pd/json')
hfq=QA_fetch_get_stock_day('ts',code,'1991-01-01','','02','pd/json')
```
### 1.52 QATDX改动(0.4.0-b-dev39)
2017/8/15

QATDX之前在获取日线的时候,虽然修复了时间索引 但是没有考虑到800条数据上限的问题

现在进行了修复

```python

QA.QA.QA_fetch_get_stock_day('tdx','000001','1990-01-01','2017-08-01')
```

### 1.53 Darwin平台的quantaxis 生成路径问题(0.4.0-b-dev40)
2017/8/15


### 1.54 支持下载时候 遇到网络问题 断点续传(0.4.0-beta-dev41)
2017/8/15

QUANTAXIS> update

### 1.55 分钟线获取接口(0.4.0-beta-dev42 43)

2017/08/16


```python
import QUANTAXIS as QA
QA.QA_fetch_get_stock_min('tdx','000002','2017-07-11 09:30:00','2017-08-01 10:00:00','1')

```

QA.QA_fetch_get_stock_min('tdx',code,start,end,type)

type:
- 1,1m,1min
- 5,5m,5min
- 15,15m,15min
- 30,30m,30min
- 60,60m,60min



### 1.56 QA_Util 新增格式转换 (0.4.0-beta-dev44)
2017/08/16

```python
import QUANTAXIS as QA
QA.QA_util_to_json_from_pandas(DataFrame)
```


### 1.57 QA_SU 新增复权因子的保存(0.4.0-beta-dev44)

2017/08/16

```python
import QUANTAXIS as QA
QA.QA_SU_save_stock_fqfactor()
```
### 1.58 优化QA_QAQuery 和QAMarket_engine的代码(0.4.0-beta-dev44,45,46,47)

2017/08/17

- QA_Query 代码清洗

- QAMarket_engine 数据库隔离

- 日线交易引擎成交价优化

- 日线交易引擎的显示更新

- 回测和交易委托的api修改


### 1.59 QA_fetch_get_stock_transaction('tdx',code,start,end,retry,ip,port)(0.4.0-beta-dev48,49)
2017/8/18

历史分笔数据获取端口
```python
QA.QA_fetch_get_stock_transaction('tdx','000002','2000-07-12','2001-01-25')
```
```
             time  price  vol  buyorsell        date    code  order
date
2000-07-12  09:30  13.64   68          2  2000-07-12  000002      0
2000-07-12  09:31  13.66  306          0  2000-07-12  000002      1
2000-07-12  09:31  13.66    1          1  2000-07-12  000002      2
2000-07-12  09:31  13.70   20          0  2000-07-12  000002      3
2000-07-12  09:31  13.70   53          0  2000-07-12  000002      4
2000-07-12  09:31  13.70   20          0  2000-07-12  000002      5
2000-07-12  09:32  13.66    8          1  2000-07-12  000002      6
2000-07-12  09:32  13.70   17          0  2000-07-12  000002      7
2000-07-12  09:32  13.70   62          0  2000-07-12  000002      8
...           ...    ...  ...        ...         ...     ...    ...
2001-01-19  10:38  14.99   50          0  2001-01-19  000002    335
2001-01-19  10:38  14.99  100          0  2001-01-19  000002    336
2001-01-19  10:38  14.99    6          0  2001-01-19  000002    337
2001-01-19  10:39  14.99   67          0  2001-01-19  000002    338
2001-01-19  10:39  14.99    6          0  2001-01-19  000002    339
2001-01-19  10:39  14.99    5          0  2001-01-19  000002    340
2001-01-19  10:39  14.99   12          0  2001-01-19  000002    341
2001-01-19  10:39  14.99   85          0  2001-01-19  000002    342
2001-01-19  10:40  14.98   13          1  2001-01-19  000002    343
2001-01-19  10:40  14.99   51          0  2001-01-19  000002    344
2001-01-19  10:40  14.99   20          0  2001-01-19  000002    345

[36119 rows x 7 columns]
```
### 1.60 新增多个QAUtil的api (0.4.0-beta-dev50)
- QA_util_if_trade(day) 是否交易函数
- QA_util_get_trade_range(start,end) 根据开始,结束日期 给出交易日列表

> QA_util_make_ 系列:

1. 要求day一定要是交易日
2. 给出的分钟线数据都是标准的交易格式 9:31-11:30 1:00-3:00

- QA_util_make_15min_bar(day)
- QA_util_make_1h_bar(day)
- QA_util_make_1min_bar(day)
- QA_util_make_5min_bar(day)
- QA_util_make_30min_bar(day)
- QA_util_make_bar(type, start, end=None)  [跨日期的获取,如果没有end,就是单日的获取]
[ QA_util_make_bar  会自动给出交易段的bar  交易日+交易时间  type可选择 1m,5m,15m,30m,60m,1h]

```python
                                                
In [2]: QA.QA_util_make_1min_bar('2017-08-17')  
```
```
Out[2]:                                         
                    open high  low close volume 
2017-08-17 09:31:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 09:32:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 09:33:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 09:34:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 09:35:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 09:36:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 09:37:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 09:38:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 09:39:00  NaN  NaN  NaN   NaN    NaN 
...                  ...  ...  ...   ...    ... 
2017-08-17 14:52:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 14:53:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 14:54:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 14:55:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 14:56:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 14:57:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 14:58:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 14:59:00  NaN  NaN  NaN   NaN    NaN 
2017-08-17 15:00:00  NaN  NaN  NaN   NaN    NaN 
                                                
[240 rows x 5 columns]                          
```
## 巨大改动/重构

### 2.1 QA.QAARP.QAAccount
在0.3.9-gamma中,quantaxis对于account账户方法进行了重构.优化了回测逻辑以及数组的存储方式.

现在的account只有如下几个变量:

- assets: 总资金曲线
- hold: 持仓列表
- history : 历史交易列表
- cash: 历史现金列表
- detail: 买卖明细表(有买入id和卖出id对应关系)



新版的quantaxis并不在回测框架中定义利润的计算以及其他的逻辑,这些在backtest_analysis中会涉及计算,当然也可以自己定义利润的计算方法
### 2.2 QA.QABacktest.Backtest_analysis

对于quantaxis_backtest_analysis进行了巨大的修改,现在的backtest_analysis的接口调用函数有了一定程度的修改.

对于交易组合而言,quantaxis的backtest_analysis 可以直接对于组合进行分析,计算组合的情况

增加了可以自己选定组合的benchmark标的

### 2.3 QA.QABacktest.QABacktest

对于QABacktest进行了彻底的重构,重新写入了读取数据方法和函数句柄的接受方法,具体参见test/new test


### 2.4 QA.QA_Queue

事件队列,参见 ###1.14


### 2.5 彻底放弃QUANTAXIS-WEBKIT-CLIENT

webkit/client 是一个基于electronic的客户端,但是其功能本质上和网页版并无区别,且缺乏维护

0.4.0-alpha中将其去除,之后也不会再维护


### 2.6 更换QABACKTEST的回测模式

参见 ###1.34
```python
import QUANTAXIS as QA
from QUANTAXIS import QA_Backtest_stock_day as QB


"""
写在前面:
===============QUANTAXIS BACKTEST STOCK_DAY中的变量
常量:
QB.account.message  当前账户消息
QB.account.cash  当前可用资金
QB.account.hold  当前账户持仓
QB.account.history  当前账户的历史交易记录
QB.account.assets 当前账户总资产
QB.account.detail 当前账户的交易对账单
QB.account.init_assest 账户的最初资金



QB.strategy_stock_list 回测初始化的时候  输入的一个回测标的
QB.strategy_start_date 回测的开始时间
QB.strategy_end_date  回测的结束时间


QB.today  在策略里面代表策略执行时的日期

QB.benchmark_code  策略业绩评价的对照行情




函数:
获取市场(基于gap)行情:
QB.QA_backtest_get_market_data(QB,code,QB.today)
获取市场自定义时间段行情:
QA.QA_fetch_stock_day(code,start,end,model)


报单:
QB.QA_backtest_send_order(QB, code,amount,towards,order: dict)

order有三种方式:
1.限价成交 order['bid_model']=0或者l,L
  注意: 限价成交需要给出价格:
  order['price']=xxxx

2.市价成交 order['bid_model']=1或者m,M,market,Market
3.严格成交模式 order['bid_model']=2或者s,S
    及 买入按bar的最高价成交 卖出按bar的最低价成交

查询当前一只股票的持仓量
QB.QA_backtest_hold_amount(QB,code)


"""


@QB.backtest_init
def init():
    #
    QB.setting.QA_util_sql_mongo_ip='192.168.4.189'

    QB.account.init_assest=2500000
    QB.benchmark_code='hs300'

    QB.strategy_stock_list=['000001','000002','600010','601801','603111']
    QB.strategy_start_date='2017-03-01'
    QB.strategy_end_date='2017-07-01'

@QB.before_backtest
def before_backtest():
    global risk_position
    QA.QA_util_log_info(QB.account.message)
    
    
    
@QB.load_strategy
def strategy():
    print(QB.account.message)
    print(QB.account.cash)
    input()
    for item in QB.strategy_stock_list:
        if QB.QA_backtest_hold_amount(QB,item)==0:
        #获取数据的第一种办法[这个是根据回测时制定的股票列表初始化的数据]
            QB.QA_backtest_send_order(QB,item,10000,1,{'bid_model':'Market'})

    
        else:
            print(QB.QA_backtest_hold_amount(QB,item))
            QB.QA_backtest_send_order(QB,item,10000,-1,{'bid_model':'Market'})
    
@QB.end_backtest
def after_backtest():
    pass

```


### 2.7 数据源更换(0.4.0-beta-dev30)

对比了通达信,同花顺,ifeng,腾讯财经的数据源
前复权:
```bash
====================腾讯======================
600340
2009-09-02
http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?_var=kline_dayqfq2009&param=sh600340,day,2009-01-01,2010-12-31,640,qfq&r=0.18617627655340497
[{'date': '2009-09-02', 'open': 1.264, 'close': 1.293, 'high': 1.303, 'low': 1.264, 'volume': 30684.29, 'code': '600340', 'date_stamp': 1251820800.0, 'fqtype': 'qfq'}, {'date': '2009-09-03', 'open': 1.307, 'close': 1.357, 'high': 1.357, 'low': 1.307, 'volume': 40504.84, 'code': '600340', 'date_stamp': 1251907200.0, 'fqtype': 'qfq'}, {'date': '2009-09-04', 'open': 1.423, 'close': 1.425, 'high': 1.425, 'low': 1.386, 'volume': 52082.41, 'code': '600340', 'date_stamp': 1251993600.0, 'fqtype': 'qfq'}, {'date': '2009-09-07', 'open': 1.462, 'close': 1.471, 'high': 1.497, 'low': 1.425, 'volume': 69120.01, 'code': '600340', 'date_stamp': 1252252800.0, 'fqtype': 'qfq'}, {'date': '2009-09-09', 'open': 1.544, 'close': 1.544, 'high': 1.544, 'low': 1.544, 'volume': 2528.08, 'code': '600340', 'date_stamp': 1252425600.0, 'fqtype': 'qfq'}, {'date': '2009-09-10', 'open': 1.621, 'close': 1.621, 'high': 1.621, 'low': 1.592, 'volume': 65376.57, 'code': '600340', 'date_stamp': 1252512000.0, 'fqtype': 'qfq'}, {'date': '2009-09-11', 'open': 1.694, 'close': 1.633, 'high': 1.694, 'low': 1.615, 'volume': 105574.09, 'code': '600340', 'date_stamp': 1252598400.0, 'fqtype': 'qfq'}, {'date': '2009-09-14', 'open': 1.619, 'close': 1.715, 'high': 1.715, 'low': 1.593, 'volume': 90609.98, 'code': '600340', 'date_stamp': 1252857600.0, 'fqtype': 'qfq'}, {'date': '2009-09-15', 'open': 1.743, 'close': 1.73, 'high': 1.782, 'low': 1.707, 'volume': 45260.01, 'code': '600340', 'date_stamp': 1252944000.0, 'fqtype': 'qfq'}, {'date': '2009-09-16', 'open': 1.702, 'close': 1.733, 'high': 1.747, 'low': 1.662, 'volume': 48149.54, 'code': '600340', 'date_stamp': 1253030400.0, 'fqtype': 'qfq'}]
====================ths同花顺======================
600340
2009-09-02
             open   high    low  close    volume        amount  factor
date
2009-09-02  -0.48  -0.44  -0.48  -0.45   3068429   30789151.00  15.202
2009-09-03  -0.43  -0.38  -0.43  -0.38   4050484   42518565.00  20.068
2009-09-04  -0.31  -0.30  -0.35  -0.30   5208241   57345823.00  25.804
2009-09-07  -0.26  -0.23  -0.30  -0.25   6912001   79692366.00  34.245
2009-09-09  -0.18  -0.18  -0.18  -0.18    252808    3041280.00   1.253
2009-09-10  -0.09  -0.09  -0.12  -0.09   6537657   82537179.00  32.390
2009-09-11  -0.01  -0.01  -0.10  -0.08  10557409  135804180.00  52.306
2009-09-14  -0.10   0.01  -0.12   0.01   9060998  117785149.00  44.892
2009-09-15   0.04   0.08   0.00   0.03   4526001   61421440.00  22.424
2009-09-16  -0.00   0.04  -0.05   0.03   4814954   63716609.00  23.855
In [3]: =======凤凰网=====
ts.get_h_data('600340','2009-09-02','2009-09-16',autype='qfq')
[Getting data:]Out[3]:
             open   high  close    low      volume       amount
date
2009-09-16  39.29  40.33  40.00  38.37   4814954.0   63716608.0
2009-09-15  40.24  41.13  39.94  39.41   4526001.0   61421440.0
2009-09-14  37.37  39.59  39.59  36.77   9060998.0  117785152.0
2009-09-11  39.11  39.11  37.69  37.28  10557409.0  135804192.0
2009-09-10  37.43  37.43  37.43  36.74   6537657.0   82537176.0
2009-09-09  35.65  35.65  35.65  35.65    252808.0    3041280.0
2009-09-07  33.75  34.55  33.96  32.89   6912001.0   79692368.0
2009-09-04  32.86  32.89  32.89  32.00   5208241.0   57345824.0
2009-09-03  30.17  31.32  31.32  30.17   4050484.0   42518564.0
2009-09-02  29.19  30.08  29.84  29.19   3068429.0   30789152.0
```

对比发现,ifeng,同花顺,通达信(软件)的复权方法有问题,最终采用wind/腾讯的数据作为数据源

缺点是这样没有turnover数据


## 重要性能优化  重新定义回测流程,减少数据库IO压力

在新的回测框架中,大幅优化了数据的读取方式,通过大量的内存结构来进行数据缓存,之后的数据调用请求都通过内存中的数据接口来获得,这样大大减少了数据库IO

同时,通过对于Account账户的修改,大幅优化了回测数据的存储方式,以及存储的的模式,大大减少了回测数据存储的数量


## 废弃的接口


## to do list