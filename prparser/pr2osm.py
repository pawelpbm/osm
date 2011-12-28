#!/usr/bin/python
import sqlite3
import os

conn = sqlite3.connect('sqlite.db')
c = conn.cursor()

c.execute('select * from points')

p = os.getcwd()
ff = os.path.join(p, "points.osm")

f =  open(ff, 'w')
f.write("""<?xml version='1.0' encoding='UTF-8'?><osm version='0.6' generator='JOSM'>""")

for (i, row) in enumerate(c):
    lat, lon = row
    f.write('<node id="{0}" lat="{1}" lon="{2}" visible="true" />\n'.format(-(i+1), lat, lon))
    
f.write("</osm>")
f.close()
c.close()
