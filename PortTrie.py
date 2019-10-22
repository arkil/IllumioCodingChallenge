# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:56:43 2019

@author: Arkil Thakkar
"""
from IPTrie import IPTrie

class PortTrieNode(object):
   
    def __init__(self, bit):
        self.bit = bit
        self.children = list()
        self.is_leaf = False
        self.ip_trie = IPTrie()

class PortTrie(object):
   
    def __init__(self):
        self.root = PortTrieNode("*")
       
    def convert_port(self,port):
        bin_port = bin(port)[2:]
        if len(bin_port) != 16:
            missing_bits_len = 16-len(bin_port)
            bin_port = "0"*missing_bits_len+bin_port
        return bin_port
       
    def add_port(self, port):
        bin_port = self.convert_port(port)
        node = self.root
        for bit in bin_port:
            found_in_child = False
            for child in node.children:
                if child.bit == bit:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = PortTrieNode(bit)
                node.children.append(new_node)
                node = new_node
        node.is_leaf = True
        return node.ip_trie
       
    def find_port(self, port):
        bin_port = self.convert_port(port)
        node = self.root
        for bit in bin_port:
            bit_not_found = True
            for child in node.children:
                if child.bit == bit:
                    bit_not_found = False
                    node = child
                    break
            if bit_not_found:
                return False
        return node.ip_trie