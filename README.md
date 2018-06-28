
# QUANTAXIS 量化金融策略框架



[![Github workers](https://img.shields.io/github/watchers/quantaxis/quantaxis.svg?style=social&label=Watchers&)](https://github.com/quantaxis/quantaxis/watchers)
[![GitHub stars](https://img.shields.io/github/stars/quantaxis/quantaxis.svg?style=social&label=Star&)](https://github.com/quantaxis/quantaxis/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/quantaxis/quantaxis.svg?style=social&label=Fork&)](https://github.com/quantaxis/quantaxis/fork)


> ENGLISH DOCUMENTS PLEASE CLICK [THIS](README_ENG.md)

[点击右上角Star和Watch来跟踪项目进展! 点击Fork来创建属于你的QUANTAXIS!]

![post201802](http://pic.yutiansut.com/quantaxis-post201802.png)
![main_1](http://pic.yutiansut.com/Main_1.gif)
![logo](http://pic.yutiansut.com/QUANTAXIS-small.png)
![presentbyyutiansut](http://pic.yutiansut.com/yutiansut-logo.png)


![version](https://img.shields.io/pypi/v/quantaxis.svg)
![build](https://travis-ci.org/QUANTAXIS/QUANTAXIS.svg?branch=master)
[![Codefresh build status]( https://g.codefresh.io/api/badges/build?repoOwner=yutiansut&repoName=QUANTAXIS&branch=master&pipelineName=QUANTAXIS&accountName=yutiansut_marketplace&type=cf-1)]( https://g.codefresh.io/repositories/yutiansut/QUANTAXIS/builds?filter=trigger:build;branch:master;service:5a30c1026e9d6c0001c5143b~QUANTAXIS)
[![BCH compliance](https://bettercodehub.com/edge/badge/QUANTAXIS/QUANTAXIS?branch=master)](https://bettercodehub.com/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d8504e4af33747bb8117579212425af9)](https://www.codacy.com/app/yutiansut/QUANTAXIS?utm_source=github.com&utm_medium=referral&utm_content=yutiansut/QUANTAXIS&utm_campaign=badger)
[![Stories in Ready](https://badge.waffle.io/yutiansut/QUANTAXIS.svg?label=ready&title=Ready)](http://waffle.io/yutiansut/QUANTAXIS)
[![StackShare](https://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/yutiansut/quantaxis)
![QAS](https://img.shields.io/badge/QAS-%200.0.8-brown.svg)
![python](https://img.shields.io/badge/python-%203.6/3.5/3.4/win/ubuntu-darkgrey.svg)
![Npm](https://img.shields.io/badge/Npm-%200.4.0-yellow.svg)
![author](https://img.shields.io/badge/Powered%20by-%20%20yutiansut-red.svg)
![license](https://img.shields.io/badge/License-%20MIT-brightgreen.svg)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FQUANTAXIS%2FQUANTAXIS.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FQUANTAXIS%2FQUANTAXIS?ref=badge_shield)




> 欢迎加群讨论: 563280067 [群链接](https://jq.qq.com/?_wv=1027&k=4CEKGzn) 

> 欢迎关注公众号: ![公众号](http://pic.yutiansut.com/qrcode_for_gh_bbb47e0550f7_258%20%281%29.jpg)

> 许多问题 可以在 [GITHUB ISSUE](https://github.com/QUANTAXIS/QUANTAXIS/issues)中找到, 你可以提出新的issue

QUANTAXIS量化金融策略框架,是一个面向中小型策略团队的量化分析解决方案. 我们通过高度解耦的模块化以及标准化协议,可以快速的实现面向场景的定制化解决方案.QUANTAXIS是一个渐进式的开放式框架,你可以根据自己的需要,引入自己的数据,分析方案,可视化过程等,也可以通过RESTful接口,快速实现多人局域网/广域网内的协作.

<!-- TOC -->

- [QUANTAXIS 量化金融策略框架](#quantaxis-量化金融策略框架)
    - [电脑配置推荐](#电脑配置推荐)
    - [1. 功能](#1-功能)
    - [2. 文档](#2-文档)
    - [3. 安装和部署](#3-安装和部署)
    - [4. 更新](#4-更新)
    - [5. Docker](#5-docker)
    - [6. 使用说明](#6-使用说明)
    - [7. Jupyter示例](#7-jupyter示例)
    - [8. 开发计划](#8-开发计划)
    - [9. 常见问题FAQ](#9-常见问题faq)
    - [10. 项目捐赠](#10-项目捐赠)
    - [11. 回测Webkit插件概览](#11-回测webkit插件概览)
    - [12. QUANTAXIS 标准化协议和未来协议](#12-quantaxis-标准化协议和未来协议)
    - [License](#license)

<!-- /TOC -->

## 电脑配置推荐

推荐配置:
6代以上CPU+ 16/32GB DDR3/DDR4内存+ 256GB以上SSD硬盘

最低配置:
支持X64位的CPU

因为在存储本地数据的时候,需要存储超过2GB的本地数据,而32位的MONGODB最高只支持2GB左右的数据存储,因此最少需要一个X64位的CPU

如果SSD资源够用,尽量将数据存储在SSD中,增加```wiretiger```写盘的速度

如果是阿里云/腾讯云的服务器,请在最初的时候 选择64位的操作系统


##  1. 功能
======

![](http://pic.yutiansut.com/framework.png)

已经实现：

- [x] 日线（自1990年）回测 [定点复权] (T+1)
- [x] 分钟线 [1min/5min/15min/30min/60min]回测 (T+1)
- [x] 股指期货日线(T+0)/指数日线/ETF日线
- [x] 股指期货分钟线(T+0) / 指数分钟线/ETF分钟线 [1min/5min/15min/30min/60min]
- [x] 期货日线/分钟线(期货指数/期货主连/期货合约)
- [x] 基于[pytdx](https://github.com/rainx/pytdx)/[tushare](https://github.com/waditu/tushare)以及各种爬虫的数据源 
- [x] 实时交易数据,实时tick
- [x] 基于Vue.js的前端网站
- [x] 自定义的数据结构QADataStruct
- [x] 指标计算QAIndicator
- [x] 板块数据(0.5.1新增)/同花顺,通达信板块
- [x] 基本面数据(部分 最新一期财务报表)
- [x] 行情分发
- [x] 自定义账户类/组合类/用户类
- [x] 自定义市场类/可接入的下单接口(BROKER)
- [x] 分布式数据库连接(mongodb集群)/带权限数据库
- [x] 用户分析模块/风控,表现插件
- [x] 指标类(1.0.42新增)
- [x] 成交记录分析器
- [x] T0交易(股票日内做T)回测分析框架(1.0.46)
- [x] 1996至今的每一季度的财务数据(1.0.52)
- [x] 文档更新
- [x] 数据库权限管理
- [x] 期货数据(郑州/大连/上海/上期/中金)
- [x] 现货数据(渤海商品期货/齐鲁商品期货/上海T+D黄金(伦敦金交割))
- [x] 期权数据(郑州商品期权/大连商品期权/上海商品期权/中金所期权/上海股票期权)
- [x] 港股数据(港股主板/港股创业板/港股指数/港股基金)
- [x] 美股数据
- [x] 国际期货数据(伦敦金属/伦敦石油/纽约商品/纽约石油/芝加哥谷/东京工业品/纽约期货/新加坡期货/马来期货)
- [x] 宏观指标
- [x] 汇率数据(基础汇率/交叉汇率)

预计实现:

- [ ] 期货回测
- [ ] 实盘
- [ ] 分析模块(行情分析/板块分析)
- [ ] 多数据库支持



- [QUANTAXIS 2018开发计划表](job_list.md)


##  2. 文档

文档参见: [book](http://book.yutiansut.com)

下载文档手册(实时更新)

[PDF](https://www.gitbook.com/download/pdf/book/quantaxis/quantaxis) | [MOBI](https://www.gitbook.com/download/mobi/book/quantaxis/quantaxis) | [EPUB](https://www.gitbook.com/download/epub/book/quantaxis/quantaxis)

##  3. 安装和部署

直接上手~

```
pip install quantaxis -U
```

本地安装
```
git clone https://github.com/yutiansut/quantaxis --depth 1
```

代码提交式安装 代码提交参见  [代码提交](https://github.com/QUANTAXIS/QUANTAXIS/blob/master/Documents/about_pr.md)

- fork QUANTAXIS 到你的github账户

```
git clone https://github.com/你的账户名/quantaxis
```

参见 [安装说明](Documents/install.md)

##  4. 更新
参见 [更新说明](Documents/update.md)

##  5. Docker
参见 [Docker](Documents/docker.md)
##  6. 使用说明
参见 


* [QUANTAXIS的使用示例](https://github.com/quantaxis/QADemo)

* [QUANTAXIS回测API](Documents/backtest_api.md)
* [QUANTAXIS的数据结构](Documents/DataStruct.md)
* [QUANTAXIS指标系统及指标类](Documents/indicators.md)
* [QUANTAXIS的数据获取指南](Documents/DataFetch.md)
* [QUANTAXIS行情研究](Documents/analysis.md)
* [QUANTAXIS回测分析](Documents/backtestanalysis.md)
* [常见策略整理](Documents/strategy.md)

##  7. Jupyter示例
参见 [Jupyter示例](jupyterexample)


##  8. 开发计划
参见 [开发计划](job_list.md)
##  9. 常见问题FAQ
参见 [FAQ](Documents/FAQ.md)

##  10. 项目捐赠

写代码不易...请作者喝杯咖啡呗?


![](http://pic.yutiansut.com/alipay.png)

(PS: 支付的时候 请带上你的名字/昵称呀 会维护一个赞助列表~ )

[捐赠列表](CONTRIBUTING.md)



##  11. 回测Webkit插件概览

![](http://pic.yutiansut.com/homepage.png)
![](http://pic.yutiansut.com/loginpage.png)
![](http://pic.yutiansut.com/adminpage.png)
![](http://pic.yutiansut.com/backtestpage.png)
![](http://pic.yutiansut.com/rebacktest.png)
![](http://pic.yutiansut.com/backtestpic.png)
![](http://pic.yutiansut.com/strategy.png)
![](http://pic.yutiansut.com/kline.png)
![](http://pic.yutiansut.com/settings.png)


##  12. QUANTAXIS 标准化协议和未来协议


QUANTAXIS-Stardand-Protocol 版本号0.0.8

详情参见  [QUANATXISProtocol](Documents/readme.md)


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FQUANTAXIS%2FQUANTAXIS.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FQUANTAXIS%2FQUANTAXIS?ref=badge_large)
