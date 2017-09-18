from pygal_maps_world.maps import World
import json
from pygal.style import RotateStyle, LightColorizedStyle

countries = {}
countries['<=100000'] = {}
countries['<=200000'] = {}
countries['<=300000'] = {}
countries['<=400000'] = {}
countries['>400000'] = {}
with open('data/country.csv') as f:
    data = json.load(f)
    for jdict in data:
        num = int(jdict['num'])
        code = str(jdict['code']).strip()

        if num <= 100000:
            countries['<=100000'][code] = num
        elif num <= 200000:
            countries['<=200000'][code] = num
        elif num <= 300000:
            countries['<=300000'][code] = num
        elif num <= 400000:
            countries['<=400000'][code] = num

wm_style = RotateStyle('#336699')
wm = World(style=wm_style, base_style=LightColorizedStyle)
wm.title = 'THE A'
for k, v in countries.items():
    wm.add(k, v)
wm.render_to_file('americas.svg')
