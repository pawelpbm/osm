#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import xlrd
import os

NN = 3

def is_float(element):
    try:
        float(element)
    except ValueError:
        return False

    return True

def row_type(sh, row):
    """
    0 - empty
    1 - first line of point
    2 - second line of point
    3 - path
    4 - summary
    """

    if is_float(sh.row_values(row)[NN]):
        return 1

    if len(sh.row_values(row)[NN].split('-')) == 2:
        return 3

    if row == sh.nrows - 1:
        return 4

    return 0

def print_osm_header():
    return """<?xml version='1.0' encoding='UTF-8'?>
    <osm version='0.6' generator='JOSM'>
    """

def print_osm_footer():
    return "</osm>"


def get_file_for_sheet(path, name):
    p, n = os.path.split(path)
    if not p:
        p = os.getcwd()

    n, _ = os.path.splitext(n)
    directory = os.path.join(p, n)
    if not os.path.exists(directory):
        os.mkdir(directory)
    return open(os.path.join(directory, name + ".osm"), 'w')

def convert_to_dd(d, m, s):
    d = d.replace(',', '.')
    d = d.replace('\'', '')
    d = d.replace('\"', '')
    m = m.replace(',', '.')
    m = m.replace('\'', '')
    m = m.replace('\"', '')
    s = s.replace(',', '.')
    s = s.replace('\'', '')
    s = s.replace('\"', '')
    return float(float(d) + float(m) / 60 + float(s) / 3600)

def get_lat_lon(sh, row):
    coord =  sh.row_values(row)[NN+2].split()
    lat = convert_to_dd(coord[0].split('-')[1], coord[1], coord[2])
    lon = convert_to_dd(coord[3].split('-')[1], coord[4], coord[5])
    return lat, lon

def get_desc(sh, row):
    return sh.row_values(row)[NN+1].replace('"', "")

def get_shelter(sh, row):
    return sh.row_values(row)[NN+24]

def get_bike_parking(sh, row):
    return sh.row_values(row)[NN+25] or sh.row_values(row)[NN+26]

def get_surface(sh, row):
    SURFACES = {'bit': 'asphalt', 'tł': 'compacted', 'bruk': 'paving_stones', 'gu': 'compacted', 'gn': 'ground',  'bet': 'concrete', 'kk': 'paving_stones', 'kam': 'gravel'}

    surfaces = []
    for s in sh.row_values(row)[NN+6].split():
        surfaces.append(SURFACES[s])
    return surfaces

def get_node_number(sh, row):
    return -int(sh.row_values(row)[NN])

def get_path_number(sh, row):
    return -int('10' + sh.row_values(row)[NN].replace("-", ""))

def get_nodes_in_path(sh, row):
    a, b = sh.row_values(row)[NN].split('-')
    return -int(a), -int(b)
        
if __name__ == '__main__':

    xls_file_path = sys.argv[1]
    
    xls_file = xlrd.open_workbook(xls_file_path)

    sh = xls_file.sheets()[0]
    f = get_file_for_sheet(xls_file_path, sh.name)
    f.write(print_osm_header())

    nodes = []
    paths = []

    
    for row in range(0, sh.nrows):
        t = row_type(sh, row)
        if t == 1:
            nodes.append(row)
        elif t == 3:
            paths.append(row)

    for node in nodes:
        lat, lon = get_lat_lon(sh, node)
        f.write('<node id="{0}" lat="{1}" lon="{2}" visible="true">\n'.format(get_node_number(sh, node), lat, lon))
        f.write(u'<tag k="name" v="{0}"/>\n'.format(get_desc(sh, node)).encode('utf-8'))
        if get_shelter(sh, node):
            f.write('<tag k="amenity" v="shelter"/>\n')
            f.write('<tag k="shelter_type" v="weather_shelter"/>\n')

        if get_bike_parking(sh, node):
            f.write('<tag k="amenity" v="bicycle_parking"/>\n')
            
        f.write('</node>\n')
        
    for path in paths:
        f.write('<way id="{0}" visible="true">\n'.format(get_path_number(sh, path)))
        for n in get_nodes_in_path(sh, path):
            f.write('<nd ref="{0}"/>\n'.format(n))

        f.write('<tag k="highway" v="road"/>\n')
        f.write(u'<tag k="name" v="{0}"/>\n'.format(get_desc(sh, path)).encode('utf-8'))
            
        for s in get_surface(sh, path):
            f.write('<tag k="surface" v="{0}"/>\n'.format(s))
        f.write('</way>\n')
    f.write(print_osm_footer())
    f.close()
