# -*-coding:utf-8 -*
# Laurent VOLFF
# 14/06/2016
# rsi

def rsi(cotation):
    '''
     Plus d'info sur le calcul d'une RSI
     http://www.edubourse.com/guide-bourse/rsi.php
     parametre cotation : liste des cotations sur x jours
    '''
    i = len(cotation) - 1
    hausse = []
    baisse = []

    while i:
        x = cotation[i] - cotation[i - 1]
        i = i - 1
        if x > 0:
            hausse.append(x)
        else:
            baisse.append(abs(x))

    H = sum(hausse)/float(len(cotation))
    B = sum(baisse)/float(len(cotation))

    RSI = 100 - (100/(1+(H/B)))

    return RSI

if __name__=='__main__':
    # 9 valeurs
    cotation = [252,257,258,265,272,268,265,267,272,298,300,600]
    print('RSI = {}'.format(rsi(cotation)))
