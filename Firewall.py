# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:00:21 2019

@author: Arkil Thakkar
"""

from Rule import Rule

class Firewall(object):
   
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.rule = self.generate_firewall_rules()
       
    def partial_dec_ip(self, ind, ip_part):
        return ((256)**(3-ind))*int(ip_part)
       
    def generate_firewall_rules(self):
       
        rule = Rule()
       
        with open(self.csv_file_path,'r') as file:
           
            for line in file.readlines():
               
                direction, protocol, ports, ips = line.split(",")
                print("------------------------------------")
                print("\n", direction, protocol, ports, ips)
               
                if "-" in ports:
                    ports_range = ports.split("-")
                    ports = range(int(ports_range[0]),int(ports_range[1])+1)
                else:
                    ports = range(int(ports), int(ports)+1)
               
                print("Ports:", ports)
               
                if "-" in ips:
                    ips_range = ips.split("-")
                    dec_ip_start = 0
                    for ind, ip_part in enumerate(ips_range[0].split(".")):
                        dec_ip_start += self.partial_dec_ip(ind, ip_part)
                    dec_ip_end = 0
                    for ind, ip_part in enumerate(ips_range[1].split(".")):
                        dec_ip_end += self.partial_dec_ip(ind, ip_part)
                    ips = range(dec_ip_start, dec_ip_end+1)
                else:
                    dec_ip_start = 0
                    for ind, ip_part in enumerate(ips.split(".")):
                        dec_ip_start += self.partial_dec_ip(ind, ip_part)
                    ips = range(dec_ip_start, dec_ip_start+1)
                   
                print("Ips:", ips)
               
                rule.add_rule(direction, protocol, ports, ips)
               
        return rule
       
    def accept_packet(self, direction, protocol, port, ip):
        if port < 1 or port > 65535:
            return False
        ip_parts = ip.split(".")
        dec_ip = 0
        for ind, ip_part in enumerate(ip_parts):
            if int(ip_part) < 0 or int(ip_part) > 255:
                return False
            dec_ip += self.partial_dec_ip(ind, ip_part)
        return self.rule.validate_rule(direction, protocol, port, dec_ip)

