# webscrapping

## Plebiscito constitucional constituyente

Dado que la página del servel para acceder al resultado individual de cada una de las mesas requiere de un "click" para llegar (como una especie de embudo), es que 
utilicé Selenium con el webdriver para poder guiarme con las interacciones, utilizando un delay de la query de 0.3 segundos entre cada uno (lo mínimo que se demoraba mi pc en recargar la página). El embudo es de alrededor de 5 alternativas de múltiple elección: Región, Comuna, Circunscripción, Local y Mesa.

Con el código anterior, se puede recabar los votos por el Apruebo, Rechazo, Nulos, Blancos y Total para cada una de las mesas. No obstante, hasta el momento está implementado solamente para printear el resultado y no incorporarlo en una base de datos propiamente tal, como se podría hacer con **pandas** u otros paquetes.
