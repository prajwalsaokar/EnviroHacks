import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time
import os
import os
from fbprophet import prophet
os.environ["PROJ_LIB"] = "C:\\Users\\prajw\\Anaconda3\\pkgs\\proj4-5.2.0-h6538335_1006\\Library\\share";

ts= []
df = pd.read_csv("database.csv")

df = df[['Date', 'Time', 'Latitude', 'Longitude', 'Depth', 'Magnitude']]
df["Datetime"] = df['Date'] + ' ' + df["Time"]
df.drop(index=0, inplace=True)

dt = df["Datetime"]
y=0
for x in dt: 
   ts.append(datetime.datetime.strptime(x, '%m/%d/%Y  %H:%M:%S'))
   ts[y]= ts[y].timestamp()
   y+=1

df['Timestamp'] = pd.Series(ts)
df.drop(index=21952, inplace=True)
feature_data  = df[['Latitude', "Longitude", "Depth", "Magnitude", "Timestamp"]]

from mpl_toolkits.basemap import Basemap

m = Basemap(projection='mill',llcrnrlat=-80,urcrnrlat=80, llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')

longitudes = df["Longitude"].tolist()
latitudes =df["Latitude"].tolist()

x,y = m(longitudes,latitudes)
fig = plt.figure(figsize=(12,10))
plt.title("All affected areas")
m.plot(x, y, "o", markersize = 2, color = 'blue')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
m.drawmapboundary()
m.drawcountries()
plt.show()


   
  


   
   

    
    


 
  

    









                                              
