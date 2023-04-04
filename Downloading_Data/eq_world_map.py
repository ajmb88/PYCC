import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'Downloading_Data/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'Downloading_Data/data/New_Json_Files/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)


all_eq_dicts = all_eq_data['features']

mags, lons, lats= [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# map the earthquakes
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker' : {
        'size' : [7.3*mag for mag in mags],
        'color' : mags,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'},
        'symbol' : 'diamond',
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')