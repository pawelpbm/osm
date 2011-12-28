# Opis

Skrypt *prparser.py* pobiera punkty GPS ze strony Przewozów Regionalnych [http://kursowania.przewozyregionalne.pl/](http://kursowania.przewozyregionalne.pl/) i umieszcza je w bazie sqlite (plik *sqlite.db*).

Skrypt *pr2osm.py* pobiera dane z bazy i konwertuje je do formatu OSM (do pliku *points.osm*).

Plik *index.html* pozwala nałożyć punkty z pliku *points.osm* na warstwę mapy OpenStreetMap lub Google Maps.

**Dane uzyskane ze skryptów nie mogą być importowane do OpenStreetMap, gdyż nie są na wolnej licencji!**


