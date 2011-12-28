#!/usr/bin/python
import mechanize
import sqlite3
import time

from lxml import html


conn = sqlite3.connect('sqlite.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS "points" ("lat" REAL, "lon" REAL, UNIQUE("lat", "lon") on CONFLICT IGNORE);""")

br = mechanize.Browser()

while True:
    br.open('http://82.160.42.14/opoznienia/')
    page = html.fromstring(br.response().read())
    print("------------new iteration--------------")
    for row in page.xpath('//div[@id="wynik"]//tr//a'):
        lat, lon = row.get('href').split('@')[1].split('&')[0].split(',')
        print("adding {0}, {1}".format(lat, lon))
        c.execute("""insert into points values ({0}, {1})""".format(lat, lon))
    conn.commit()
    time.sleep(30)
    
c.close()
