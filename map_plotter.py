import folium
from folium import plugins
import os
import time
from selenium import webdriver
import location_matcher as lm


def heatmap(lats,lons,weights,map_tile = None):
    lat, lon = lm.calcCentrePoint(lats,lons)
    if map_tile is None:
        m = folium.Map(location=[lat,lon], zoom_start=15,control_scale = True)
    else:
        m = folium.Map(location=[lat,lon], zoom_start=15,control_scale = True,tiles=map_tile)

# I am using the magnitude as the weight for the heatmap
    m.add_child(plugins.HeatMap(zip(d_cor['lat'].tolist(), d_cor['lon'].tolist(), d_cor['manifest_count'].tolist()), radius = 10))
    return m

## drop the empty lat lon in dataframe
def drop_empty_latlon(df):
    df['lon'].replace('', np.nan, inplace=True)
    df['lat'].replace('', np.nan, inplace=True)
    df.dropna(subset=['lon'], inplace=True)
    return df

##adapted from https://github.com/python-visualization/folium/issues/35#issuecomment-164784086
def save_to_png(mapfile):
    delay=5
    fn= mapfile
    tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile)
    m.save(fn)
    browser = webdriver.Firefox()
    browser.get(tmpurl)
    #Give the map tiles some time to load
    time.sleep(delay)
    browser.save_screenshot('map.png')
    browser.quit()
