import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'Norht, Cetral, and South America'
wm.add('North America',['ca','mx','us'])
wm.add('Central Amierical',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South Amirical',['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ev'])
wm.render_to_file('./wordmap/americas.svg')