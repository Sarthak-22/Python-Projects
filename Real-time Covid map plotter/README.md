## Problem Statement 
Generate a **heat map** on the world map indicating the **live data** of the number of **cases of 
coronavirus** in each country. 

## Approach
* Since this problem statement deals with real-time updating of world map, I used a [Basemap](https://mayurmgaikwad.wordpress.com/2018/11/18/india-map-visualization-python-and-basemap/) for map visualisation. A basemap package eases the access of geographical locations on a world map when combined with geopandas package.
* Further, a software named **ArcGis** was installed which has an app called **ArcMap**. ArcMap can read a _shapefile_(.shp) and visualize it to make the desired modification.
* A shapefile (_World_map.shp_) needs to be downloaded from internet. The 'Geopandas' package was also used since it allows us to access geographical coordinates in a map by converting the map to a geopandas dataframe.
* The live Covid-19 cases were accessed from the site 'https://www.worldometers.info/coronavirus/'. Pandas dataframe was used to parse and clean the data from the website.
* Finally, the data from pandas dataframe was combined(/merged) with Geopandas dataframe for world map visualization and converted again to a new shapefile (_dataplot.shp_+)

## How to plot the map ?
* The shapefile _dataplot.shp_ is fed to the software. The graduated colours throughout the map, which varies with the total number of cases, can be set by modifying the properties of the map.
* The dataplot in the map in the software will keep on updating by hitting the refresh button, as and when the information on the site is updated.
* Some of the countries in the map might be ‘uncoloured’ (especially in Africa). This is either due to no active cases present in these countries/regions or the data entry of these countries/regions might not be updated in the website from which information is taken.

#### The complete procedure of the creation of the map using the ArcGis map software can be seen in the linked [video](https://drive.google.com/file/d/12TBUueaU31_4shZEf9CgblZws1qpZuPM/view) 

### The final map visualization (as of 12th April 2020) from ArcGis can be seen below - 
![image](https://github.com/Sarthak-22/Python-Projects/blob/main/Real-time%20Covid%20map%20plotter/Coronavirus%20world%20plot.jpg)



