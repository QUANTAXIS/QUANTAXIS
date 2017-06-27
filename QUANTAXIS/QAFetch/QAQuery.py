# encoding: UTF-8
from QUANTAXIS.QAUtil import QA_util_log_info
from QUANTAXIS.QAUtil import QA_util_date_valid, QA_util_date_stamp
from pandas import DataFrame
from bson.objectid import ObjectId
import numpy
import datetime

"""
按要求从数据库取数据，并转换成numpy结构

"""


def QA_fetch_stock_day(code, startDate, endDate, collections):
    # print(datetime.datetime.now())
    startDate = str(startDate)[0:10]
    endDate = str(endDate)[0:10]

    if QA_util_date_valid(endDate) == True:

        list_a = [[], [], [], [], [], [], []]

        for item in collections.find({'code': str(code)[0:6], "date_stamp": {"$lte": QA_util_date_stamp(endDate), "$gte": QA_util_date_stamp(startDate)}}):
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


def QA_fetch_trade_date(collections):
    data = []
    for item in collections.find({}):

        data.append(item['date'])
    print(len(data))
    return data


def QA_fetch_stock_info(code, collections):
    pass


def QA_fetch_stocklist_day(stock_list, collections, date_range):
    data = []
    for item in stock_list:
        data.append(QA_fetch_stock_day(
            item, date_range[0], date_range[-1], collections))
    return data
