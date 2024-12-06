from dataclasses import dataclass

@dataclass
class Packet:
    """Represents a network packet"""
    ip_address: str
    port: str
    protocol: str  # TCP, UDP, ICMP, etc.
    
    def __str__(self):
        return f"Packet(IP={self.ip_address}, Port={self.port}, Protocol={self.protocol})"