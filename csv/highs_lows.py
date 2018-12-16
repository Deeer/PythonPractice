import matplotlib.pyplot as plt
import csv 
from datetime import datetime



filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs= [], []

    for row in reader:
         current_date= datetime.strptime(row[0], '%Y-%m-%d')
         dates.append(current_date)

         high = int(row[1])
         highs.append(high)

    # for index, colum_header in  enumerate(header_row):
    #     print(index,colum_header)

    # hights = []
    # for row in reader: 
    #         hight = int(row[1])
    #         hights.append(hight)

    fig = plt.figure(dpi=128, figsize = (10,6))
    plt.plot(dates,highs, c='red')

    plt.title('Daily high  tempture, july 2014', fontsize = 24)
    plt.xlabel('', fontsize = 15)
    fig.autofmt_xdate()
    plt.ylabel('temptuer(F)', fontsize = 16)
    plt.tick_params(axis='both', which='major', labelsize = 15)
    plt.show()


    print(hights)





