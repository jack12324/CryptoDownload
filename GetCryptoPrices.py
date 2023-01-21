import pandas as pd
import yfinance as yf
import os

# Get Bitcoin data
tic = ['BTC-USD', 'LTC-USD', 'BSV-USD', 'DOGE-USD', 'ETC-USD', 'ETH-USD', 'XTZ-USD', 'XLM-USD', 'ANKR-USD', 'ADA-USD', 'ATOM-USD', 'DOT-USD', 'ALGO-USD', 'SOL-USD', 'SHIB-USD', 'XYO-USD', 'ARPA-USD', 'JASMY-USD', 'GRT6719-USD', 'FET-USD', 'CLV-USD', 'USDT-USD', 'MANA-USD', 'UNI7083-USD', 'SAND-USD']
ticz = ['zzzBTC', 'zzzLTC', 'zzzBSV', 'zzzDOGE', 'zzzETC', 'zzzETH','zzzXTZ', 'zzzXLM', 'zzzANKR', 'zzzADA', 'zzzATOM', 'zzzDOT', 'zzzALGO', 'zzzSOL', 'zzzSHIB', 'zzzXYO', 'zzzARPA', 'zzzJASMY', 'zzzGRT', 'zzzFET', 'zzzCLV', 'zzzUSDT', 'zzzMANA', 'zzzUNI', 'zzzSAND']
data = yf.download(tickers=tic, period = '1mo', interval = '1d', group_by='ticker')

all_frames = []

for i in range(len(tic)):
    csv = data[tic[i]].to_csv("cryptotemp")
    csv = pd.read_csv("cryptotemp")
    csv.pop('Open')
    csv.pop('High')
    csv.pop('Low')
    csv.pop('Adj Close')
    csv.pop('Volume')
    csv.insert(0,'ticker',ticz[i])
    csv = csv[['ticker','Close','Date']]
    for j in range(len(csv['Date'])):
        t = str(csv['Date'][j])
        x = "{}/{}/{}".format(t[5:7], t[8:], t[2:4])
        csv.at[j,'Date'] = x
    all_frames.append(csv)

os.remove("cryptotemp")

final_csv = pd.concat(all_frames, ignore_index=True)
final_csv.to_csv("crypto_price.csv", float_format='%.15f', index=False)

