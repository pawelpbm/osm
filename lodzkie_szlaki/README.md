# Opis

Skrypty przeznaczone są do dokonywania konwersji z formatu xls opisującego łódzkie szlaki turystyczne do formatu osm rozpoznawanego przez edytor JOSM. Szczegóły dostępne są w temacie [Szlaki turystyczne woj. łódzkiego](http://forum.openstreetmap.org/viewtopic.php?id=14754). 

Skrypt *lodzkie_szlaki_to_osm.py* konwertuje pliki *Karta szlaku*, skrypt *lodzkie_szlaki_to_osm_2.py* powinien obsłużyć pozostałe pliki

# Wymagania

W systemie zainstalowane muszą być:

* [Python 2.7](http://python.org/)
* [biblioteka xlrd](http://pypi.python.org/pypi/xlrd)

# Użycie

## [lodzkie_szlaki_to_osm.py](https://raw.github.com/pawelszubert/osm/master/lodzkie_szlaki/lodzkie_szlaki_to_osm.py)

### Windows

    lodzkie_szlaki_to_osm.py plik.xls

### Linux

    chmod +x lodzkie_szlaki_to_osm.py
    ./lodzkie_szlaki_to_osm.py plik.xls

W wyniku działania skryptu otrzymujemy katalog o nazwie takiej jak przetwarzany plik ze zbiorem plików osm dla każdej z gmin.

## [lodzkie_szlaki_to_osm_2.py](https://raw.github.com/pawelszubert/osm/master/lodzkie_szlaki/lodzkie_szlaki_to_osm_2.py)

Skrypt uruchamiamy dokładnie tak jak poprzedni, jednak przed jego uruchomieniem musimy sprawdzić w której kolumnie pliku xls znajduje się numer id punktu (kolumny liczymy od 0), a następnie otwierając skrypt dowolnym edytorem tekstu ustawić wartość zmiennej *NN*.

W wyniku działania skryptu otrzymujemy katalog o nazwie takiej jak przetwarzany plik z jednym plikiem osm opisującym cały szlak.
