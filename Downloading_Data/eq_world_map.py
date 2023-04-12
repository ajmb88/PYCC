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

mags, lons, lats, titles,  = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    titles.append(eq_dict['properties']['title'])
    

# map the earthquakes
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker' : {
        'size' : [3.7*mag for mag in mags],
        'color' : mags,
        'colorscale' : 'Earth',
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'},
        'symbol' : 'diamond',
    },
}]
my_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')