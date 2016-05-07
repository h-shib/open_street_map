#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint


def audit_tag_key(filename, tag_key):
    """Return list of name and count of tag_key."""
    lists = {}
    for _, element in ET.iterparse(filename):
        if element.tag == "tag":
            if tag_key in element.attrib["k"]:
                if element.attrib["v"] not in lists:
                    lists[element.attrib["v"]] = 1
                else:
                    lists[element.attrib["v"]] += 1
    return lists


def audit_way(filename):
    """Return list of name and count of ways."""
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
    """Return list of name and count of users."""
    users = {}
    for _, element in ET.iterparse(filename):
        if "user" in element.attrib:
            if element.attrib["user"] not in users:
                users[element.attrib["user"]] = 1
            else:
               users[element.attrib["user"]] += 1
    return users


def audit_tag(filename):
    """Return list of tag and count."""
    tags = {}
    for _, element in ET.iterparse(filename):
        if element.tag not in tags:
            tags[element.tag] = 1
        else:
            tags[element.tag] += 1
    return tags


def audit_member(filename):
    """Return list of name and count of members."""
    members = {}
    for _, element in ET.iterparse(filename):
        if element.tag == "member":
            if element.attrib["ref"] not in members:
                members[element.attrib["ref"]] = 1
            else:
                members[element.attrib["ref"]] += 1
    return members

def audit():
    lists = audit_tag_key('../sendai_japan.osm', 'postcode')
    pprint.pprint(lists)
    print len(lists)


if __name__ == "__main__":
    audit()