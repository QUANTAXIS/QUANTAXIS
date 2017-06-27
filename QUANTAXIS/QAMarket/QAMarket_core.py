# coding :utf-8

from QUANTAXIS.QAUtil import QA_util_sql_mongo_setting, QA_util_log_info
from QUANTAXIS.QAUtil import QA_Setting
from QUANTAXIS.QASignal import QA_signal_send
from .QABid import QA_QAMarket_bid
#from .market_config import stock_market,future_market,HK_stock_market,US_stock_market
import datetime
import random


class QA_Market():

    # client=QA_Setting.client
    # client=QA.QA_util_sql_mongo_setting()
    # db= client.market
    def market_make_deal(self, bid, client):
        coll = client.quantaxis.stock_day
        try:
            item = coll.find_one(
                {"code": str(bid['code'])[0:6], "date": str(bid['date'])[0:10]})
            if bid['price'] == 'market_price':
                bid['price'] = (float(item["high"]) + float(item["low"])) * 0.5
                return self.market_make_deal(bid, client)
            elif (float(bid['price']) < float(item["high"]) and float(bid['price']) > float(item["low"]) or float(bid['price']) == float(item["low"]) or float(bid['price']) == float(item['high'])) and float(bid['amount']) < float(item['volume']) / 8:
                #QA_util_log_info("deal success")
                message = {
                    'header': {
                        'source': 'market',
                        'status': 200,
                        'code': str(bid['code']),
                        'session': {
                            'user': str(bid['user']),
                            'strategy': str(bid['strategy'])
                        },
                        'order_id': str(bid['order_id']),
                        'trade_id': str(random.random())
                    },
                    'body': {
                        'bid': {
                            'price': str(bid['price']),
                            'code': str(bid['code']),
                            'amount': int(bid['amount']),
                            'date': str(bid['date']),
                            'towards': bid['towards']
                        },
                        'market': {
                            'open': item['open'],
                            'high': item['high'],
                            'low': item['low'],
                            'close': item['close'],
                            'volume': item['volume'],
                            'code': item['code']
                        },
                        'fee': {
                            'commission': 0.002 * float(bid['price']) * float(bid['amount'])
                        }
                    }
                }

                # QA_signal_send(message,client)
            # print(message['body']['bid']['amount'])
                return message
            else:
               # QA_util_log_info('not success')
                if int(bid['price']) == 0:
                    status_mes = 401
                else:
                    status_mes = 402

                message = {
                    'header': {
                        'source': 'market',
                        'status': status_mes,
                        'code': str(bid['code']),
                        'session': {
                            'user': str(bid['user']),
                            'strategy': str(bid['strategy'])
                        },
                        'order_id': str(bid['order_id']),
                        'trade_id': str(random.random())
                    },
                    'body': {
                        'bid': {
                            'price': '',
                            'code': str(bid['code']),
                            'amount': int(bid['amount']),
                            'date': str(bid['date']),
                            'towards': bid['towards']
                        },
                        'market': {
                            'open': item['open'],
                            'high': item['high'],
                            'low': item['low'],
                            'close': item['close'],
                            'volume': item['volume'],
                            'code': item['code']
                        }
                    }
                }
            # print(message['body']['bid']['amount'])
                return message
        except:
            ##QA_util_log_info('no market data')
            message = {
                'header': {
                    'source': 'market',
                    'status': 500,
                    'code': str(bid['code']),
                    'session': {
                        'user': str(bid['user']),
                        'strategy': str(bid['strategy'])
                    },
                    'order_id': str(bid['order_id']),
                    'trade_id': str(random.random())
                },
                'body': {
                    'bid': {
                        'price': str(bid['price']),
                        'code': str(bid['code']),
                        'amount': int(bid['amount']),
                        'date': str(bid['date']),
                        'towards': bid['towards']
                    },
                    'market': {
                        'open': 0,
                        'high': 0,
                        'low': 0,
                        'close': 0,
                        'volume': 0,
                        'code': 0
                    }
                }
            }
            return message
