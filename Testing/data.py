#import packages 
import pandas as pd
from io import StringIO
import matplotlib as plt
import datetime

#file paths
flow_sch = "C:/Users/Ahmed Bazina/OneDrive/Documents/Information-of-Bees-Dissertation/Kaggle data/Schwartau/flow_schwartau.csv"
temperature_sch = "C:/Users/Ahmed Bazina/OneDrive/Documents/Information-of-Bees-Dissertation/Kaggle data/Schwartau/temperature_schwartau.csv"

#The mean per hour() method accepts the files as an argument and organises the data by day.
#groups data per day: sum of flow and mean temperature, weight and humidity

def DataPerDay(datafile):
    name = str(datafile)
    datafile = pd.read_csv(datafile, sep=',', decimal=".")
    datafile['timestamp'] = pd.to_datetime(datafile['timestamp'])
    datafile.sort_values(by="timestamp")  #sort values by date
    datafile.set_index('timestamp', inplace=True) #date as index
    #if file contains flow then group and sum it otherwise group and mean the rest of files and if Nan is found fill value with data from previous day
    print(name)
    if "flow" in name: 
        datafile = datafile.groupby(pd.Grouper(freq='D')).sum() 
        datafile.ffill()
    else: 
        datafile = datafile.groupby(pd.Grouper(freq='D')).mean() 
        datafile.ffill()
    return datafile 

#calling DataPerDay function on the input files
flow_sch = DataPerDay(flow_sch)
temperature_sch = DataPerDay(temperature_sch)
weight_sch = DataPerDay(weight_sch)
humidity_sch = DataPerDay(humidity_sch)


