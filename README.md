  # Analise_mapa_com_python
  Aqui vai um código autoral onde o programa realiza uma analise em uma area especifica no mapa e fornece algumas informações sobre a área. 
  O projeto esta sendo desenvolvido em parceria com minha irmã que é arquiteta, urbanista pós graduada e já esta fazendo mestrado, Ainda 
  está em teste e em desenvolvimento.
  Caso alguém se interesse pelos servições que ela faz o que consigo passar @RP_construtora
  
  
Instalação das bibliotecas osmnx e folium.
A biblioteca osmnx é utilizada para obter, modelar, analisar e visualizar dados de rede de ruas,
além de dados de outros elementos geográficos presentes no OpenStreetMap, que é um projeto de mapeamento colaborativo
para criar um mapa livre e editável do mundo, incluindo edifícios, praças, rios, parques, entre outros.
A OSM oferece uma API gratuita, porém, em troca, pode não fornecer a melhor qualidade possível de um mapa.
Existem outras APIs gratuitas disponíveis, mas com um pouco de pesquisa é possível encontrá-las.
A biblioteca folium permite criar mapas interativos em HTML usando o Leaflet,
uma biblioteca JavaScript de código aberto para mapas interativos.
Com o Folium, você pode visualizar dados geográficos em mapas interativos diretamente no navegador.
Ele fornece uma interface fácil de usar para integrar dados geográficos com informações visuais, como marcadores, polígonos,
popups e camadas de informações. Essa biblioteca é realmente útil, especialmente para quem prefere uma interface de marcadores mais sutis.
  
  # Instalação das bibliotecas osmnx e folium.
  
    !pip install osmnx folium --quiet
  
  # Importação das bibliotecas que utilizaremos (sem segredos aqui, são bibliotecas públicas, qualquer um tem acesso)
  
    import folium
    import osmnx as ox
  
  #Coordenadas especificadas 
(Aqui começaram as dificuldades, pois queria uma área grande, mas as coordenadas acabam sendo um
pouco imprecisas, pois não demarcam uma área muito grande. Isso pode ser um problema mais tarde.
Escolha suas coordenadas, pode-se obter essas informações através do Google Maps.)
  
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
  
 # Encontrar as coordenadas extremas 
(Aqui foi basicamente o ajuste para separar as coordenadas acima em norte, sul, leste e oeste,
aplicando o valor máximo e mínimo de cada uma, o que nos ajudará a ter uma leitura de área, em vez de apenas um ponto específico.)
    lats, lons = zip(*coordenadas)   
    norte, sul = max(lats), min(lats)
    leste, oeste = max(lons), min(lons)
  
  # Criar o mapa usando a biblioteca folium, centralizando nas coordenadas médias
(A localização média é calculada a partir das coordenadas extremas (norte, sul, leste e oeste),
garantindo que todas as coordenadas estejam dentro da área visível do mapa. Visualmente é muito melhor e mais confortável.)

    mapa = folium.Map(location=[(norte + sul) / 2, (leste + oeste) / 2], zoom_start=16, tiles='Stamen Terrain')
  
   # Loop para contar a quantidade de árvores em cada coordenada e adicionar marcadores
(Aqui temos as funções que irão fazer a contagem de árvores. Usei um raio grande de 130 metros, o que gera uma porcentagem de erro grande, mas é o menor valor que funcionou após várias tentativas testando diferentes distâncias. Acredito que seja possível diminuir e incluir uma resposta caso não encontre árvores em vez de retornar como erro.)
   
    for i, (lat, lon) in enumerate(coordenadas, 1):
    
# Consulta por raio para obter as árvores ao redor de cada coordenada

     trees = ox.geometries_from_point((lat, lon), dist=130, tags={'natural': 'tree'})
    
# Contar a quantidade de árvores
      quantidade_arvores = len(trees)
  
# Adicionar um marcador com a quantidade de árvores no
# Adicionar um marcador com a quantidade de árvores no mapa
    folium.Marker(
          location=[lat, lon],
          popup=f"Coordenada {i}\nQuantidade de Árvores: {quantidade_arvores}",
          icon=folium.Icon(icon='cloud')
      ).add_to(mapa)
  
# Consulta por raio para obter os edifícios ao redor de cada coordenada
(Mesma lógica da consulta anterior, mas com um raio menor, pois, à medida que aumentamos, pode fugir da área de interesse.
Caso a área em questão seja maior, é possível aumentar o raio ou até mesmo adicionar entrada de dados para facilitar o manuseio,
mas esse não é o foco por enquanto.)

      buildings = ox.geometries_from_point((lat, lon), dist=35, tags={'building': True})
  
# Adicionar os prédios ao mapa como camada GeoJSON, com borda azul e sem preenchimento
(Aqui teremos as formas das construções do mapa, claro que não estará 100% precisa, pois é algo bem difícil de obter.
Você pode procurar em outros locais que têm uma visualização semelhante, e dificilmente estará centralizado.)
      
      folium.GeoJson(buildings, style_function=lambda x: {'fillOpacity': 0, 'color': 'blue'}).add_to(mapa)
  
  # Mostrar o mapa interativo (o mais bonitinho, ver tudo funcionando e poder mexer à vontade no mapa)
      mapa
  
Sim, tenho um código bem melhor que está em desenvolvimento, só quis mostrar o começo deste.
Ele é bom, foi um teste que me retornou muita produtividade, aprendizado e respostas positivas.
O outro está mais completo, só não posso postar ainda. Assim que puder, estará aqui exatamente como este,
com o código e comentários. Para quem não gosta, é só pegar o código e usar à vontade.

  Segue a imagem que esse codigo gera:

  ![image](https://github.com/SraPadilha/Analise_mapa_com_python/assets/110247189/60e3c042-88fd-4855-9181-222e1118f6cf)
