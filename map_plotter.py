import folium
from folium import plugins



def heatmap(lats,lons,weights):
    m = folium.Map(location=[0.1514, 51.5144], zoom_start=15,control_scale = True)

# I am using the magnitude as the weight for the heatmap
    m.add_child(plugins.HeatMap(zip(d_cor['lat'].tolist(), d_cor['lon'].tolist(), d_cor['manifest_count'].tolist()), radius = 10))
    return m
