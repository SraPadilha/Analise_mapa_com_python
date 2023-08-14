import osmnx
import folium

coordenadas = [
  (-27.595405862036344, -48.55128898304735),
  (-27.59600680294117, -48.55192467417698),
  (-27.596745924329053, -48.55247215576605),
  (-27.59598632580152, -48.550608076922146),
  (-27.596602328956163, -48.55098103392928),
  (-27.597180019512916, -48.551647357933746),
  (-27.59617867797671, -48.54992360707304),
  (-27.596948930938915, -48.55030021028882),
  (-27.59760364873307, -48.550865133049875)
]

    lats, lons = zip(*coordenadas)
    norte, sul = max(lats), min(lats)
    leste, oeste = max(lons), min(lons)

    mapa = folium.Map(location=[(norte + sul) / 2, (leste + oeste) / 2], zoom_start=16, tiles='Stamen Terrain')

        for i, (lat, lon) in enumerate(coordenadas, 1):
            trees = ox.geometries_from_point((lat, lon), dist=130, tags={'natural': 'tree'})
            quantidade_arvores = len(trees)

    folium.Marker(
          location=[lat, lon],
          popup=f"Coordenada {i}\nQuantidade de Árvores: {quantidade_arvores}",
          icon=folium.Icon(icon='cloud')
      ).add_to(mapa)

    buildings = ox.geometries_from_point((lat, lon), dist=35, tags={'building': True})

    folium.GeoJson(buildings, style_function=lambda x: {'fillOpacity': 0, 'color': 'blue'}).add_to(mapa)


    mapa