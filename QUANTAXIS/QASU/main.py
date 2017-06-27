#coding:utf-8
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


from . import save_tushare as sts
from . import save_wind as sw
from . import update_tushare as uts
from . import update_wind as uw


def QA_SU_save_stock_list(engine,client):
    engine=select_engine(engine)
    engine.QA_SU_save_stock_list(client)

def QA_SU_save_trade_date(engine,client):
    engine=select_engine(engine)
    engine.QA_SU_save_trade_date(client)
def QA_SU_save_stock_info(engine,client):
    engine=select_engine(engine)
    engine.QA_SU_save_stock_info(client)
def QA_SU_save_stock_day(name, startDate, endDate, engine, client):
    engine=select_engine(engine)
    engine.QA_SU_save_stock_day(name, startDate, endDate, client)

def QA_SU_save_stock_day_init(startDate,engine,client):
    engine=select_engine(engine)
    engine.QA_SU_save_stock_day_init(startDate,client)


def QA_SU_update_stock_day(engine, client):
    engine=select_update_engine(engine)
    engine.QA_update_stock_day_all(client)

def select_engine(engine):
    if engine in ['wind','Wind','WIND']:
       return sw
    elif engine in ['tushare','ts','Tushare']:
       return sts

def select_update_engine(engine):
    if engine in ['wind','Wind','WIND']:
       return uw
    elif engine in ['tushare','ts','Tushare']:
       return uts
