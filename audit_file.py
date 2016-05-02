#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint

# count each postal code
def audit_postal_code(filename):
    postal_codes = {}
    for _, element in ET.iterparse(filename):
        if element.tag == "tag":
            if "postcode" in element.attrib["k"]:
                if element.attrib["v"] not in postal_codes:
                    postal_codes[element.attrib["v"]] = 1
                else:
                    postal_codes[element.attrib["v"]] += 1
    return postal_codes


def audit_way(filename):
    ways = {}
    for _, element in ET.iterparse(filename):
        if element.tag == "way":
            for tag in element.iter("tag"):
                if tag.attrib["k"] not in ways:
                    ways[tag.attrib["k"]] = 1
                else:
                    ways[tag.attrib["k"]] += 1
    return ways


def audit_user(filename):
    users = {}
    for _, element in ET.iterparse(filename):
        if "user" in element.attrib:
            if element.attrib["user"] not in users:
                users[element.attrib["user"]] = 1
            else:
               users[element.attrib["user"]] += 1
    return users


def audit_tag(filename):
    tags = {}
    for _, element in ET.iterparse(filename):
        if element.tag not in tags:
            tags[element.tag] = 1
        else:
            tags[element.tag] += 1
    return tags


def audit_member(filename):
    members = {}
    for _, element in ET.iterparse(filename):
        if element.tag == "member":
            if element.attrib["ref"] not in members:
                members[element.attrib["ref"]] = 1
            else:
                members[element.attrib["ref"]] += 1
    return members

def audit():
    postal_codes = audit_postal_code('sendai_japan.osm')
    #ways = audit_way('sendai_japan.osm')
    #users = audit_user('sendai_japan.osm')
    #tags = audit_tag('sendai_japan.osm')
    #members = audit_member('sendai_japan.osm')
    pprint.pprint(postal_codes)
    print len(postal_codes)


if __name__ == "__main__":
    audit()