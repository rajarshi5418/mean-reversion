import pandas as pd

df = pd.read_csv(r'nifty.csv')
nfty  = df["NIFTY 50"].tolist()

nifty_50=[]

def nifty():
    for i in nfty:
        nse = ".NS"
        stk = str(i) + nse
        nifty_50.append(stk)

    nifty_50.pop(-1)
    print(nifty_50)
    return nifty_50

nifty()