# -*-coding:utf-8 -*
# Laurent VOLFF
# 09/06/2016
# macd

def macd(mme12,mme26):
    return mme12 - mme26

if __name__=='__main__':
    mme12 = 49.2181469231
    mme26 = 48.6909814815
    print '{}'.format(macd(mme12,mme26))

