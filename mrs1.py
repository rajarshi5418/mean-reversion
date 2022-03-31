# from nifty_stock_list import*
import talib
import pandas_datareader.data as pdr
from talib import abstract
import datetime
from datetime import timedelta, date
from pandas import DataFrame
import pandas as pd
from pynse import*



# nfty_50 = nifty()
nse = Nse()

# print(nse.bhavcopy_fno(req_date=datetime.date(2022, 3, 7)))

data = nse.bhavcopy_fno()
# print(data)

data2=data.index.to_list()
list1=set(data2)
print(list1)
print(len(list1))

mean_rev_list=[]
enddate=date.today()
startdate=enddate-timedelta(300)
count = 0
for stk in list1:
    count=count+1
    # print(count,stk)
    try:
        ohlcv = nse.get_hist(stk, startdate,enddate)
        # print(ohlcv)
        rsi = abstract.RSI(ohlcv,2)
        ohlcv['rsi']=rsi

        ohlcv['MA'] = ohlcv['close'].rolling(window=200).mean()
        # print(ohlcv)

        per_change=(ohlcv['close'].iloc[-1]-ohlcv['close'].iloc[-2])/ohlcv['close'].iloc[-1]*100
        # print(per_change)
        if ohlcv['MA'].iloc[-1]<ohlcv['close'].iloc[-1]:
            if ohlcv['rsi'].iloc[-1]>50:
                if per_change>3:
                    print(count, stk, "stock found")
                    # print(ohlcv)
                    # print(per_change)
                    # print(ohlcv['close'].iloc[-1])
                    # print(ohlcv['MA'].iloc[-1])
                    # print(ohlcv['rsi'].iloc[-1])
                    mean_rev_list.append(stk)
    except ValueError or AttributeError:
        print("sorry")

print(mean_rev_list)

startdate_5d=enddate-timedelta(10)

short_list={}
for stk_mrs in mean_rev_list:

    print(stk_mrs)

    ohlcv = nse.get_hist(stk_mrs, startdate,enddate)

    per_change_5d = (ohlcv['close'].iloc[-1] - ohlcv['close'].iloc[-5]) / ohlcv['close'].iloc[-1] * 100
    print(stk_mrs,per_change_5d)

    short_list[stk_mrs]=per_change_5d

print(short_list)
print(dict(sorted(short_list.items(), key=lambda item: item[1])))
short_list=dict(sorted(short_list.items(), key=lambda item: item[1], reverse=True))

for i in short_list:
    print(i,"\t\t",short_list[i])
    data = nse.get_quote(i)
    close = data["close"]
    print("quantity", 30000/close)
    print("entry", close * 1.01)
    print("stop loss", close * 1.03)
    print("exit", (close * .94))



