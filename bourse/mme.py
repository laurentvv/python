# -*-coding:utf-8 -*
# Laurent VOLFF
# 09/06/2016
# mme

def mme(periode,mme_veille,cours_actuel):
    '''

     MME = MME[n-1] + (2/(Période + 1)) * (Cours[n] - MME[n-1])

       Où

      MME[n-1] — est la valeur de la moyenne mobile de la veille : mme_veille
      Cours[n] — est le cours de clôture du jour : cours_actuel
      (2/(Période + 1)) — est le pourcentage exponentiel, qui dépend de la période de calcul de la moyenne mobile.
      
      Il en résulte que la dernière cotation sera beaucoup plus importante que la plus ancienne valeur prise en
      compte dans le calcul. De même, plus la période de calcul est importante et moins les données anciennes
      sont prises en compte
      
    '''
    return mme_veille + ( 2.0 /( periode + 1 )) * (cours_actuel - mme_veille)

if __name__=='__main__':
    periode = 26
    mme_veille = 48.74986
    cours_actuel = 47.955
    print '{}'.format(mme(periode,mme_veille,cours_actuel))
