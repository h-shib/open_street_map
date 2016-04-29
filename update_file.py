#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = ["version", "changeset", "timestamp", "user", "uid"]


def set_pos(node, element, a):
    if 'pos' not in node:
        node['pos'] = [0, 0]
    if a == 'lat':
        node['pos'][0] = float(element.attrib[a])
    elif a == 'lon':
        node['pos'][1] = float(element.attrib[a])
    return node


def update_value(key, value):
    if key == 'postcode':
        value = value.replace("-", "")
    return value


def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way":
        node['type'] = element.tag
        # for first level node
        for a in element.attrib:
            if a == 'lat' or a == 'lon':
                node = set_pos(node, element, a)
            elif a in CREATED:
                if 'created' not in node:
                    node['created'] = {}
                node['created'][a] = element.attrib[a]
            else:
                node[a] = element.attrib[a]
        # for second level node
        for child in element.getchildren():
            if child.tag == 'nd':
                if 'node_refs' not in node:
                    node['node_refs'] = []
                node['node_refs'].append(child.attrib['ref'])
            else:
                if problemchars.match(child.attrib['k']):
                    continue
                elif child.attrib['k'][0:5] == 'addr:' and not len(child.attrib['k'].split(':')) > 2:
                    if 'address' not in node:
                        node['address'] = {}
                    key = child.attrib['k'].split(':')[1]
                    node['address'][key] = update_value(key, child.attrib['v'])
        return node
    else:
        return None


def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                    print len(data)
                else:
                    fo.write(json.dumps(el) + "\n")
                    print len(data)
    return data

if __name__ == "__main__":
    process_map('sendai_japan.osm', True)
