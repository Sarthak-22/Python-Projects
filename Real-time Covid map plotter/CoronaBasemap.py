import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm
from covid import Covid
 
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

fig,ax = plt.subplots(figsize=(40,40))
m = Basemap(resolution='c',projection='merc',llcrnrlon=-168.7,llcrnrlat=-59.3,urcrnrlon=180,urcrnrlat=78.7)
m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
m.drawcoastlines()
m.drawstates()
m.drawcountries()

covid=Covid()
data=covid.get_data()
lats=list()
longs=list()
cases=list()


for i in range(len(data)):
    lats.append(data[i]['latitude'])
    longs.append(data[i]['longitude'])
    cases.append(data[i]['confirmed'])
        
for i in range(len(data)-2):
    if lats[i]==None:
        lats.pop(i)
        longs.pop(i)
        cases.pop(i)
#print(longs)
#lon,lat = np.meshgrid(longs,lats)
x, y = m(longs, lats)
print(x)
print("")
print(y)
#c_scheme = m.pcolormesh(x,y,cases,cmap='jet')






