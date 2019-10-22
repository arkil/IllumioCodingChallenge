# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:53:47 2019

@author: Arkil Thakkar
"""

class IPTrieNode(object):
   
    def __init__(self, bit):
        self.bit = bit
        self.children = list()
        self.is_leaf = False

class IPTrie(object):
   
    def __init__(self):
        self.root = IPTrieNode("*")
       
    def convert_ip(self,ip):
        bin_ip = bin(ip)[2:]
        if len(bin_ip) != 32:
            missing_bits_len = 32-len(bin_ip)
            bin_ip = "0"*missing_bits_len+bin_ip
        return bin_ip
       
    def add_ip(self, ip):
        bin_ip = self.convert_ip(ip)
        node = self.root
        for bit in bin_ip:
            found_in_child = False
            for child in node.children:
                if child.bit == bit:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = IPTrieNode(bit)
                node.children.append(new_node)
                node = new_node
        node.is_leaf = True
       
    def find_ip(self, ip):
        bin_ip = self.convert_ip(ip)
        node = self.root
        for bit in bin_ip:
            bit_not_found = True
            for child in node.children:
                if child.bit == bit:
                    bit_not_found = False
                    node = child
                    break
            if bit_not_found:
                return False
        return True
