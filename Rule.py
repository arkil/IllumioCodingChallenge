# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:59:31 2019

@author: Arkil Thakkar
"""

from collections import defaultdict

from PortTrie import PortTrie
class Rule(object):
   
    def __init__(self):
        self.rule_dict = defaultdict(PortTrie)
       
    def add_rule(self, direction, protocol, ports, ips):
        port_trie = self.rule_dict[direction+protocol]
        for port in ports:
            ip_trie = port_trie.add_port(port)
            for ip in ips:
                ip_trie.add_ip(ip)
       
    def validate_rule(self, direction, protocol, port, ip):
        port_trie = self.rule_dict[direction+protocol]
        if not port_trie:
            return False
        ip_trie = port_trie.find_port(port)
        if not ip_trie:
            return False
        return ip_trie.find_ip(ip)
