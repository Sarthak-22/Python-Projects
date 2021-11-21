import requests
import pandas as pd                              #Including Pandas library
import geopandas as gpd                          #Including geopandas library
url='https://www.worldometers.info/coronavirus/' #Website from which active Covid-19 world data is taken.
corona_url=requests.get(url)
corona_url

data = pd.read_html(corona_url.text)[0]          #Extracting info from the website to make a pandas dataframe (currently 241rows*12 columns)
    
cases_new = data[['Country,Other', 'TotalCases' ]] #Cropping the dataframe to extract only two required columns

#A shapefile (.shp) of worldmap is downloaded from the internet and converted to geopandas geodataframe to visulaize it on the map
data_world = gpd.read_file(r'C:\Users\Sarthak Vora\Downloads\Covid cases\World_Map.shp') 
#print(data_world)                                                                

# Now, we have a pandas dataframe 'cases_new' and a geopandas dataframe 'data_world'.However there might be a possibility that the name of a #particular country does not match in both the dataframes as they are taken from different sources.

#Hence, the following code block finds the countries whose name is different in both the dataframes, by converting both the dataframes first to 'list' data structure and iterates through 'cases_new['Country,Other']' list to find the desired output.

flag=0
for countries in cases_new['Country,Other'].tolist():
    world_list = data_world['NAME'].tolist()
    if countries in world_list:
        pass
    else:
        print(countries ) #To show the country names which do match in both the tables
        flag=flag+1
print(flag)

#There are around 30 entries which do not match in both the dataframes including union territories,islands etc
#The names of countries, different in both the dataframes, are individually replaced below in 'data_world' dataframe 
#Most of the entries have been replaced excluding some islands and union territories

data_world.replace('Korea, Republic of', 'S. Korea', inplace = True)
data_world.replace('Iran (Islamic Republic of)', 'Iran', inplace = True)
data_world.replace('United States', 'USA', inplace = True)
data_world.replace('United Kingdom', 'UK', inplace = True)
data_world.replace('United Arab Emirates', 'UAE', inplace = True)
data_world.replace('Viet Nam', 'Vietnam', inplace = True)
data_world.replace('Macau', 'Macao', inplace = True)
data_world.replace('The former Yugoslav Republic of Macedonia', 'North Macedonia', inplace = True)
data_world.replace('Czech Republic', 'Czechia', inplace = True)
data_world.replace('United Republic of Tanzania','Tanzania',inplace=True)
data_world.replace('Burma','Myanmar',inplace=True)
data_world.replace('Libyan Arab Jamahiriya','Libya',inplace=True)
data_world.replace('Republic of Moldova','Moldova',inplace=True)
data_world.replace('Cote d\'Ivoire','Ivory Coast',inplace=True)
data_world.replace('Democratic Republic of the Congo','DRC',inplace=True)
data_world.replace('Brunei Darussalam','Brunei',inplace=True)
data_world.replace('Syrian Arab Republic','Syria',inplace=True)
data_world.replace('Lao People\'s Democratic Republic','Laos',inplace=True)
data_world.replace('Swaziland','Eswatini',inplace=True)
data_world.replace('United Republic of Tanzania','Tanzania',inplace=True)

# Renaming the columnname, so that both the dataframes have same columnname which includes name of all the countries.

cases_new.rename(columns = {'Country,Other': 'NAME'}, inplace = True)

#Merging the pandas and geopandas dataframe on the geopandas dataframe to create a new geopandas dataframe whose one column consists of the geometry of all the countries(used to visualize on the map) and the other column consists of the total cases pertaining to that country.

merge_data = data_world.merge(cases_new , on='NAME')

#print(merge_data)

merge_data.to_file(r'C:\Users\Sarthak Vora\Downloads\Covid cases\dataplot.shp')

#The geopandas dataframe can be saved in a desired location in the PC in the form of a shapefile.
#The shapefile is then visualised in'ArcGis' software.
