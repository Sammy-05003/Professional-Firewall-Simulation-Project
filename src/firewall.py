import logging
from datetime import datetime
from packet import Packet
from rules_manager import RulesManager

class Firewall:
    def __init__(self, rules_manager: RulesManager):
        self.rules_manager = rules_manager
        self.setup_logging()
        
    def setup_logging(self):
        logging.basicConfig(
            filename='firewall.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def process_packet(self, packet: Packet) -> bool:
        """
        Process a network packet and determine if it should be allowed or blocked
        Returns: True if packet is allowed, False if blocked
        """
        allowed = True
        rules = self.rules_manager.get_rules()
        
        for rule in rules:
            if (
                (rule.ip_address == packet.ip_address or rule.ip_address == "*") and
                (rule.port == packet.port or rule.port == "*") and
                (rule.protocol == packet.protocol or rule.protocol == "*")
            ):
                allowed = rule.action == "ALLOW"
                self.log_packet(packet, allowed)
                return allowed
        
        # Default policy: allow if no rules match
        self.log_packet(packet, allowed)
        return allowed
    
    def log_packet(self, packet: Packet, allowed: bool):
        """Log packet processing results"""
        status = "ALLOWED" if allowed else "BLOCKED"
        message = f"Packet {status}: IP={packet.ip_address}, Port={packet.port}, Protocol={packet.protocol}"
        logging.info(message)