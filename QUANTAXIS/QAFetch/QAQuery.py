# coding: utf-8
#
# The MIT License (MIT)
#
# Copyright (c) 2016-2017 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import datetime

import numpy
from bson.objectid import ObjectId
from pandas import DataFrame

from QUANTAXIS.QAUtil import (QA_util_date_stamp, QA_util_date_valid,
                              QA_util_log_info)


"""
按要求从数据库取数据，并转换成numpy结构

"""


def QA_fetch_stock_day(code, startDate, endDate, collections):
    # print(datetime.datetime.now())
    startDate = str(startDate)[0:10]
    endDate = str(endDate)[0:10]

    if QA_util_date_valid(endDate) == True:

        list_a = [[], [], [], [], [], [], [], []]

        for item in collections.find({
            'code': str(code)[0:6], "date_stamp": {
                "$lte": QA_util_date_stamp(endDate), 
                "$gte": QA_util_date_stamp(startDate)}}):
            # print(item['code'])

            list_a[0].append(item['code'])
            list_a[1].append(item['open'])
            list_a[2].append(item['high'])
            list_a[3].append(item['low'])
            list_a[4].append(item['close'])
            list_a[5].append(item['volume'])
            list_a[6].append(item['date'])
            list_a[7].append(item['turnover'])

        data = numpy.asarray(list_a).transpose()

        return data
    else:
        QA_util_log_info('something wrong with date')


def QA_fetch_trade_date(collections):
    data = []
    for item in collections.find({}):
        data.append(item['date'])
    return data


def QA_fetch_stock_info(code, collections):
    pass


def QA_fetch_stocklist_day(stock_list, collections, date_range):
    data = []
    for item in stock_list:
        data.append(QA_fetch_stock_day(
            item, date_range[0], date_range[-1], collections))
    return data


def QA_fetch_index_day(code, startDate, endDate, collections):
    # print(datetime.datetime.now())
    startDate = str(startDate)[0:10]
    endDate = str(endDate)[0:10]

    if QA_util_date_valid(endDate) == True:

        list_a = [[], [], [], [], [], [], []]

        for item in collections.find({
            'code': str(code), "date_stamp": {
                "$lte": QA_util_date_stamp(endDate),
                "$gte": QA_util_date_stamp(startDate)
            }
        }):
            # print(item['code'])

            list_a[0].append(item['code'])
            list_a[1].append(item['open'])
            list_a[2].append(item['high'])
            list_a[3].append(item['low'])
            list_a[4].append(item['close'])
            list_a[5].append(item['volume'])
            list_a[6].append(item['date'])

        data = numpy.asarray(list_a).transpose()

        return data
    else:
        QA_util_log_info('something wrong with date')
