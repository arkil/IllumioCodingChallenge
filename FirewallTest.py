# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:02:18 2019

@author: Arkil Thakkar
"""


from Firewall import Firewall


import unittest


class FirewallTest(unittest.TestCase):
    
    def setUp(self):
        self.firewall = Firewall("rules.csv")
    def test_firewall_accept_packet_1(self):
        res = self.firewall.accept_packet("inbound", "tcp", 80, "192.168.1.2")
        self.assertTrue(res)
    def test_firewall_accept_packet_2(self):
        res = self.firewall.accept_packet("inbound", "udp", 53, "192.168.2.1")
        self.assertEqual(res, True)
    def test_firewall_accept_packet_3(self):
        res =self.firewall.accept_packet("outbound", "tcp", 10234, "192.168.10.11")
        self.assertEqual(res, True)
    def test_firewall_accept_packet_4(self):
        self.assertEqual(self.firewall.accept_packet("inbound", "tcp", 81, "192.168.1.2"),False)
    def test_firewall_accept_packet_5(self):
        self.assertEqual(self.firewall.accept_packet("inbound", "udp", 24, "52.12.48.92"),False)
    def test_firewall_accept_packet_6(self):
        self.assertEqual(self.firewall.accept_packet("inbound", "udp", 53, "192.168.2.6"),False)x
        
if __name__ == '__main__':
    unittest.main()