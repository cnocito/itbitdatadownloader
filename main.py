from itbit_api import itBitApiConnection
import json
import time
import pymysql

class tradingDB:
    def __init__(self,host='127.0.0.1'):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='bitcoin_trader')

    def viewTrades(self):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT * FROM trade;
        """)
        result = cur.fetchall()
        cur.close()
        return result

    def insertTicker(self,symbol,bid,volume24,low24,lastPrice,askAmt,vwapToday,volumeToday,ask,lastAmt,high24h,
                    vwap24h,lowToday,highToday,serverTimeUTC,bidAmt,openToday):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO `bitcoin_trader`.`ticker`
                (
                `symbol`,
                `bid`,
                `volume24`,
                `low24`,
                `lastPrice`,
                `askAmt`,
                `vwapToday`,
                `volumeToday`,
                `ask`,
                `lastAmt`,
                `high24h`,
                `vwap24h`,
                `lowToday`,
                `highToday`,
                `serverTimeUTC`,
                `bidAmt`,
                `openToday`)
                VALUES
                (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s);
            """,list((symbol,bid,volume24,low24,lastPrice,askAmt,vwapToday,volumeToday,ask,lastAmt,high24h,vwap24h,lowToday,highToday,serverTimeUTC,bidAmt,openToday)))
            self.conn.commit()
            return 1
        except pymysql.MySQLError as e:
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))

    def insertTrade(self,matchnumber,timestamp,amount,price):
        try:
            cur = self.conn.cursor()
            cur.execute("""INSERT INTO trade(matchnumber,timestamp,amount,price) VALUES(%s,%s,%s,%s)""",list((matchnumber,timestamp,amount,price)))
            self.conn.commit()
            return 1
        except pymysql.MySQLError as e:
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))


class itBitTrader:
    clientKey = ''
    secretKey = ''
    userId = ''

    def __init__(self,clientKey,secretKey,userId):
        self.clientKey = clientKey
        self.secretKey = secretKey
        self.userId = userId
        self.apiConn = itBitApiConnection(clientKey=self.clientKey, secret=self.secretKey, userId=self.userId)

def sampleData(trader,db):
    symbols = ['XBTUSD','XBTEUR','XBTSGD']
    for symbol in symbols:
        ticker = trader.apiConn.get_ticker(symbol).json()
        db.insertTicker(ticker['pair'],ticker['bid'],ticker['volume24h'],ticker['low24h'],ticker['lastPrice'],ticker['askAmt'],ticker['vwapToday'],
                    ticker['volumeToday'],ticker['ask'],ticker['lastAmt'],ticker['high24h'],ticker['vwap24h'],ticker['lowToday'],ticker['highToday'],
                    ticker['serverTimeUTC'],ticker['bidAmt'],ticker['openToday'])

    trades = trader.apiConn.get_trades('XBTUSD').json()
    for trade in trades['recentTrades']:
        db.insertTrade(str(trade['matchNumber']).strip(' \t\n\r'),str(trade['timestamp']).strip(' \t\n\r'),str(trade['amount']).strip(' \t\n\r'),str(trade['price']).strip(' \t\n\r'))

trader = itBitTrader('','','')
db = tradingDB()

while True:
    try:
        sampleData(trader,db)
    except Exception:
        print('Unable to sample data!')
    time.sleep(10)