import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

with open('data/4.5_month .geojson',encoding='utf-8') as f:
    all_eq_data = json.load(f)

title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']

mags, lons, lats,hover_texts=[], [], [],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    titles=eq_dict['properties']['title']
    mags.append(mag if mag>0 else 0)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(titles)

#map earthquake
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*int(mag) for mag in mags],
        'color':mags,
        'colorscale':'electric',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'},
    },
}]
my_layout=Layout(title=title)
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')

