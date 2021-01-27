# Program to use Currency conversion API
# Created by Alex Amato
# WORK IN PROGRESS

import cmath
import requests
import json
import matplotlib.pyplot as plt
import numpy


#url = "https://api.ratesapi.io/api/latest"
#url = "https://data.fixer.io/api/latest"
# url = "https://api.exchangeratesapi.io/latest"
url = "https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&symbols=GBP"

responseStatus = requests.get(url)
response = responseStatus.json()

print(len(response['rates']))

#print(len(response['rates']))
#print(response['rates'])

dates = []
eur2gbp = []

for i in response['rates']:
    #print(response['rates'][i]['GBP'])
    dates.append(i)
    eur2gbp.append(response['rates'][i]['GBP'])
    
#Sorts two arrays by 1 array
eur2gbp = [x for _,x in sorted(zip(dates,eur2gbp))]
dates.sort()

for i in range(len(dates)):
    print(str(dates[i]) + ": " + str(eur2gbp[i]))


# print(dates)
# print(Z)
# print(eur2gbp)

plt.plot(dates, eur2gbp)
plt.show()