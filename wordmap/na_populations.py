import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'Populations of Countries'
wm.add('Noth Americal',{'ca':321210,'us':249349392,'mx':1134992})
wm.render_to_file('./wordmap/americas_populations.svg')