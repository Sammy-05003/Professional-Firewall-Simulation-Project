import unittest
from src.firewall import Firewall
from src.rules_manager import RulesManager
from src.packet import Packet

class TestFirewall(unittest.TestCase):
    def setUp(self):
        self.rules_manager = RulesManager()
        self.firewall = Firewall(self.rules_manager)
        
        # Add some test rules
        self.rules_manager.add_rule("192.168.1.1", "80", "TCP", "BLOCK")
        self.rules_manager.add_rule("10.0.0.*", "*", "UDP", "ALLOW")
    
    def test_block_specific_ip_and_port(self):
        packet = Packet("192.168.1.1", "80", "TCP")
        self.assertFalse(self.firewall.process_packet(packet))
    
    def test_allow_wildcard_ip(self):
        packet = Packet("10.0.0.5", "443", "UDP")
        self.assertTrue(self.firewall.process_packet(packet))
    
    def test_default_allow(self):
        packet = Packet("172.16.0.1", "22", "TCP")
        self.assertTrue(self.firewall.process_packet(packet))

if __name__ == '__main__':
    unittest.main()