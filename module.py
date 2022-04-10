import requests
from datetime import datetime
import pandas as pd

def getData(ticker, start, end):
    data = []
    date = []
    quot = []
    last_date = start

    d1 = datetime.strptime(start, '%Y-%m-%d')
    d2 = datetime.strptime(end, '%Y-%m-%d')
    res = pd.date_range(d1, d2).strftime('%Y-%m-%d').tolist()
    for i in res:
        data.append([i, None])

    while last_date < end:
        last_date = start
        kat = requests.get('https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/' +
                       ticker + '.json?from=' + start + '&till=' + end + '&history.columns=TRADEDATE,OPEN&iss.meta=off')
        for i in range(len(kat.json()["history"]["data"])):
            date.append(kat.json()["history"]["data"][i][0])
            quot.append(kat.json()["history"]["data"][i][1])
        start = kat.json()["history"]["data"][-1][0]
        if start == last_date:
            del date[-1]
            del quot[-1]
            break
    for i in range(len(data)):
        for j in range(len(date)):
            if data[i][0] == date[j]:
                data[i][1] = quot[j]
    for i in range(len(data)):
        quot.append(data[i][1])
    return quot



